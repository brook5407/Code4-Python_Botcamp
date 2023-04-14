import discord
import random
import os
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
typo_words = ["Twddy", "Taddy", "Trddy", "Tnddy?", "Tmddy?"]
rps_list = ["$rock", "$paper", "$scissors"]


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if any(word in message.content for word in typo_words):
        await message.channel.send('Did you mean Teddy?')

    if message.content == '$hello':
        await message.channel.send('Hello!')

    elif message.content == '$greet':
        await message.channel.send(f"Hello {message.author.name}")

    elif message.content == '$greetings':
        await message.channel.send(f"Hello {message.author.display_name}")

    elif message.content.startswith('$echo '):
        await message.channel.send(message.content[6:].format(message))

    elif message.content.startswith('$Say '):
        await message.delete()
        await message.channel.send(message.content[5:].format(message))

    elif message.content in rps_list:
        response = random.choice(rps_list)
        await message.channel.send(f"I choose {response[1:]}!")

        if response == message.content:
            await message.channel.send(f"Well, this is awkward... We both picked {response[1:]}.")
        elif (response == "$rock" and message.content == "$scissors") or (
                response == "$paper" and message.content == "$rock") or (
                response == "$scissors" and message.content == "$paper"):
            await message.channel.send(
                f"You won? I must be getting rusty. {message.content[1:].capitalize()} beats {response[1:]} any day of the week... except Tuesday.")
        else:
            await message.channel.send(
                f"Ha! I knew I'd win. {response[1:].capitalize()} beats {message[1:].content}. Did you really think you could beat me with {message[1:].content}? Rookie mistake!")

    elif message.content == '$help':
        embed = discord.Embed(title="Discord Bot Commands",
                              description="Here are the available commands for this bot:", color=0x00ff00)
        embed.add_field(name="$help", value="Show this help message", inline=False)
        embed.add_field(name="$greet", value="Greets user", inline=False)
        embed.add_field(name="$greetings", value="Greets user's nickname", inline=False)
        embed.add_field(name='$echo', value="Enables the bot to repeat the user’s message", inline=False)
        embed.add_field(name="$Say", value="Allows you to “speak” as the bot", inline=False)
        embed.add_field(name="$rock/ $paper/ $scissors (any)", value="Play a simple game of rock, paper scissors with the user", inline=False)
        await message.channel.send(embed=embed)

client.run(os.getenv("TOKEN"))
