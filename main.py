from discord.ext import commands
import discord
import os
import asyncio

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())
my_secret = os.environ['TOKEN']

@bot.event
async def on_ready():
  print(f'We have logged in as {bot.user}')

async def load():
  for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
      await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
  async with bot:
    await load()
    await bot.start(my_secret)
    
asyncio.run(main())
