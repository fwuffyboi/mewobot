import discord
from discord.ext import commands
import requests
import random


class textCommands(commands.Cog, name='text'):

  def __init__(self, bot):
      self.bot = bot

  #Commands here:
  @commands.command(name='thonk')
  async def thonk(self, ctx):
    '''
    want a weird thought?
    '''
    think_phrase = (random.choice(['*head empty*', '*confuse 100*', 'do cats ever look at humans and ever wonder \'why arent they fluffy?\'', 'why is my name mewo?', 'dogs are great but cats are greater, or are they?????', 'want a talking topic? if so, use the \'=topic\' command']))
    await ctx.send(think_phrase)


  @commands.command(name='wsid')
  async def wsid(self, ctx):
    """What should you do?"""
    wsid_answers = random.randint['do it!!', 'pls dont do dat', 'idk' 'roll again ig?']
    await ctx.send(wsid_answers)

  @commands.command(name='aias')
  async def aias(self, ctx):
    """am i a shitposter? -probably... but lets find out!"""
    result = (random.randrange(0, 10))
    if result <5:
      await ctx.send('you got a ' + str(result) + ' thats ok')
    if result >5:
      await ctx.send('you got a ' + str(result) + ' thats bad.. oof')
    

# Adds cog
def setup(bot):
  bot.add_cog(textCommands(bot))
  