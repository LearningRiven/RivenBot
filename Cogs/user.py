import discord
from discord.ext import commands
from discord.utils import get

#Defaults
DEFAULT_ROLES="The Lost"
client = discord.Client()

class User(commands.Cog):

  def __init__(self, client):
    self.client = client

  #Events
  @commands.Cog.listener()
  async def on_ready(self):
    print('COG:User Cog Successfully Loaded')

  #Autorole Method - uses on_member_join in order to give a role to everyone 
  @commands.Cog.listener()
  async def on_member_join(self,member):
    role = get(member.guild.roles, name=DEFAULT_ROLES)
    await member.add_roles(role)
    print(f"USER: {member} has joined the server and was given {role}")
    channel = member.guild.get_channel(925933545854222356);
    await channel.send(f"{member} has left the server. We now have {member.guild.member_count} members");

  @commands.Cog.listener()
  async def on_member_remove(self,member):
    channel = member.guild.get_channel(925933545854222356);
    await channel.send(f"{member} has left the server. We now have {member.guild.member_count} members");

  #Admin Commands
  @commands.command()
  @commands.has_role('The Owner')
  async def updateAllMemberRoles(self, member):
    #TODO
    return

def setup(client):
  client.add_cog(User(client))