import discord
from discord.ext import commands
import os
import requests
import json
from keep_alive import keep_alive
import random

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='for vaccines'))

@client.event   
async def on_message(message):
  if message.author == client.user:
    return
  
