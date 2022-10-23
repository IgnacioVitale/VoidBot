import random

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


async def dice_roll(ctx):
    result_of_the_dices_throws = 0
    message_of_user = ctx.message.content
    await ctx.channel.send(message_of_user)
    quantity_of_throws = message_of_user[6:7]
    dice_thrown = message_of_user[8:]
    for i in range(0, int(quantity_of_throws)):
        result_of_the_dices_throws += random.choice(range(1, int(dice_thrown)))
    await ctx.channel.send(
        f"you have thrown {int(quantity_of_throws)} dice/s of {dice_thrown} "
        f"faces, and they sum {result_of_the_dices_throws}")
