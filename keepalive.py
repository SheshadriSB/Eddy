from flask import Flask
import threading
import os
import discord
from discord.ext import commands

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_bot():
    intents = discord.Intents.default()
    bot = commands.Bot(command_prefix='!', intents=intents)
    
    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user.name} ({bot.user.id})')

    bot.run(os.environ['DISCORD_TOKEN'])

if __name__ == '__main__':
    # Start Discord bot in a background thread
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.daemon = True  # Daemonize thread to exit when main thread exits
    bot_thread.start()

    # Run Flask app in the main thread (required for Render's port binding)
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port, use_reloader=False)
