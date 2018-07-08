import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready(): 
    print("bot is ready")
    
@client.event
async def on_message(message):
    if message.content.startswith('!ping'):
        userID = message.author.id
        await client.send_message(message.channel,"<@%s> pong!" % (userID))
    if message.content.startswith('hey'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> hi" % (userID))   
          

client.run("NDUzOTcyODEyMDU5OTAxOTU0.DiPoug.qdnUKksJfrTyGTrxdJxEGy0bvC0")
