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

  if message.content == '$list':
    if 'encouragements' in db.keys():
      encouragements_list = list(db['encouragements'])
      await message.channel.send(encouragements_list)
    else:
      await message.channel.send("No encouragement message has been saved")

client.run(os.getenv("TOKEN"))
