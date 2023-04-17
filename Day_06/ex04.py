import discord
import os
from dotenv import load_dotenv
from replit import db

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


def update_encoragements(encouraging_message):
  if "encouragements" in db.keys():
    db["encouragements"].append(encouraging_message)
  else:
    db["encouragements"] = [encouraging_message]


@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$new '):
    update_encoragements(message.content[4:])
    await message.channel.send("new encouraging message added.")

client.run(os.getenv("TOKEN"))
