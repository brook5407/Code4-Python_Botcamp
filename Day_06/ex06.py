import discord
import os
from dotenv import load_dotenv
from replit import db

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


def delete_encouragement(index):
  if "encouragements" in db.keys() and index < len(db["encouragements"]):
    del(db["encouragements"][index])
    return True
  else:
    return False
    


@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$del '):
    if (message.content[5:].isnumeric() == True):
      if delete_encouragement(message.content[5:] == True):
        await message.channel.send("Encouragement message deleted")
      else:
        await message.channel.send("list index not found")
    else:
        await message.channel.send("Invalid index")

client.run(os.getenv("TOKEN"))
