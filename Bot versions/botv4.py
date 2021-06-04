# check user's role before initiating a command
import os
import discord  
from discord.ext import commands
from dotenv import load_dotenv
import plotly.express as px
import yfinance as yf
import pandas as pd

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')
client = discord.Client()

#1. Displays confirmation after connecting with discord servers
@client.event
async def on_ready(): 
    print(
        f'Batman, {client.user.name} has connected to Discord!' +
        f'\n{client.user}\n '
        )


# 1. admin can create channel 
@bot.command(name='create-channel',help="creates a channel")
@commands.has_role('admin')
async def create_channel(ctx,channel_name='real-python'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels,name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel : {channel_name}')
        await guild.create_text_channel(channel_name)

# 2.  If an error occurs
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')
        # ctx.author.send will send a DM

# 3. show a particular stock details with image
@bot.command(name='show-stock',help="displays information of a stock")
async def display_stock(ctx,stock_name='AAPL',):
    
    data = yf.download(stock_name, period="1d",interval="1m",group_by="ticker")

    # to make use of time
    data.to_csv("stock_data.csv")
    data = pd.read_csv("stock_data.csv")

    # print(ctx.author) --> important to make a log file
    
    fig = px.line(data, x = 'Datetime', y = 'Close', title=stock_name+ ' Share Prices today')
    fig.write_image("fig1.png")


    
    await ctx.send(file=discord.File('fig1.png'))




bot.run(TOKEN)        