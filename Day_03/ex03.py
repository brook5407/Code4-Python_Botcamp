import discord
import os
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
client.run(os.getenv("TOKEN"))
