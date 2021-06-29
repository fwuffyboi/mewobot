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
    await ctx.send('yes, ' + (ctx.message.author.mention) + ', This bot is indeed, VERY cool :)')

  @commands.command(name='pingo')
  async def pingo(self, ctx):
    '''want thy latency?'''
    bot = self.bot
    await ctx.send(f'PING-PONG! {bot.latency} ms')
      
  @commands.command(name="mewo")
  async def mewo(self, ctx):
    await ctx.send("i am online and listening for commands! uwu")

# Adds cog
def setup(bot):
  bot.add_cog(aboutCommands(bot))
  