from discord.ext import commands
from replit import db

class Day06(commands.Cog, name='Day 06'):
  def __init__(self, bot):
    self.bot = bot
    if "encouragements" not in db.keys():
      db["encouragements"] = []
    self.list = db["encouragements"]

  @commands.Cog.listener()
  async def on_ready(self):
    print("day 05 is running")

  @commands.command()
  async def new(self, ctx, *, message):
    self.list.append(message)
    await ctx.send("new encouraging message added.")

  @commands.command()
  async def list(self, ctx):
    await ctx.send(list(self.list))

  @commands.command()
  async def delete(self, ctx, index: int):
    del(self.list[index])
    await ctx.send("Encouragement message deleted")

  @commands.command()
  async def del_list(self, ctx, index: int):
    del(self.list[index])
    await ctx.send("Encouragement message deleted")
    await ctx.send(list(self.list))

  @new.error
  async def new_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("$new <message>")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("ERROR: invalid message")
    else:
        await ctx.send(f"ERROR: {error}")
  
  @delete.error
  async def delete_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("$delete <index>")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("ERROR: invalid index")
    else:
        await ctx.send(f"ERROR: {error}")

  @del_list.error
  async def del_list_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("$del_list <index>")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("ERROR: invalid index")
    else:
        await ctx.send(f"ERROR: {error}")
      
async def setup(bot):
  await bot.add_cog(Day06(bot))