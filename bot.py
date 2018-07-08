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
    await client.change_presence(game=discord.Game(name="24/7"))
    
@client.event
async def on_message(message):
    if message.content.startswith('!ping'):
        userID = message.author.id
        await client.send_message(message.channel,"<@%s> pong!" % (userID))
    if message.content.startswith('hey'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> hi" % (userID))  

async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        

          

client.run("NDUzOTcyODEyMDU5OTAxOTU0.DiPoug.qdnUKksJfrTyGTrxdJxEGy0bvC0")
