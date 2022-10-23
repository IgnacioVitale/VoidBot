import discord
from discord.ext import commands
from dotenv import dotenv_values

from message_commands import *

config = dotenv_values('.env')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot_prefix = '!'
bot = commands.Bot(intents=intents, command_prefix=bot_prefix)


@bot.command()
async def greet(ctx, *names):
    await greet_user(ctx, *names)


@bot.command()
async def love(ctx: commands.Context):
    await love_user(ctx)


@bot.command()
async def coinflip(ctx):
    await coin_flip(ctx)


@bot.command()
async def allstar(ctx):
    await all_star(ctx)


@bot.command()
async def hello(ctx):
    await hello_there(ctx)


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
