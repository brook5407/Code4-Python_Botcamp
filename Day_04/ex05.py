import discord
import random
import os
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

rps_list = ["$rock", "$paper", "$scissors"]

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$help'):
        embed = discord.Embed(title="Discord Bot Commands",
                              description="Here are the available commands for this bot:", color=0x00ff00)
        embed.add_field(name="$help", value="Show this help message", inline=False)
        embed.add_field(name="$greet", value="Greets user", inline=False)
        embed.add_field(name="$greetings", value="Greets user's nickname", inline=False)
        embed.add_field(name="$echo", value="Enables the bot to repeat the user’s message", inline=False)
        embed.add_field(name="$Say", value="Allows you to “speak” as the bot", inline=False)
        embed.add_field(name="$rock/ $paper/ $scissors (any)", value="Play a simple game of rock, paper scissors with the user", inline=False)
        await message.channel.send(embed=embed)

client.run(os.getenv("TOKEN"))
