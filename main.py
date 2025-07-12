import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} 작동 중!')

@bot.command()
async def 안녕(ctx):
    await ctx.send("안녕하세요!")

bot.run(os.getenv("TOKEN"))
