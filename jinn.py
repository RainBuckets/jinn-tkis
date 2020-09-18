# jinn bot for TKIS by RainBuckets
import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get

# gets bot token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
ODDCH = os.getenv("SPOILERS_ODD")
EVENCH = os.getenv("SPOILERS_EVEN")

# gets bot object
bot = commands.Bot(command_prefix='!')

# bot is online
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# bot updates channel names
@bot.command(name='update-spoilers')
async def updatespoilers(ctx):
    odd = bot.get_channel(int(ODDCH))
    even = bot.get_channel(int(EVENCH))
    if odd.name < even.name:
        # change name to "spoilers_episode_odd+2"
        epnum = int(odd.name[-1]) + 2
        newname = odd.name[:-1] + str(epnum)
        await odd.edit(name=newname)
        await ctx.send("spoilers_episode_odd updated")
    else:
        # change name to "spoilers_episode_even+2"
        epnum = int(even.name[-1]) + 2
        newname = even.name[:-1] + str(epnum)
        await even.edit(name=newname)
        await ctx.send("spoilers_episode_even updated")

bot.run(TOKEN)
