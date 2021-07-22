import discord
from discord.ext import commands

class Channel(commands.Cog):

  def __init__(self, client):
    self.client = client

  #Commands
  @commands.command()
  @commands.has_role('The Owner')
  async def clear(self, ctx, amount=5):
    await ctx.channel.purge(limit=amount)

def setup(client):
  client.add_cog(Channel(client))