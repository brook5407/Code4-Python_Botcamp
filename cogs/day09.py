from discord.ext import commands
import random
import discord

class Day09(commands.Cog, name='Day 09'):
  def __init__(self, bot: commands.Bot):
    self.bot = bot
    self.guessing = set()
  
  @commands.command(name='numberbomb')
  async def guessing_process(self, ctx: commands.Context):
    """
    Play a NumberBomb Game
    """
    lower, upper, guess = 1, 99, -1
    number = random.randint(lower, upper)

    def check(m: discord.Message):
      return m.channel == ctx.channel and m.author != self.bot.user

    prefix = "The NumberBomb game is start!\n🚫Rule: Guess the number within the range to avoid the bomb💣\n⁉️you can type 'STOP' anytime to stop the game\n"
    while guess != number:
      await ctx.send(f'{prefix} ▶️Please guess the number between {lower} to {upper}')
      msg = await self.bot.wait_for('message', check=check)
      if msg.content == 'STOP':
        await ctx.send("The game is over👾")
        return
      try: 
        guess = int(msg.content)
      except ValueError:
        prefix = ''
        await ctx.send(f'{msg.author.mention} Please key in a Number!')

      if guess > lower and guess > upper or guess < upper and guess < lower:
        prefix = 'Exceed the range!\n'
      elif guess > lower and guess < number:
        prefix, lower  = 'So close!!\n', guess
      elif guess < upper and guess > number:
        prefix, upper = 'So close!\n', guess

    await ctx.send(f"{msg.author.mention} got the Number BOMB! 💣")

async def setup(bot):
  await bot.add_cog(Day09(bot))