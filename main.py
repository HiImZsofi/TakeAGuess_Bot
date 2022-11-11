#Imports
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Create bot
client = commands.Bot(intents=discord.Intents.all() , command_prefix= "!")

# Startup Information
@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

# Command
@client.command()
async def helloworld(ctx):
    await ctx.send('Hello World!')

#Get token from .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

#Run the bot
client.run(TOKEN)

