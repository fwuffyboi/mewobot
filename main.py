import os
from keep_alive import keep_alive
from discord.ext import commands
import os
import discord
from replit import db
import discord_rpc
import tracemalloc
import time


numcount = 0

token = os.environ['.env']

 
bot = commands.Bot(
	command_prefix="!",  # Change to desired prefix
	case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 773466452661108747  # Change to your discord id!!!


@bot.event 
async def on_ready():  # When the bot is ready
    print("Online")
    print(bot.user)# Prints the bot's username and identifier
    print('bot online')
    await bot.change_presence(activity=discord.Activity(name='spotify', type=2))
    #await bot.change_presence(activity=discord.State(text='Enjoying life!')) #keep this bit



extensions = [
	'cogs.example',  # Same name as it would be if you were importing it
  'cogs.about',
  'cogs.data',
  'cogs.image'
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loades every extension.

keep_alive()  # Starts a webserver to be pinged.

bot.run(token)  # Starts the bot