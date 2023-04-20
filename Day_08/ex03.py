import discord
import os
import requests
import random
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
  if message.content == '$quote':
    url = "https://zenquotes.io/api/quotes"
    r = requests.get(url)
    if r.status_code != requests.codes.ok:
        r.raise_for_status()
    data = r.json()
    random_quote = random.choice(data)
    output = f"{random_quote['q']} - {random_quote['a']}"
    await message.channel.send(output)

client.run(os.getenv("TOKEN"))
    