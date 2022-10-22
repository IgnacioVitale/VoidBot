import discord
from dotenv import dotenv_values

config = dotenv_values('.env')
discord_api_key = config['DISCORD_API_KEY']
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

bot_prefix = './'


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    message_content = message.content
    # we get the channel members
    member_list = client.get_channel(message.channel.id).members

    # if the message is from the bot, we ignore it
    if message.author == client.user:
        return

    # greet command: greets the user, mentioning it. it can take both name and nickname
    if message_content.startswith(f'{bot_prefix}greet'):
        # we take the first word after ./greet
        name = message_content.split(" ")[1]

        # we search in the member_list for the name, both in nicknames and in names
        for member in member_list:
            if name.lower() == member.name.lower() or name.lower() == member.display_name.lower():
                await message.channel.send(f"Sup <@{member.id}>")

    # hello command: says hi
    if message_content.startswith('./hello'):
        await message.channel.send('Sup fam')


@client.event
async def on_message_delete(message):
    if message.author == client.user:
        await message.channel.send('Me estan censurando en vivo')
    else:
        await message.channel.send('Vi lo que borraste, picaron')


client.run(discord_api_key)
