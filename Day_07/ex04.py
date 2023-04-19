import discord
import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content == '$job':
      r = requests.get('https://yilinnnnn.github.io/yillinnnnn.github.io/')
      if r.status_code != 200:
        await message.channel.send("Invalid link")
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
        await message.channel.send(embed=embed)
        
client.run(os.getenv("TOKEN"))
