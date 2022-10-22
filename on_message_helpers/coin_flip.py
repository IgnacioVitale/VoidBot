import random


async def coin_flip(ctx):
    coin_head = "head"
    coin_tails = "tails"
    coin_throw = random.randint(1, 2)
    if coin_throw == 1:
        await ctx.channel.send(f"Your coin landed on {coin_head}")
    else:
        await ctx.channel.send(f"Your coin landed on {coin_tails}")
