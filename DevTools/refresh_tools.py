import discord
import os
from discord.ext import commands

class RefreshTools(commands.Cog):

  def __init__(self, client):
    self.client = client
  #Events
  @commands.Cog.listener()
  async def on_ready(self):
    print('DEVTOOLS: refresh_tools Cog Successfully Loaded')

  #Loads a single cog
  @commands.command()
  @commands.has_role('The Owner')
  async def load(self, ctx, extension):
    self.client.load_extension(f'Cogs.{extension}')
    print(f"RefreshTools: {extension} was loaded - by {ctx.message.author.name}#{ctx.message.author.discriminator}")

  #Unloads a single cog
  @commands.command()
  @commands.has_role('The Owner')
  async def unload(self, ctx, extension):
    self.client.unload_extension(f'Cogs.{extension}')
    print(f"RefreshTools: {extension} was unloaded - by {ctx.message.author.name}#{ctx.message.author.discriminator}")

  #Reloads a cogs - used to not need to restart bot
  @commands.command()
  @commands.has_role('The Owner')
  async def refresh(self, ctx, extension):
    self.client.unload_extension(f'Cogs.{extension}')
    self.client.load_extension(f'Cogs.{extension}')
    print(f"RefreshTools: {extension} was refreshed - by {ctx.message.author.name}#{ctx.message.author.discriminator}")

  #Reloads all cogs - used to not need to reload them one by one
  @commands.command()
  @commands.has_role('The Owner')
  async def refreshAll(self, ctx):
    finalTotal = 0
    for filename in os.listdir('./Cogs'):
      if filename.endswith('.py'):
        self.client.unload_extension(f'Cogs.{filename[:-3]}')
        self.client.load_extension(f'Cogs.{filename[:-3]}')
        print(f"RefreshTools: {filename[:-3]} was refreshed - by {ctx.message.author.name}#{ctx.message.author.discriminator}")
        finalTotal+= 1
    print(f"RefreshTools: {finalTotal} files were refreshed")

def setup(client):
  client.add_cog(RefreshTools(client))