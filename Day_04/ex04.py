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

    if message.content in rps_list:
        response = random.choice(rps_list)
        await message.channel.send(f"I choose {response[1:]}!")

        if response == message.content:
            await message.channel.send(f"Well, this is awkward... We both picked {response[1:]}.")
        elif (response == "$rock" and message.content == "$scissors") or (response == "$paper" and message.content == "$rock") or (response == "$scissors" and message.content == "$paper"):
            await message.channel.send(f"You won? I must be getting rusty. {message.content[1:].capitalize()} beats {response[1:]} any day of the week... except Tuesday.")
        else:
            await message.channel.send( f"Ha! I knew I'd win. {response[1:].capitalize()} beats {message[1:].content}. Did you really think you could beat me with {message[1:].content}? Rookie mistake!")

client.run(os.getenv("TOKEN"))
