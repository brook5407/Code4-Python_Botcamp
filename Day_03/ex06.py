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

    if message.content == '$hello':
        await message.channel.send('Hello!')

    if message.content == '$greet':
        await message.channel.send(f"Hello {message.author.name}")

    if message.content == '$greetings':
        await message.channel.send(f"Hello {message.author.display_name}")

client.run(os.getenv("TOKEN"))
