# import stuff
import os
import discord
from dotenv import load_dotenv

#load the environment variables from the .env file
load_dotenv()

# intents needed
intents = discord.Intents.default()
intents.message_content = True

# define client
client = discord.Client(intents = intents)
@client.event
async def on_ready():
    print("Eigenbot is eigenready! :)")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('bees'):
        await message.reply("The Entire Bee Movie Script")

#client token
client.run(str(os.environ.get('TOKEN')))
