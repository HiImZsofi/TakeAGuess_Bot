#Imports
import os
from random import uniform
from collections import Counter
from operator import ge
import discord
import gmaps
from discord.ext import commands
from dotenv import load_dotenv

# Create bot
client = commands.Bot(intents=discord.Intents.all() , command_prefix= "!")


# Startup Information
@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))       

#Function to replace longitude and latitude in link
def formatLink(link):
    replaceLet = link.replace("47.5763831", "40.75")
    replaceLong = replaceLet.replace("-122.4211769", "-74.00")
    return replaceLong

#Send the formatted link to the channel
@client.command()
async def replaceLink(channel):
    channel = client.get_channel(1040967366835699765)
    await channel.send(formatLink("https://maps.googleapis.com/maps/api/streetview?size=400x400&location=47.5763831,-122.4211769&fov=80&heading=70&pitch=0&key=" + MAPS_TOKEN))
   

#Get token from .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
MAPS_TOKEN = os.getenv("MAPS_TOKEN")

#Authenticate to Google Maps
gmaps.configure(MAPS_TOKEN)

#Run the bot
client.run(TOKEN)