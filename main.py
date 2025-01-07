import discord
from keepalive import keep_alive  
import os


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

    if message.content.startswith('!hello'):
        await message.channel.send('Hello fam!')
    if message.content.startswith('!UP'):
        await message.channel.send('Yeah dude, chill out!')

# Keep the bot alive using the keepalive method
keep_alive()

# Run the bot with the token from the .env file
client.run(os.getenv("BOT_TOKEN"))  # Ensure you have a .env file with your bot token
