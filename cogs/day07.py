from discord.ext import commands
from replit import db
import requests
import json
from bs4 import BeautifulSoup

class Day07(commands.Cog, name='Day 07'):
  def __init__(self, bot):
    self.bot = bot
    self.header = {"user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15"}

  @commands.Cog.listener()
  async def on_ready(self):
    print("day 07 is running")

  @commands.command()
  async def scrap(self, ctx, url : str):
    """Scrape the first paragraph from selected website"""
    r = requests.get(url)
    if r.status_code is not requests.codes.ok:
      r.raise_for_status()
    else:
      html_doc = r.text
      soup = BeautifulSoup(html_doc, "html.parser")
      text = soup.p.text
      await ctx.send(text)

  @commands.command()
  async def programming(self, ctx):
    """Scrape the “Designed by” of the programming language"""
    r = requests.get("https://bohchuu.github.io/bc.github.io/")
    if r.status_code is not requests.codes.ok:
      r.raise_for_status()
    else:
      html_doc = r.text
      soup = BeautifulSoup(html_doc, "html.parser")
      soup_td = soup.tr.find_next('tr').find_next('tr').td
      creator_list = []
      for x in range(6):
        creator_list.append(soup_td.text)
        soup_td = soup_td.find_next('td')
      title = "Designed_by"
      gettext_python = creator_list[0]
      gettext_c = creator_list[1]
      gettext_cpp = creator_list[2]
      gettext_java = creator_list[3]
      gettext_js = creator_list[4]
      gettext_r = creator_list[5]
      output = f"**__{title}__** \nPython : {gettext_python} \nC: {gettext_c} \nC++ : {gettext_cpp} \nJava : {gettext_java} \nJavaScript : {gettext_js} \nR : {gettext_r} \n"
      await ctx.send(output)

  @commands.command()
  async def currency(self, ctx, currency : str):
    r = requests.get("https://mtradeasia.com/main/daily-exchange-rates/")
    if r.status_code is not requests.codes.ok:
      r.raise_for_status()
    else:
      html_doc = r.text
      soup = BeautifulSoup(html_doc, "html.parser")
      soup = soup.find('td', style="line-height: 1;")
      while soup is not None:
        if soup.text.split()[1] == currency:
          name = soup.text.split('\n')[3]
          update_currency = name.split(")")[1].strip() if ')'in name else name
          rate = soup.find_next("td").text.split()[0]
          output = "Currency: {}\nExchange Rate (MYR): {}".format(update_currency, rate)
          await ctx.send(output)
          break
        soup = soup.find_next('td', style="line-height: 1;")
      else:
        await ctx.send("Currency Not found")
  
  @commands.command()
  async def job(self, ctx):
    """Print the list of All Job Title, Company Name and Salary"""
    r = requests.get('https://yilinnnnn.github.io/yillinnnnn.github.io/')
    if r.status_code is not requests.codes.ok:
      r.raise_for_status()
    else:
      html_doc = r.text
      soup = BeautifulSoup(html_doc, "html.parser")
      jobs = soup.find_all('h3')
      companies = soup.find_all('p')
      salaries = soup.find_all('span', 'salary')
      for i in range(4):
        jobs[i] = jobs[i].text
        companies[i] = companies[i].text
        salaries[i] = salaries[i].text
      embed = discord.Embed(title="Job List:",
                        description="",
                        color=0xE06666)
      embed.add_field(name='Job1', 
                      value=f"{jobs[0]}, {companies[0]}\n{salaries[0]}",
                      inline = False)
      embed.add_field(name='Job2', 
                      value=f"{jobs[1]}, {companies[1]}\n{salaries[1]}",
                      inline = False)
      await ctx.send(embed=embed)
  
  @commands.command()
  async def movie(self, ctx, *, movie_name : str):
    """Search the storyline of the movie"""
    r_search = requests.get(f"https://www.imdb.com/find?q={movie_name}&s=tt&ttype=ft&ref_ =fn_ft", headers=self.header)
    if r_search.status_code != 200:
      await message.channel.send("Invalid link")
    else:
      html_search = r_search.text
      soup_search = BeautifulSoup(html_search, "html.parser")
      soup_search = soup_search.find('script', id='__NEXT_DATA__').text
      json_search = json.loads(soup_search)
      result_search = json_search['props']['pageProps']['titleResults']['results']
      movie_id = result_search[0]['id'] if result_search else None
      if movie_id is not None:
        r_movie = requests.get(f"https://www.imdb.com/title/{movie_id}", headers=self.header)
        if r_movie.status_code != 200:
          await message.channel.send("Movie Id not found")
        else:
          html_movie = r_movie.text
          soup_movie = BeautifulSoup(html_movie, "html.parser")
          text_movie = soup_movie.find('script', type="application/ld+json").text
          json_movie = json.loads(text_movie)
          movie_name = json_movie['name']
          storyline = json_movie['description']
          output = f"Movie Name: {movie_name} \nStoryline: {storyline}" 
          await ctx.send(output)
      else:
        await ctx.send("Movie name not found")
  
  @scrap.error
  async def scrap_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("$scrap <url>")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("ERROR: invalid url")
    else:
        await ctx.send(f"ERROR: {error}")

  @currency.error
  async def currency_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("$currency <currency code>")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("ERROR: invalid currency code")
    else:
        await ctx.send(f"ERROR: {error}")

  @movie.error
  async def movie_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("$movie <movie name>")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("ERROR: invalid movie name")
    else:
        await ctx.send(f"ERROR: {error}")


async def setup(bot):
  await bot.add_cog(Day07(bot))