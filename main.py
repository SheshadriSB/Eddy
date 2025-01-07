import discord
from keepalive import keep_alive  
import os
from dotenv import load_dotenv


load_dotenv()

    if message.author == client.user:
        return


    if message.content.startswith('!hello'):
        await message.channel.send('Hello fam!')
    if message.content.startswith('!UP'):
        await message.channel.send('Yeah dude, chill out!')


keep_alive()


client.run(os.getenv("BOT_TOKEN"))  
