from discord.ext import commands
from discord.utils import get
import random
import json

import discord


with open('json/son.json') as f:
  son = json.load(f)

x = ''

class AUTO(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  
  @commands.Cog.listener()
  async def on_message(self, ctx):
    if "Upscaled" in ctx.content and ctx.channel.id in [1032086846970277988]:
      await ctx.pin()
      await ctx.channel.send("<@582730177763737640> i pinned the message dad :D")

    if "Question sent!" in ctx.content or "That user already has an active question" in ctx.content:
      if ctx.channel.id in [955333108125806644]:
        lmsg = ctx
        # await self.sleep(1)
        await lmsg.delete()
    listo = []
    foo = open('json/exempt.txt', 'r')
    for line in foo:
        listo.append(int(line))
    msg=ctx
    
      
    #   # if not(owo==None):
    #   #   if (owo[1] == 'w' and (uwu == ' ' or uwu == None)):
    #   #     lmsg=msg
    #   #     await lmsg.delete()
    #   # if not(ewe==None) and not(owo==None):
    #   #   if (ewe[1] == 'w' and (iwi == ' ' or iwi == None)) or (owo[1] == 'w' and (uwu == ' ' or uwu == None)):
    #   #     lmsg=msg
    #   #     if str(ctx.author.id) in ['358402076574744577','270048463079604224', '582730177763737640']:
    #   #       # print('okidoki :D')
    #   #       pass
    #   #     else:
    #   #       # print(ctx.author.id)
    #   #       await lmsg.delete()

    # if ctx.content[:2]=='r/':
    #   embed=discord.Embed(title=ctx.content, url=f'https://www.reddit.com/{ctx.content}',color=0xfe4503)
    #   embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1333471260483801089/OtTAJXEZ_400x400.jpg")
    #   await msg.channel.send(embed=embed)

    if not (ctx.author.bot or (ctx.channel.id in listo)):
      msg = ctx
    #   if '<@!582730177763737640>' in ctx.content:
    #       await msg.channel.send("you'd better have a reason")
    #   if '<@!302986022894043137>' in ctx.content:
    #     await msg.channel.send("oh boi. you're in for it now. you decided. with your smooth papega brain. that pinging austin. would be a good idea. oooooooh boi i would not wanna be you right now. you are in for quite the reckoning. may discord have mercy on your soul.")
      if not get(ctx.author.roles, name="optout"):
    #     if ctx.content[:3].lower() == "im ":
    #       await msg.channel.send(f"Hi {ctx.content[3:]}, I'm {random.choice(son)}.")
    #     elif ctx.content[:4].lower() == "i'm " or ctx.content[:4].lower() == "i’m ":
    #       await msg.channel.send(f"Hi {ctx.content[4:]}, I'm {random.choice(son)}.")
    #     if ctx.content[:3].lower() == "joe":
    #       await msg.channel.send('JOE MAMA <@' + str(msg.author.id) + '>')
    #     if ctx.content[:3].lower() == "lol":
    #       await msg.channel.send('rofl')
    #     if 'straight' in ctx.content:
    #       await msg.channel.send('*Audrey:* haha straight')
    #     if ctx.content.lower()=='yousef khan':
    #       await msg.channel.send('fesuoy nahk')
    #     if ctx.content=='sct':
    #       await msg.channel.send('teach me SOHCAHTOA teach me teach me SOHCAHTOA')

        content = ctx.content
        
    #     if ctx.content == 'bee' or ctx.content[-3:]=='bee':
    #       content = 'bee '
        listy=[]
        thefile= open('json/copypasta.txt', 'r')
        for x in thefile:
          response=[]
          stringie=''
          for index,piece in enumerate(x.split(':')):
            if not index==0:
              stringie += piece+':'
            else:
              response.append(piece)
          response.append(stringie[:-1])
          listy.append(response)
        for item in listy:
          if item[0] in content.lower():
            await msg.channel.send(item[1])

  


async def setup(bot: commands.Bot):
    await bot.add_cog(AUTO(bot))






