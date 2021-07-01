Hello guys, this is my journey to creating an interactive bot on discord. Further, the bot will be tweaked in order to show information regarding stocks.

I will not be talking about the formalities to generate a basic bot with no functions in discord for the time being.

This repo will contain all the versions of the bot I make from the beginning with nothing in them till the final bot.

## .env
The .env file contains the variables one requires while working with a discord bot. In the beginning, it must contain, the token generated for the bot that we get from the Discord developer page.


## botv1.py 
This file highlights the bot name and mentions the servers it's connected to.

## botv2py
This version of the bot deals with the command "99!" that displays random messages from the created list with the help of the on_message event handler. Exception handling has also been dealt with in this iteration

Here we made use of the client which is a superclass of the bot. In the next version, we will see the bot implementation.

## botv3.py
In this file , we shift from making use of client to using bot.command. This specifies the name and provides information on what it does. The bot will accept a command only if it has a '!' in its prefix. This version of bot is able to roll n number of die and display their respective result.

## botv4.py
This bot iteration creates a channel only if the person calling the command has the role of an admin. If a non-admin user call the function , it immediately informs the user that they don't have the permission.

The command "show-stock" displays present day graph of the mentioned stock as an image. For this , we required kaleido to generate an image and plotly for making the graph with the data we got from yfinance.

## botv5.py
This bot gives End of the Day (EOD) details of the company stock along with the rest of the commands already given in previous versions. It shows the details in a specific format of pointers. 

## botv6.py
This displays stock updates of a company every hour. Since market opens at 9:30am - 4:00pm , the hoursly updates follow after every hour starting form 9:30. Time between 3:30pm to 4:00pm is considered as individual update.

Like previously , the rest functions are present in this iteration too.