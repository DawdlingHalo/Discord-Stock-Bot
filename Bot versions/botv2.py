# Events performed with the help of client
# See how exceptions are raised and logged  
import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')# Discord token

client = discord.Client()


@client.event
async def on_ready():
    print(
        f'Batman, {client.user.name} has connected to Discord!' +
        f'\n{client.user}\n '
        )

@client.event
async def on_member_join(member): # not working currently
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, mere Server par swagat hai twaada !'
    )    

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content =='99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
    elif message.content =='raise-exception': # Allows to raise Discord Exception on command
        raise discord.DiscordException

@client.event
async def on_error(event,*args,**kwargs):
    with open('err.log','a') as f :
        if event == 'on_message':
            f.write(f'Unhandled message:{args[0]}\n')
        else:
            raise discord.DiscordException   

client.run(TOKEN)
