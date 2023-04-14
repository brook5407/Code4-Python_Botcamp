import discord
import os
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
typo_words = ["Twddy", "Taddy", "Trddy", "Tnddy?", "Tmddy?"]

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if any(word in message.content for word in typo_words):
        await message.channel.send('Did you mean Teddy?')

client.run(os.getenv("TOKEN"))
