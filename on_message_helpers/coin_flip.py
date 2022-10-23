import random

from utils import mention_id


async def coin_flip(ctx):
    user = ctx.message.author.id
    coin_head = "head"
    coin_tails = "tails"
    coin_throw = random.randint(1, 2)
    if coin_throw == 1:
        await ctx.channel.send(f"{mention_id(user)} Your coin landed on {coin_head}")
    else:
        await ctx.channel.send(f"{mention_id(user)} Your coin landed on {coin_tails}")
