# dotenv and discord downloaded easily in vscode
# gives bot name and members if present in the server/guild
import os

import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()



@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    # guild = discord.utils.get(client.guilds,name=GUILD)
    # guild = discord.utils.find(lambda g : g.name ==GUILD,client.guilds)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


client.run(TOKEN)

    

   
