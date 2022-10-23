import random
import discord
import asyncio
from utils import mention_id


async def all_star(ctx):
    await ctx.channel.send(f"🎵 HEY NOW, YOU'RE A ROCKSTAR.. 🎵 \n https://youtu.be/L_jWHffIx5E?t=37")


async def coin_flip(ctx):
    user = ctx.message.author.id
    coin_head = "head"
    coin_tails = "tails"
    coin_throw = random.randint(1, 2)
    if coin_throw == 1:
        await ctx.channel.send(f"{mention_id(user)} Your coin landed on {coin_head}")
    else:
        await ctx.channel.send(f"{mention_id(user)} Your coin landed on {coin_tails}")


async def greet_user(ctx, *names):
    name = ' '.join(names)
    members = ctx.message.channel.members
    # member_list = ctx.get_channel(ctx.channel.id).members
    for member in members:
        if name.lower() == member.name.lower() or name.lower() == member.display_name.lower():
            await ctx.channel.send(f"Sup {mention_id(member.id)}")


async def love_user(ctx):
    user = ctx.message.author.id
    new_msg = await ctx.channel.send(f"I love you {mention_id(user)}")
    await new_msg.add_reaction('❤️')


async def hello_there(ctx):
    # User that requests the greeting
    greeted_user_id = ctx.message.author.id
    # This is hardcoded for now, we'll evaluate other options later.
    source = await discord.FFmpegOpusAudio.from_probe("audio_files/shrek_hello_there.m4a", method='fallback')
    # First, we check if the user calling is in a VC.
    user_in_vc = ctx.message.author.voice
    if user_in_vc:
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
    else:
        await ctx.channel.send(f"Hey {mention_id(greeted_user_id)}, you're not in a VC! Please join one so i can greet you 💌 :)!")
