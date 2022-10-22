from sys import prefix
import discord
from discord.ext import commands
from dotenv import dotenv_values
from on_message_helpers.all_star import all_star
from on_message_helpers.greet import greet
config = dotenv_values('.env')
discord_api_key = config['DISCORD_API_KEY']
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
            await ctx.channel.send(f"Sup <@{member.id}>")

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    message_content = message.content

    # We grab the first word which determines the command.
    command = message_content.split(" ")[0]

    # If the message does not start with the predix OR from the bot, return.
    if command[:2] != prefix or message.author == bot.user:
        return

    ## We already checked for the prefix, we simply take the command.
    command = command[2:]

    # Get the member list.
    member_list = bot.get_channel(message.channel.id).members

    # Match the 'commmand' to a specific function called from the 'on_message_helpers' directory
    match command:
        case "allstar":
            await all_star(message)
        case "hello":
            await message.channel.send('Sup fam')
        case _:
            return


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

bot.run(discord_api_key)
