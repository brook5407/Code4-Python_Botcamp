from discord.ext import commands
import random
import requests
import io
import aiohttp
from discord import Embed, File


class Day05(commands.Cog, name='Day 05'):

  def __init__(self, bot):
    self.bot = bot
    self.emoji_api = requests.get(
      "https://emoji-api.com/emojis?access_key=93a0b8c41787b2fe4ef88cdbce42ac50a0a25344"
    )
    self.gif_api = requests.get(
      'https://api.giphy.com/v1/gifs/random?api_key=heFoHbw4GhOjYFaNACiDgvwfIugmRSZw&tag=&rating=g'
    )

  @commands.Cog.listener()
  async def on_ready(self):
    print("day 05 is running")

  @commands.command()
  async def emoji(self, ctx):
    """Send a random emoji"""
    if self.emoji_api.status_code != 200:
      await ctx.send("Sorry, there was an error retrieving the emoji.")
    else:
      emojis = self.emoji_api.json()
      if not emojis:
        await ctx.send("Sorry, there are no emojis available.")
      else:
        random_emoji = random.choice(emojis)
        emoji_code = random_emoji['character']
        await ctx.send(emoji_code)

  @commands.command()
  async def emoji_embed(self, ctx):
    """Send a random emoji in embeded message"""
    embed = Embed(title="Emoji Function ON",
                  description="Sending emoji:",
                  color=0x8000FF)
    if self.emoji_api.status_code != 200:
      embed.add_field(name="Error: retrieving the emoji",
                      value="--Unsuccessful--",
                      inline=False)
    else:
      emojis = self.emoji_api.json()
      if not emojis:
        embed.add_field(name="Error: no emoji available",
                        value="--Unsuccessful--",
                        inline=False)
      else:
        random_emoji = random.choice(emojis)
        emoji_code = random_emoji['character']
        embed.add_field(name=emoji_code, value="--Successful--", inline=False)
    await ctx.send(embed=embed)

  @commands.command()
  async def gif(self, ctx):
    """Send a random gif in embeded message"""
    embed = Embed(title="GIFs Function ON",
                  description="Sending GIF:",
                  color=0x807689)
    if self.gif_api.status_code != 200:
      embed.add_field(name="Error: retrieving the GIFs",
                      value="--Unsuccessful--",
                      inline=False)
    else:
      gif = self.gif_api.json()
      if not gif:
        embed.add_field(name="Error: no GIFs available",
                        value="--Unsuccessful--",
                        inline=False)
      else:
        gif_data = self.gif_api.json()
        gif_url = gif_data['data']['images']['original']['url']
        embed.set_image(url=gif_url)
    await ctx.send(embed=embed)

  @commands.command()
  async def intro(self, ctx):
    """Send an introduction message with image"""
    bot_mention = ctx.bot.user.mention
    await ctx.channel.send(file=File('code4teen.png'))
    await ctx.channel.send(
      f"Hello coders!! am {bot_mention}. How can I assist you today? 🤖")

  @commands.command()
  async def img(self, ctx, url: str):
    """Send an image from a URL provided"""
    async with aiohttp.ClientSession() as session:
      async with session.get(url) as resp:
        if resp.status != 200:
            return await ctx.send('Could not download file...')
        data = io.BytesIO(await resp.read())
        await ctx.send(file=File(data, 'tmp.png'))

async def setup(bot):
  await bot.add_cog(Day05(bot))
