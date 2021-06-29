import discord
from discord.ext import commands
import sys
import time

def shutdown():
	sys.exit() 

class aboutCommands(commands.Cog, name='about commands'):
  def __init__(self, bot):
    self.bot = bot

  #Commands here:
  @commands.command(name='about')
  async def about(self, ctx):
    '''
    BASIC info on mewo
    '''
    await ctx.send("Mewobot is a random bot based around cats.")
    await ctx.send('*uwu emoticon here*')

  @commands.command(name='coolbot')
  async def cool_bot(self, ctx):
    """Is the bot cool?"""
    await ctx.send('yes, ' + (ctx.message.author.mention) + ', This bot is indeed VERY cool :)')

  @commands.command(name='onlinecheck')
  async def onlinecheck(self, ctx):
    """ Mewobot\'s ping page """
    await ctx.send('https://mewo.fluffywolff.repl.co ' + (ctx.message.author.mention))
    await ctx.send('''
 _______    _______    ________    _______                 ______    _______    _______ 
|   |   |  |    ___|  |  |  |  |  |       |    _______    |   __ \  |       |  |_     _|
|       |  |    ___|  |  |  |  |  |   -   |   |_______|   |   __ <  |   -   |    |   |  
|__|_|__|  |_______|  |________|  |_______|               |______/  |_______|    |___|  

 _______    _______    _____      _______    _______    _______ 
|       |  |    |  |  |     |_   |_     _|  |    |  |  |    ___|
|   -   |  |       |  |       |   _|   |_   |       |  |    ___|
|_______|  |__|____|  |_______|  |_______|  |__|____|  |_______|
''')

  @commands.command(name='pingo')
  async def pingo(self, ctx):
    '''want latency?'''
    bot = self.bot
    await ctx.send(f'PING-PONG! {bot.latency} ms')
      

# Adds cog
def setup(bot):
  bot.add_cog(aboutCommands(bot))
  