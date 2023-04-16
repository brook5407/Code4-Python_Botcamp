import discord
import os
import io
import aiohttp
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

  if message.content.startswith('$img '):
    async with aiohttp.ClientSession() as session:
      async with session.get(message.content[5:]) as resp:
        if resp.status != 200:
          return await message.channel.send('Could not download file...')
        data = io.BytesIO(await resp.read())
        await message.channel.send(file=discord.File(data, 'tmp.png'))


client.run(os.getenv("TOKEN"))
