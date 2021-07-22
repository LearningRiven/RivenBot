import discord
from discord.ext import commands

#Just a helper class in case I want to debug something ever
class Debugger(commands.Cog):

  def __init__(self, client):
    self.client = client

  #Events
  @commands.Cog.listener()
  async def on_ready(self):
    print('DEVTOOLS: logger Cog Successfully Loaded')
    
def setup(client):
  client.add_cog(Debugger(client))