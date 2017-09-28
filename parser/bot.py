try:
    import discord
except:
    print('''
    To run, first install discord.py:

        py -3 -m pip install -U discord.py
    ''')

import asyncio
import logging

logging.basicConfig(level=logging.INFO)

clientid = 356584423443005440
with open('secret.txt') as f:
    lines = f.read().splitlines()
    secret = lines[0]
    token = lines[1]

# invite link:
#   https://discordapp.com/oauth2/authorize?client_id=356584423443005440&scope=bot&permissions=0

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {} {}'.format(client.user.name, client.user.id))

@client.event
async def on_message(message):
    print('[{}] [{}] {}'.format(message.timestamp))
    print(message.author.display_name)
    print(message.content)
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

client.run(token)
