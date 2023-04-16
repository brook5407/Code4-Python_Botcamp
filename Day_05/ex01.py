import discord
import random
import requests
import os
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

    if message.content == '$emoji':
      response = requests.get("https://emoji-api.com/emojis?access_key=93a0b8c41787b2fe4ef88cdbce42ac50a0a25344")
      if response.status_code != 200:
        await message.channel.send("Sorry, there was an error retrieving the emoji.")
      else:
        emojis = response.json()
        if not emojis:
          await message.channel.send("Sorry, there are no emojis available.")
        else:
          random_emoji = random.choice(emojis)
          emoji_code = random_emoji['character']
          await message.channel.send(emoji_code)

client.run(os.getenv("TOKEN"))
