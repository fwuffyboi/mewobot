import discord
from discord.ext import commands
import requests
import random


class imageCommands(commands.Cog, name='image'):

  def __init__(self, bot):
      self.bot = bot

  #Commands here:
  @commands.command(name='cat')
  async def image(self, ctx):
    """gives you a cat image"""
    cat_phrases = (random.choice(['cool cat!', 'aww, so floofy!', 'here you go uwu', 'Here!', 'look at the little floof, awww', 'cat really said :P']))
    await ctx.send(cat_phrases)
    x = requests.get('http://aws.random.cat/meow')
    y = x.json()
    await ctx.send(y['file'])


  #@commands.command(name='dog')
  #async def image(self, ctx):
    #dog_phrases = (random.choice(['nice', 'aww, very cute', 'here you go uwu', 'Here!', 'therapist: describe \'e\' in one sentence\nme: ', 'awww', 'blep', 'what does a dalmation say #after dinner? \n\'Thanks! that really hit the *spot*\'']))
    #await ctx.send(dog_phrases)
    #do = dog.getDog(directory=None, filename=None)
    #comp = do.json()
    #await ctx.send(comp['file'])

# Adds cog
def setup(bot):
  bot.add_cog(imageCommands(bot))
