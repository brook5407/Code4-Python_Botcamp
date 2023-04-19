import discord
import os
import requests
from bs4 import BeautifulSoup
import json
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

  if message.content.split()[0] == '$movie':
      name = message.content[7:]
      if not name:
        await message.channel.send("Please enter a movie name")
      else:
        headers = {"user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15"}
        r_search = requests.get(f"https://www.imdb.com/find?q={name}&s=tt&ttype=ft&ref_ =fn_ft", headers=headers)
        if r_search.status_code != 200:
          await message.channel.send("Invalid link")
        else:
          html_search = r_search.text
          soup_search = BeautifulSoup(html_search, "html.parser")
          soup_search = soup_search.find('script', id='__NEXT_DATA__').text
          json_search = json.loads(soup_search)
          result_search = json_search['props']['pageProps']['titleResults']['results']
          movie_id = result_search[0]['id'] if result_search else None
          if movie_id is not None:
            r_movie = requests.get(f"https://www.imdb.com/title/{movie_id}", headers=headers)
            if r_movie.status_code != 200:
              await message.channel.send("Movie Id not found")
            else:
              html_movie = r_movie.text
              soup_movie = BeautifulSoup(html_movie, "html.parser")
              text_movie = soup_movie.find('script', type="application/ld+json").text
              json_movie = json.loads(text_movie)
              movie_name = json_movie['name']
              storyline = json_movie['description']
              output = f"Movie Name: {movie_name} \nStoryline: {storyline}" 
              await message.channel.send(output)
          else:
            await message.channel.send("Movie Name not found")
            
client.run(os.getenv("TOKEN"))
