import discord
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

  if message.content == '$intro':
    bot_mention = client.user.mention
    await message.channel.send(file=discord.File('code4teen.png'))
    await message.channel.send(
      f"Hello coders!! am {bot_mention}. How can I assist you today? 🤖")


client.run(os.getenv("TOKEN"))
