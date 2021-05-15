import os
from keep_alive import keep_alive
from discord.ext import commands
import os
import discord
from replit import db
import discord_rpc
import tracemalloc
import time

token = os.environ['.env']

bot = commands.Bot(
    command_prefix="=",  # Change to desired prefix
    case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 773466452661108747 and 576773600905003039 #ash, joelteon (discord id's to mark who the developers are)



@bot.event
async def on_ready():  # When the bot is ready
	print("Online")
	print(bot.user)  # Prints the bot's username and identifier
	print('bot online')
	await bot.change_presence(
	    activity=discord.Activity(name='spotify!', type=2)
	    #activity=discord.Activity(name='Spotify', type=2)
	    )
	    


extension = [
    'cogs.example',  # Same name as it would be if you were importing it
    'cogs.about',
    'cogs.data',
    'cogs.image',
    'cogs.text'
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extension:
		bot.load_extension(extension)  # Loades every extension.

keep_alive()  # Starts a webserver to be pinged.

bot.run(token)  # Starts the bot
