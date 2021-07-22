import discord
from discord.ext import commands
from discord.utils import get

DEFAULT_ROLE="The Lost"

class User(commands.Cog):

  DEFAULT_ROLE="The Lost"

  def __init__(self, client):
    self.client = client

  #Events
  @commands.Cog.listener()
  async def on_ready(self):
    print('Riven Bot Online')

  @commands.Cog.listener()
  async def on_member_join(self, member):
    role = get(member.guild.roles, name=DEFAULT_ROLE)
    await member.add_roles(role)
    print(f"{member} was given {role}")

  #Commands
  #@commands.command()

def setup(client):
  client.add_cog(User(client))