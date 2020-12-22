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