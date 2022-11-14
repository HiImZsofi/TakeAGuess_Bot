#Imports
import os
from random import uniform
from collections import Counter
from operator import ge
import random
import discord
import gmaps
from discord.ext import commands
from dotenv import load_dotenv
import numpy as np
import time
import googlemaps

#Get token from .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
MAPS_TOKEN = os.getenv("MAPS_TOKEN")

gmaps = googlemaps.Client(key=MAPS_TOKEN)
#Authenticate to Google Maps
#gmaps.configure(MAPS_TOKEN)

# Create bot
client = commands.Bot(intents=discord.Intents.all() , command_prefix= "!")
xdecimal = 0
ydecimal = 0

# Startup Information
@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))      


#Send the formatted link to the channel
@client.command()
async def coordinates(channel):
    channel = client.get_channel(1040967366835699765)
    await channel.send(formatLink("https://maps.googleapis.com/maps/api/streetview?size=400x400&location=47.5763831,-122.4211769&fov=80&heading=70&pitch=0&key=" + MAPS_TOKEN))

@client.command()
async def startgame(ctx):
    await ctx.send('Welcome the game will start in 5 seconds.\nGet ready!')
    time.sleep(5)
    await ctx.send('First round\nhttps://maps.googleapis.com/maps/api/streetview?size=400x400&location=34.478005,-51.224765&fov=80&heading=70&pitch=0&key='+MAPS_TOKEN)

def generateCoordinates():
    x = random.randrange(-90, 90)
    y = random.randrange(-180, 180)
    xdecimal = round(x, 6)
    ydecimal = round(y, 6)
 
#Function to replace longitude and latitude in link
def formatLink(link):
    reverse_geocode_result = gmaps.reverse_geocode((xdecimal, ydecimal))
    while(reverse_geocode_result[len(reverse_geocode_result)-1]['address_components'][len(reverse_geocode_result[len(reverse_geocode_result)-1]['address_components'])-1]['types'][0] == 'country'):
        generateCoordinates()

    replaceLet = link.replace("47.5763831", str(xdecimal))
    replaceLong = replaceLet.replace("-122.4211769", str(ydecimal))

def getCountry(lat, long):
    reverse_geocode_result = gmaps.reverse_geocode((lat, long))

    if(reverse_geocode_result[len(reverse_geocode_result)-1]['address_components'][len(reverse_geocode_result[len(reverse_geocode_result)-1]['address_components'])-1]['types'][0] == 'country'):
        country = reverse_geocode_result[len(reverse_geocode_result)-1]['address_components'][len(reverse_geocode_result[len(reverse_geocode_result)-1]['address_components'])-1]['long_name']
        print(country)
    else:
        print('error')

#Run the bot
client.run(TOKEN)