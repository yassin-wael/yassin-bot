import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="Nex Network"))


@client.event
async def on_member_join(member):
    print("recognised that a member called " + member.name + " joined")
    await client.send_message(member, "welcome to the server! we hope you will enjoy your stay :heart:")
    print("send message to " + member.name)
    
@client.event    
    
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

client.run("NTc0Njc2NTM0OTE3MzMzMDAz.XM83XQ.D6nvAe3AdcxvxXF2d2bIR7Ua7q8")




