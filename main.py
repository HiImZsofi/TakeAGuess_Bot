#Imports
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import time
import googlemaps

#Get token from .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GTOKEN = os.getenv("GOOGLE_TOKEN")

#Setup Google API
gmaps = googlemaps.Client(key=GTOKEN)

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

@client.command()
async def startgame(ctx):
    await ctx.send('Welcome the game will start in 5 seconds.\nGet ready!')
    time.sleep(5)
    await ctx.send('First round\nhttps://maps.googleapis.com/maps/api/streetview?size=400x400&location=34.478005,-51.224765&fov=80&heading=70&pitch=0&key='+GTOKEN)

def getCountry(lat, long):
    reverse_geocode_result = gmaps.reverse_geocode((lat, long))

    if(reverse_geocode_result[len(reverse_geocode_result)-1]['address_components'][len(reverse_geocode_result[len(reverse_geocode_result)-1]['address_components'])-1]['types'][0] == 'country'):
        country = reverse_geocode_result[len(reverse_geocode_result)-1]['address_components'][len(reverse_geocode_result[len(reverse_geocode_result)-1]['address_components'])-1]['long_name']
        print(country)
    else:
        print('error')


#Run the bot
client.run(TOKEN)

