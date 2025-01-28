import os
import discord
from keepalive import keep_alive


DISCORD_TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello World!')
    if message.content.startswith('!up'):
        await message.channel.send('Yeah still up!!')
    if message.content.startswith('!ping'):
        await message.channel.send('pong!')




client.run(DISCORD_TOKEN)
