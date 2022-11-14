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
country=''

# Startup Information
@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))      

#Bot commands
#Send the formatted link to the channel
@client.command()
async def coordinates(channel):
    channel = client.get_channel(1040967366835699765)
    await channel.send(formatLink("https://maps.googleapis.com/maps/api/streetview?size=400x400&location=47.5763831,-122.4211769&fov=80&heading=70&pitch=0&key=" + MAPS_TOKEN))

@client.command()
async def startgame(ctx):
    await ctx.send('Welcome the game will start in 5 seconds.\nGet ready!')
    time.sleep(5)
    await ctx.send('First round\n'+formatLink())

#Functions
def generateXCoordinate():
    global xdecimal
    x = random.uniform(-90.0000000, 90.000000)
    xdecimal = round(x, 6)
    return xdecimal

def generateYCoordinate():
    global ydecimal
    y = random.uniform(-180.000000, 180.000000)
    ydecimal = round(y, 6)
    return ydecimal
 
#Function to replace longitude and latitude in link
def formatLink():
    link = "https://maps.googleapis.com/maps/api/streetview?size=400x400&location=47.5763831,-122.4211769&fov=80&heading=70&pitch=0&key=" + MAPS_TOKEN
    reverse_geocode_result = gmaps.reverse_geocode((generateXCoordinate(), generateYCoordinate()))

    while(reverse_geocode_result[len(reverse_geocode_result)-1]['address_components'][len(reverse_geocode_result[len(reverse_geocode_result)-1]['address_components'])-1]['types'][0] == 'country'):
        global xdecimal
        global ydecimal
        global country

        xdecimal = generateXCoordinate()
        ydecimal=generateYCoordinate()
        print(xdecimal, ydecimal)
        reverse_geocode_result = gmaps.reverse_geocode((xdecimal, ydecimal))
        link = 'https://maps.googleapis.com/maps/api/streetview?size=400x400&location='+str(xdecimal)+','+str(ydecimal)+'&fov=80&heading=70&pitch=0&key=' + MAPS_TOKEN

    print(link)
    return link

def getCountry(lat, long):
    reverse_geocode_result = gmaps.reverse_geocode((lat, long))

    if(reverse_geocode_result[len(reverse_geocode_result)-1]['address_components'][len(reverse_geocode_result[len(reverse_geocode_result)-1]['address_components'])-1]['types'][0] == 'country'):
        country = reverse_geocode_result[len(reverse_geocode_result)-1]['address_components'][len(reverse_geocode_result[len(reverse_geocode_result)-1]['address_components'])-1]['long_name']
        print(country)
    else:
        print('error')

    return country

#Run the bot
client.run(TOKEN)