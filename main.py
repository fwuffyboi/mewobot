from keep_alive import keep_alive
from discord.ext import commands
import os
import discord
import time

os.system('clear')
token = os.environ['.env']

bot = commands.Bot(
    	command_prefix="=",  # Change to desired prefix
    	case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 773466452661108747 and 576773600905003039 #ash, joelteon (discord id's to mark who the developers are)

@bot.event
async def on_ready():  # When the bot is ready
	print("")
	for i in range(3):
		print(bot.user)  # Prints the bot's username and identifier
	time.sleep(5)
	await bot.change_presence(
	activity=discord.Activity(name='Spotify!', type=2)
	#activity=discord.Activity(name='Netflix!', type=0)
	)
	print('activity: Spotify!')
	print('Type: 2 ; Listening to')


extension = [
    	'cogs.about',
    	'cogs.data',
    	'cogs.developer',
    	'cogs.image',
    	'cogs.text',
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extension:
		bot.load_extension(extension)  # Loades every extension.

keep_alive()  # Starts a webserver to be pinged.
bot.run(token)  # Starts the bot
