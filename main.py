import os
import discord
from flask import Flask
from threading import Thread
from waitress import serve  # Changed import

app = Flask(__name__)

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

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    serve(app, host='0.0.0.0', port=port)  # Changed to Waitress

def run_bot():
    client.run(DISCORD_TOKEN)

if __name__ == '__main__':
    flask_thread = Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    run_bot()
