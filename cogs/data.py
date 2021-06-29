import discord
from discord.ext import commands
from replit import db
from random2 import seed
from random2 import randint

class dataCommands(commands.Cog, name='data commands'):

  def __init__(self, bot):
    self.bot = bot

  @commands.command(name='wmm')
  async def list(self, ctx):
    '''
    who made mewo?
    '''
    await ctx.send(db["id"])
    print(db["id"])

# Adds cog
def setup(bot):
  bot.add_cog(dataCommands(bot))