import discord
from keepalive import keep_alive  # Import the keepalive function to keep the bot alive
import os
from dotenv import load_dotenv

# Load environment variables from the .env file (for the bot token)
load_dotenv()

# Set intents to allow access to message content
intents = discord.Intents.default()
intents.message_content = True

# Create a client instance with the specified intents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# Keep the bot alive using the keepalive method
keep_alive()

# Run the bot with the token from the .env file
client.run(os.getenv("MTMyNjIyMDU1NDAzODAxODE1OQ.Gxh8XZ.s7lF2fZi1fMnA0eLtwJxjUq_heqYX_HK-vh9FE"))  # Ensure you have a .env file with your bot token
