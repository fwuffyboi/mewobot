import discord
from discord.ext import commands


class hidden(commands.Cog, name='hidden'):
  def __init__(self, bot):
    self.bot = bot

  #Commands here:
  @Commands.command(name='hidden')
  async def hidden(self, ctx):
    await ctx.send('this is the test command for \'=hidden\'')
# Adds cog
def setup(bot):
  bot.add_cog(hidden(bot))
  