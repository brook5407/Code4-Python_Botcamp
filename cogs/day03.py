from discord.ext import commands

class Day03(commands.Cog, name='Day 03'):
  def __init__(self, bot):
    self.bot = bot

  # @commands.Cog.listener()
  # async def on_ready(self):
  #   print("day 03 is running")
  
  @commands.command()
  async def hello(self, ctx):
    """Says hello"""
    await ctx.send('Hello!')

  @commands.command()
  async def greet(self, ctx):
    """Says hello <name>"""
    await ctx.send(f"Hello {ctx.author.name}")

  @commands.command()
  async def greetings(self, ctx):
    """Says hello <nickname>"""
    await ctx.send(f"Hello {ctx.author.display_name}")

async def setup(bot):
    await bot.add_cog(Day03(bot))
