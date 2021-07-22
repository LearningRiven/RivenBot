import os
import discord
from discord.ext import commands
from DevTools.keep_alive import keep_alive

#Global tokens
BOT_TOKEN=os.environ['BOT_TOKEN']
BOT_PREFIX="."

#Intent
intents = discord.Intents.default()
intents.members = True

#Create the connection to the discord server
client = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)

#Load all of the cogs for the bot
for filename in os.listdir('./Cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'Cogs.{filename[:-3]}')

#Load necessary development tools
client.load_extension(f'DevTools.refresh_tools')
client.load_extension(f'DevTools.debugger')

#Start up the flask webserver to make sure the bot doesnt go offline
keep_alive()

#Use the token for the bot to connect the code to discord
client.run(BOT_TOKEN)