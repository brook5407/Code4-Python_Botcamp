import discord

intents = discord.Intents.default()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

client.run("MTA5NjA1NjU0NTgzMTMwMTI0Mg.GoQpaE.VrwuFyHNExJ-h6CMhZ6xa3mAdpSFgdytwoWO3Q")
