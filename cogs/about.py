import discord
from discord.ext import commands


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
    """ ---for developers"""
    await ctx.send('https://mewo.fluffywolff.repl.co ' + (ctx.message.author.mention))



# Adds cog
def setup(bot):
  bot.add_cog(aboutCommands(bot))
