import discord
import os
import requests
from bs4 import BeautifulSoup
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

  if message.content.startswith('$currency '):
      r = requests.get("https://mtradeasia.com/main/daily-exchange-rates/")
      if r.status_code != 200:
        await message.channel.send("Invalid link")
      else:
        html_doc = r.text
        currency = message.content[10:]
        soup = BeautifulSoup(html_doc, "html.parser")
        soup = soup.find('td', style="line-height: 1;")
        while soup is not None:
          if soup.text.split()[1] == currency:
            name = soup.text.split('\n')[3]
            update_currency = name.split(")")[1].strip() if ')'in name else name
            rate = soup.find_next("td").text.split()[0]
            break
          soup = soup.find_next('td', style="line-height: 1;")
        else:
          await message.channel.send("Currency Not found")
        output = "Currency: {}\nExchange Rate (MYR): {}".format(update_currency, rate)
        await message.channel.send(output)
 
client.run(os.getenv("TOKEN"))
