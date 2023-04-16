import discord
import os
import requests
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def get_reaction_emoji(word):
  response = requests.get(f"https://emoji-api.com/emojis?search={word}&access_key=93a0b8c41787b2fe4ef88cdbce42ac50a0a25344")
  emojis = response.json() if response.status_code == 200 else None
  if emojis:
    emojis = emojis[0]["character"]
  return emojis
  

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.split()[0] == '$react':
    await message.add_reaction('✔️')
    get_reaction_emoji(message.content.split()[1])
    emoji = get_reaction_emoji(message.content.split()[1])
    if emoji:
      await message.add_reaction(emoji)

client.run(os.getenv("TOKEN"))
