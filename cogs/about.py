import discord
from discord.ext import commands
import sys

def shutdown():
	sys.exit() 

class aboutCommands(commands.Cog, name='about commands'):
  def __init__(self, bot):
    self.bot = bot

  #Commands here:
  @commands.command(name='about')
  async def about(self, ctx):
    '''
    About 1
    '''
    await ctx.send("Mewobot is a random bot based around cats.")
    await ctx.send('''  
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⡆⠀⠀⢸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⣾⣿⡆⠀
⣿⣿⡇⠀⠀⢸⣿⢰⣿⡆⠀⣾⣿⡆⠀⣾⣷ ⣿⣿⡇⠀⠀⣿⣿⡇⠀
⣿⣿⡇⠀⠀⢸⣿⠘⣿⣿⣤⣿⣿⣿⣤⣿⡇⢻⣿⡇⠀⠀⣿⣿⡇⠀
⣿⣿⡇⠀⠀⢸⡿⠀⢹⣿⣿⣿⣿⣿⣿⣿⠁⢸⣿⣇⠀⢀⣿⣿⠇⠀
⠙⢿⣷⣶⣶⡿⠁⠀⠈⣿⣿⠟⠀⣿⣿⠇⠀⠈⠻⣿⣶⣾⡿⠋⠀⠀
    
    ''')

  @commands.command(name='coolbot')
  async def cool_bot(self, ctx):
    """Is the bot cool?"""
    await ctx.send('yes, ' + (ctx.message.author.mention) + ', This bot is indeed VERY cool :)')

  @commands.command(name='onlinecheck')
  async def onlinecheck(self, ctx):
    """ Mewobot\'s ping page """
    await ctx.send('https://mewo.fluffywolff.repl.co ' + (ctx.message.author.mention))

  @commands.command(name='ping')
  async def ping(self, ctx):
    '''ping command'''
    bot = self.bot
    await ctx.send(f'PONG! {bot.latency}')

  @commands.command(name='shutdownsys')
  async def shutdownsys(self, ctx):
    """ ---for developers"""
    if ctx.message.author.name == "576773600905003039" or "773466452661108747":
      await ctx.send('BOt SHUTTINg DOWn')
      sys.exit()
    else:
      await ctx.send('You do not have premission to use that command, ' + (ctx.mesage.author.mention))
      
  @commands.command(name='info')
  async def info(self, ctx):
  	"""provides in depth detail about mewobot"""
  	await ctx.send('to check mewobot\'s status, head over to https://stats.uptimerobot.com/LBYvotPr9m')
# Adds cog
def setup(bot):
  bot.add_cog(aboutCommands(bot))
  