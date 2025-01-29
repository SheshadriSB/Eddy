import os
import discord
from flask import Flask
from threading import Thread

# Initialize Flask app for health checks
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

# Discord bot setup
DISCORD_TOKEN = os.getenv("BOT_TOKEN")  # Make sure this matches Render's env var name

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
    app.run(host='0.0.0.0', port=port)

def run_bot():
    client.run(DISCORD_TOKEN)

if __name__ == '__main__':
    # Start Flask web server in a separate thread
    flask_thread = Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Run Discord bot in the main thread
    run_bot()
