# check user's role before initiating a command
import os
import time 
import discord  
from discord.ext import commands
from dotenv import load_dotenv
import plotly.express as px
import yfinance as yf
import pandas as pd
import datetime
import plotly.graph_objects as go


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')
client = discord.Client()

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

# 4. displays end of day data of a company
@bot.command(name='EOD',help="displays end of the day data of one company daily")
async def eod(ctx,stock_name = 'Tesla'):
    data = yf.download("GE", period="1d",group_by="ticker")
    
    data.to_csv("eod_stock_data.csv")
    data = pd.read_csv("eod_stock_data.csv")
    l1 = data.to_dict()
    columns = l1.keys()

    message = " EOD Data of company: " + stock_name
    for i in columns:
        x = f"\n- {i} :  {l1.get(i)[0]}" 
        message += x
    
    await ctx.send(message)

    time.sleep(10)
    eod(ctx,stock_name=stock_name)

# 5. Show hourly updates of a company
@bot.command(name='hour',help="displays end of the day data of one company daily")
async def hour(ctx,stock_name = 'TSLA'):
    data = yf.download(stock_name, period="1d",interval="1m",group_by="ticker")
    data.to_csv("hour_graph.csv")
    data = pd.read_csv("hour_graph.csv")
    # to find last hour
    now = datetime.datetime.now()
    current_hour = now.strftime("%H") # datatype: string
    if int(current_hour)<9 or int(current_hour)>16:
        last_hour = 14
    else:
        last_hour = int(current_hour) - 1
        # to find if minute is less than 30 or not
        minute = 0
        current_minute = now.strftime("%M")
        if(int(current_minute)<30):
            minute=0
            last_hour = last_hour -1
        else:
            minute=30

    print(f"last hour = {last_hour}"); # datatype : int

    # creating two new columns
    data['hour'] = [int(a.split()[1].split("-")[0].split(":")[0]) for a in data['Datetime']]
    data['minute'] = [int(a.split()[1].split("-")[0].split(":")[1]) for a in data['Datetime']]
    #generating two_hour_data
    two_hour_data = data[data['hour']==last_hour]
    data = two_hour_data.append(data[data['hour']==last_hour+1])
    # showing output graph
    title = stock_name+ ' Share Prices today ' + f"({last_hour}:30-{last_hour+1}:30)"
    fig = px.line(data[30:90], x='Datetime',y = 'Close', title=title )
    fig.write_image("hour_fig.png")
    
    await ctx.send(file=discord.File('hour_fig.png'))

# 6. show a trade updates of particular stock
@bot.command(name='tradeUpdate',help="displays trade updates of stock ")
async def display_stock(ctx,stock_name='AAPL',):
    #eod(ctx,stock_name = stock_name)
    data = yf.download(stock_name, period="1d",interval="1m",group_by="ticker")

    # to make use of time
    data.to_csv("tradeUpdate.csv")
    data = pd.read_csv("tradeUpdate.csv")

    # print(ctx.author) --> important to make a log file
    
    fig1 = px.line(data, x='Datetime',y = 'Close', title="Graph1 "+stock_name+ ' Share Prices today' )
    fig2 = go.Figure()
    for i in data.columns[1:6].to_list():
        fig2.add_scatter(x=data['Datetime'], y=data[i],name = i)
        
        fig2.update_layout(
            title= "Graph2 "+stock_name+ ' Share Prices today',
            xaxis_title="Datetime",
            yaxis_title="Price",
        )
    fig2.write_image("tradeUpdate2.png")
    fig1.write_image("tradeUpdate1.png")
    
    await ctx.send(file=discord.File('tradeUpdate1.png'))
    await ctx.send(file=discord.File('tradeUpdate2.png'))


bot.run(TOKEN)   
