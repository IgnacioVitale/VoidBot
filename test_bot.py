import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('./hello'):
        await message.channel.send('Sup fam')


@client.event
async def on_message_delete(message):
    if message.author == client.user:
        await message.channel.send('Me estan censurando en vivo')
    else:
        await message.channel.send('Vi lo que borraste, picaron')


client.run('MTAzMjk2NTY5OTYyMDA1MzA1Mw.GR4Qke.xLPeqa18P8xFBzK5rtCV-VgG9hA8PTZR0nSUZ0')
