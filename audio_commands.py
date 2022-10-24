import asyncio

import discord
import youtube_dl


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


async def stream(bot, ctx, *url):
    query = ' '.join(url)
    user_in_vc = ctx.message.author.voice
    user_channel = user_in_vc.channel
    vc = await user_channel.connect()

    async with ctx.typing():
        player = await YTDLSource.from_url(query, loop=bot.loop, stream=True)
        vc.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

    await ctx.send('Now playing: {}'.format(player.title))


async def stop_audio(bot, ctx):
    await ctx.voice_client.disconnect()
