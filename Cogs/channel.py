import discord
from discord.ext import commands

class Channel(commands.Cog):

  def __init__(self, client):
    self.client = client

  #Events
  @commands.Cog.listener()
  async def on_ready(self):
    print('COG:Channel Cog Successfully Loaded')

  #Commands
  @commands.command()
  @commands.has_role('The Owner')
  async def clear(self, ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    print(f"CHANNEL: '#{ctx.channel.name}' has had the last {amount} of messages cleared - by {ctx.message.author.name}#{ctx.message.author.discriminator}")


def setup(client):
  client.add_cog(Channel(client))