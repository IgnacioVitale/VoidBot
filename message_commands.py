import random
import re

import discord.ext.commands

from helpers.lichess import get_lichess_link
from utils import mention_id


async def all_star(ctx):
    await ctx.channel.send(f"🎵 HEY NOW, YOU'RE A ROCKSTAR.. 🎵 \n https://youtu.be/L_jWHffIx5E?t=37")


async def coin_toss(ctx):
    user = ctx.message.author.id
    coin_head, coin_tails = "head", "tails"
    coin_throw = random.randint(1, 2)
    if coin_throw == 1:
        await ctx.channel.send(f"{mention_id(user)} Your coin landed on {coin_head}")
    else:
        await ctx.channel.send(f"{mention_id(user)} Your coin landed on {coin_tails}")


async def dice_roll(ctx, text=None):
    result = 0
    example_for_the_text = "2d6 . First number for the quantity, second number for the faces."
    if not text or not re.match(r"\d+d\d+", text):
        await ctx.channel.send(f"Wrong format, the correct format is ---> {example_for_the_text}")
    else:
        quantity_of_dice = int(text.split("d")[0])
        faces_of_dice = int(text.split("d")[1])
        if not (faces_of_dice and quantity_of_dice):
            await ctx.channel.send(f" {mention_id(ctx.message.author.id)} rolls 0")
            return
        for _ in range(0, quantity_of_dice):
            result += random.randint(1, faces_of_dice)
        await ctx.channel.send(
            f" {mention_id(ctx.message.author.id)} rolls {result}")


async def greet_user(ctx, *names):
    name = ' '.join(names)
    members = ctx.message.channel.members
    # member_list = ctx.get_channel(ctx.channel.id).members
    for member in members:
        if name.lower() == member.name.lower() or name.lower() == member.display_name.lower():
            await ctx.channel.send(f"Sup {mention_id(member.id)}")
            return
    await ctx.channel.send(f"Sup stranger")


async def love_user(ctx: discord.ext.commands.Context):
    user = ctx.message.author.id
    await ctx.message.add_reaction('❤️')
    new_msg = await ctx.channel.send(f"I love you {mention_id(user)}")
    await new_msg.add_reaction('❤️')


async def shrekify_chat(ctx):
    await ctx.channel.send(
        "⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ \n"
        "⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ \n"
        "⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀ \n"
        "⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀ \n"
        "⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆ \n"
        "⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿ \n"
        "⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀ \n"
        "⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ \n"
        "⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ \n"
        "⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ \n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀ \n"
        "⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀ \n"
        "⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀ \n"
        "⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ \n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉                \n"
    )


async def chess_url(ctx):
    await ctx.channel.send(f"♘ {get_lichess_link()} ♝")
