import os
import discord
import requests
import json
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return quote

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event 
async def on_member_join(member):
  role = discord.utils.get(member.guild.roles, name='The Lost')
  await member.add_roles(role)

@client.event 
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$inspire'):
    await message.channel.send(get_quote())

  if message.content.startswith('$commands'):
    commands = """
$commands - get a list of the available commands
$inspire_me - random inspirational quote
"""
    await message.channel.send(commands)

keep_alive()
client.run(os.environ['BOT_TOKEN'])