import os
from keep_alive import keep_alive
from discord.ext import commands
import os
import discord
from replit import db
from pypresence import Presence 
import tracemalloc


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
    #await bot.change_presence(game=discord.Game(name='stonks'))
    pres = Presence(839387154156879892)
    pres.connect()
    await BaseClient.handshake
    self.loop.run_until_complete(self.handshake())
    self._check_running()
    pres.update(state='hungry',details='meowing for food',large_image='mewo',large_image_key='mewobot')
    

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