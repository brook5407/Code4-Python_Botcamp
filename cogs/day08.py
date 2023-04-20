from discord.ext import commands
import requests
import random

class Day08(commands.Cog, name='Day 08'):
  def __init__(self,bot):
    self.bot = bot

  def get_ip(self):
    url = "https://api.ipify.org/?format=json"
    r = requests.get(url, timeout=10)
    if r.status_code != requests.codes.ok:
        r.raise_for_status()
    data = r.json()
    return data.get('ip')
    
  # @commands.Cog.listener()
  # async def on_ready(self):
  #   print("day 08 is running")
  
  @commands.command()
  async def ip(self, ctx):
    """Print Bot’s unique IP address"""
    bot_ip = self.get_ip()
    await ctx.send(bot_ip)

  @commands.command()
  async def iploc(self, ctx):
    """Print Bot's geographical location"""
    bot_ip = self.get_ip()
    url = f"https://ipinfo.io/{bot_ip}/geo"
    r = requests.get(url)
    if r.status_code != requests.codes.ok:
        r.raise_for_status()
    data = r.json()
    await ctx.send(f'{data["city"]}, {data["region"]}, {data["country"]}')

  @commands.command()
  async def quote(self, ctx):
    """Print  A random quote"""
    url = "https://zenquotes.io/api/quotes"
    r = requests.get(url)
    if r.status_code != requests.codes.ok:
        r.raise_for_status()
    quote_list = r.json()
    random_quote = random.choice(quote_list)
    await ctx.send(f"{random_quote['q']} - {random_quote['a']}")
    
async def setup(bot):
  await bot.add_cog(Day08(bot))
