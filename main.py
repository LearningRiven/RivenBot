import os
import discord
from discord.ext import commands
from Server.keep_alive import keep_alive

#Global tokens
BOT_TOKEN=os.environ['BOT_TOKEN']
BOT_PREFIX="."

#Intent
intents = discord.Intents.default()
intents.members = True

#Create the connection to the discord server
client = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)

#Loads a cog
@client.command()
@commands.has_role('The Owner')
async def load(ctx, extension):
  client.load_extension(f'Cogs.{extension}')

#Unloads a cog
@client.command()
@commands.has_role('The Owner')
async def unload(ctx, extension):
  client.unload_extension(f'Cogs.{extension}')

#Reloads a cog - used to not need to restart bot
@client.command()
@commands.has_role('The Owner')
async def reload(ctx, extension):
  client.unload_extension(f'Cogs.{extension}')
  client.load_extension(f'Cogs.{extension}')

#loops through the cogs folder pulling all of the python files out
for filename in os.listdir('./Cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'Cogs.{filename[:-3]}')

#Make sure the webserver keeps running
keep_alive()

#Use the token for the bot to connect the code to discord
client.run(BOT_TOKEN)