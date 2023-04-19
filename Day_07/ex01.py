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

  if message.content.split()[0] == '$scrape':
      r = requests.get(message.content.split()[1])
      if r.status_code != 200:
        await message.channel.send("Invalid link")
      else:
        html_doc = r.text
        soup = BeautifulSoup(html_doc, "html.parser")
        soup_text = soup.p.text
        await message.channel.send(soup_text)
        
client.run(os.getenv("TOKEN"))
