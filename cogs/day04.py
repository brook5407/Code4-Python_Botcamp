from discord.ext import commands
import random
# from discord import Embed

class Day04(commands.Cog, name='Day 04'):
  def __init__(self, bot):
    self.bot = bot
    self.choice = ["rock", "paper", "scissor"]

  async def rps(self, ctx, choice):
    bot_choice = random.choice(self.choice)
    user_index = self.choice.index(choice)
    bot_index = self.choice.index(bot_choice)
    diff = user_index - bot_index
    if diff == 0:
      await ctx.send(f"Well, this is awkward... We both picked {bot_choice}")
    elif diff == -1 or diff == 2:
      await ctx.send(
        f"Ha! I knew I'd win. {bot_choice.capitalize()} beats {choice}. Did you really think you could beat me with {choice}? Rookie mistake!"
      )
    elif diff == 1 or diff == -2:
      await ctx.send(
        f"You won? I must be getting rusty. {choice.capitalize()} beats {bot_choice} any day of the week... except Tuesday."
      )

  # @commands.Cog.listener()
  # async def on_ready(self):
  #   print("day 04 is running")

  @commands.command()
  async def echo(self, ctx, *, message):
    """Repeats user message"""
    await ctx.send(message)

  @commands.command()
  async def say(self, ctx, *, message):
    """Repeats user message and delete user message"""
    await ctx.message.delete()
    await ctx.send(message)

  @commands.command()
  async def rock(self, ctx):
    """choose rock in rock, paper, scissor game"""
    await self.rps(ctx, 'rock')

  @commands.command()
  async def paper(self, ctx):
    """choose paper in rock, paper, scissor game"""
    await self.rps(ctx, 'paper')

  @commands.command()
  async def scissors(self, ctx):
    """choose scissor in rock, paper, scissor game"""
    await self.rps(ctx, 'scissor')
  
  @say.error
  async def say_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("$say <message>")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("ERROR: invalid message")
    else:
        await ctx.send(f"ERROR: {error}")

  
async def setup(bot):
  await bot.add_cog(Day04(bot))
