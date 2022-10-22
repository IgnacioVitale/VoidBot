import discord
from discord.ext import commands
from dotenv import dotenv_values

from on_message_helpers.coin_flip import coin_flip
from on_message_helpers.all_star import all_star
from utils import *

config = dotenv_values('.env')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot_prefix = './'
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


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    message_content = message.content
    command = message_content.split(" ")[0]

    # if the message is from the bot, we ignore it
    if message.author == bot.user:
        return

    if command == f"{bot_prefix}allstar":
        await all_star(message)
        return

    # hello command: says hi
    if message_content.startswith('./hello'):
        await message.channel.send('Sup fam')


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
