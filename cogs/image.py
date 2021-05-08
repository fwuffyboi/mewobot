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
    cat_phrases = (random.choice(['cool cat!', 'aww, so floofy!', 'here you go uwu', 'Here!', 'look at the little floof, awww', 'cat really said :P']))
    await ctx.send(cat_phrases)
    x = requests.get('http://aws.random.cat/meow')
    y = x.json()
    await ctx.send(y['file'])

# Adds cog
def setup(bot):
  bot.add_cog(imageCommands(bot))
