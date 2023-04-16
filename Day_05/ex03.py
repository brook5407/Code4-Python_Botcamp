import discord
import random
import json
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

  if message.content == '$gif':
    response = requests.get(
      'https://api.giphy.com/v1/gifs/random?api_key=heFoHbw4GhOjYFaNACiDgvwfIugmRSZw&tag=&rating=g'
    )
    embed = discord.Embed(title="GIFs Function ON",
                          description="Sending GIF:",
                          color=0x807689)
    if response.status_code != 200:
      embed.add_field(name="Error: retrieving the GIFs",
                      value="--Unsuccessful--",
                      inline=False)
    else:
      gifs = response.json()
      if not gifs:
        embed.add_field(name="Error: no GIFs available",
                        value="--Unsuccessful--",
                        inline=False)
      else:
        gif_data = json.loads(response.text)
        gif_url = gif_data['data']['images']['original']['url']
        embed.set_image(url=gif_url)
    await message.author.send(embed=embed)


client.run(os.getenv("TOKEN"))
