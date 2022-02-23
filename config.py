import discord
from discord.ext import commands

from constants import COMMAND_PREFIX

def init():
    global bot
    intents = discord.Intents.default()
    intents.members = True
    intents.guilds = True
    bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)
