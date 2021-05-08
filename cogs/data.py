import discord
from discord.ext import commands
from replit import db
from random2 import seed
from random2 import randint

class dataCommands(commands.Cog, name='data commands'):

  def __init__(self, bot):
    self.bot = bot

  #Commands here:
  @commands.command(name='add_developer')
  async def add(self, ctx):
    '''
    Add developer to list of developers
    '''
    value = randint(0, 10)
    db["id"] = ctx.message.mentions[0].id

  @commands.command(name='list_developer')
  async def list(self, ctx):
    '''
    list all the developers
    '''
    await ctx.send(db["id"])

# Adds cog
def setup(bot):
  bot.add_cog(dataCommands(bot))