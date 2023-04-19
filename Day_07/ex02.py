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

  if message.content == '$programming':
      r = requests.get("https://bohchuu.github.io/bc.github.io/")
      if r.status_code != 200:
        await message.channel.send("Invalid link")
      else:
        html_doc = r.text
        soup = BeautifulSoup(html_doc, "html.parser")
        soup_td = soup.tr.find_next('tr').find_next('tr').td
        creator_list = []
        for x in range(6):
          creator_list.append(soup_td.text)
          soup_td = soup_td.find_next('td')
        title = "Designed_by"
        gettext_python = creator_list[0]
        gettext_c = creator_list[1]
        gettext_cpp = creator_list[2]
        gettext_java = creator_list[3]
        gettext_js = creator_list[4]
        gettext_r = creator_list[5]
        output = f"**__{title}__** \nPython : {gettext_python} \nC: {gettext_c} \nC++ : {gettext_cpp} \nJava : {gettext_java} \nJavaScript : {gettext_js} \nR : {gettext_r} \n"
        await message.channel.send(output)
        
client.run(os.getenv("TOKEN"))
