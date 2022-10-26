import asyncio
from asyncio import sleep

import discord
import youtube_dl
from discord.ext import commands

from helpers.song_queue import SongQueue
from utils import mention_id

song_queue = SongQueue()

# TODO: MAKE THIS BETTER
ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'  # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=1):
        super().__init__(source, volume)

        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


async def stream(bot, ctx: discord.ext.commands.Context, *url):
    if song_queue.is_playing:
        return
    while song_queue.q:
        song_queue.is_playing = True
        query = ' '.join(song_queue.pop_upcoming())
        user_channel = ctx.message.author.voice.channel
        try:
            vc = await user_channel.connect()
        except:
            pass
        async with ctx.typing():
            player = await YTDLSource.from_url(query, loop=bot.loop, stream=True)
            vc.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

        await ctx.send('Now playing: {}'.format(player.title))
        while vc.is_playing():
            await sleep(1)
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
    song_queue.is_playing = False


async def add_to_queue(ctx: discord.ext.commands.Context, *url):
    song_queue.add_song(url)
    await ctx.channel.send(f"Query {' '.join(url)} added to queue!")


async def stop_audio(ctx: discord.ext.commands.Context):
    if ctx.voice_client:
        print('Disconecting . . .')
        await ctx.voice_client.disconnect()
    song_queue.empty()


async def hello_there(ctx):
    # User that requests the greeting
    greeted_user_id = ctx.message.author.id
    # This is hardcoded for now, we'll evaluate other options later.
    # First, we check if the user calling is in a VC.
    user_in_vc = ctx.message.author.voice
    if not user_in_vc:
        await ctx.channel.send(
            f"Hey {mention_id(greeted_user_id)}, you're not in a VC! Please join one so i can greet you 💌 :)!")
    else:
        source = await discord.FFmpegOpusAudio.from_probe("audio_files/shrek_hello_there.m4a", method='fallback')

        user_channel = user_in_vc.channel
        vc = await user_channel.connect()

        # This is a 'Future', and follows the design as suggested by the discord.py team.
        # Read more about this here: https://discordpy.readthedocs.io/en/latest/faq.html#how-do-i-pass-a-coroutine-to-the-player-s-after-function
        def exit_future(error):
            coro = vc.disconnect()
            loop = vc.loop
            future = asyncio.run_coroutine_threadsafe(coro, loop=loop)
            try:
                future.result()
            except:
                pass

        vc.play(source, after=exit_future)

