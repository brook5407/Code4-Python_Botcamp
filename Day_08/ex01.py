import discord
import os
import requests
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def ip():
    url = "https://api.ipify.org/?format=json"
    r = requests.get(url, timeout=10)
    if r.status_code != requests.codes.ok:
        r.raise_for_status()
    data = r.json()
    return data.get('ip')

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
  if message.author == client.user:
        return

  if message.content == '$ip':
    await message.channel.send(ip())

client.run(os.getenv("TOKEN"))
    