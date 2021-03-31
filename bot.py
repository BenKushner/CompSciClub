import discord
from discord.ext import commands

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("Bot is on!")

client.run('ODI2NjE1NjA5NjQ2MzgzMTA0.YGPDxw.CC-sA7lYwD1SfCJRUgdSrkt70jM')
