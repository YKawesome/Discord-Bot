from discord.ext import commands
# import json
import discord
from discord import app_commands
from discord.ext.commands import Greedy, Context
# import urllib.request, urllib.parse, urllib.error



class APLCOMS(commands.Cog,description='Application Commands'):
  def __init__(self, bot):
    self.bot = bot
    
  def is_in_guild(guild_ids):
    async def predicate(ctx):
      go = False
      for thing in guild_ids:
        if ctx.guild.id == thing:
          go = True
          break
      return ctx.guild and go
    return commands.check(predicate)

  # @commands.command()
  # async def syncCommands(self, ctx: Context, guilds: Greedy[discord.Object]):
  #   synced = await ctx.bot.tree.sync()

  #   await ctx.send(f"Synced {len(synced)} commands globally.")
  #   return
    
  #   ret = 0
  #   for guild in guilds:
  #     try:
  #       await ctx.bot.tree.sync(guild=guild)
  #     except discord.HTTPException:
  #       pass
  #     else:
  #       ret+=1

  #     await ctx.send(f"Synced the tree.")
  
  @app_commands.command()
  async def testapp(self, interaction: discord.Interaction) -> None:
    await interaction.response.send_message("hello from the command!")


  
async def setup(bot: commands.Bot):
  await bot.add_cog(APLCOMS(bot))
