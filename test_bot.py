import discord
from discord.ext import commands
from dotenv import dotenv_values

from message_commands import *
from utils import *

config = dotenv_values('.env')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot_prefix = '!'
bot = commands.Bot(intents=intents, command_prefix=bot_prefix)


@bot.command()
async def greet(ctx, *names):
    name = ' '.join(names)
    member_list = bot.get_channel(ctx.channel.id).members
    for member in member_list:
        if name.lower() == member.name.lower() or name.lower() == member.display_name.lower():
            await ctx.channel.send(f"Sup {mention_id(member.id)}")


@bot.command()
async def love(ctx: commands.Context):
    user = ctx.message.author.id
    new_msg = await ctx.channel.send(f"I love you {mention_id(user)}")
    await new_msg.add_reaction('❤️')


@bot.command()
async def coinflip(ctx):
    await coin_flip(ctx)


@bot.command()
async def allstar(ctx):
    await all_star(ctx)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.event
async def on_message_delete(message):
    if message.author == bot.user:
        await message.channel.send('Me estan censurando en vivo')
    else:
        await message.channel.send('Vi lo que borraste, picaron')


# This block is to avoid errors when using a non-existent command
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    raise error


bot.run(config['DISCORD_API_KEY'])
