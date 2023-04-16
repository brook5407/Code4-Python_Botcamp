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

  if message.content == '$emoji_embed':
    response = requests.get(
      'https://emoji-api.com/emojis?access_key=93a0b8c41787b2fe4ef88cdbce42ac50a0a25344'
    )
    embed = discord.Embed(title="Emoji Function ON",
                          description="Sending emoji:",
                          color=0x8000FF)
    if response.status_code != 200:
      embed.add_field(name="Error: retrieving the emoji",
                      value="--Unsuccessful--",
                      inline=False)
    else:
      emojis = response.json()
      if not emojis:
        embed.add_field(name="Error: no emoji available",
                        value="--Unsuccessful--",
                        inline=False)
      else:
        random_emoji = random.choice(emojis)
        emoji_code = random_emoji['character']
        embed.add_field(name=emoji_code, value="--Successful--", inline=False)
    await message.author.send(embed=embed)


client.run(os.getenv("TOKEN"))
