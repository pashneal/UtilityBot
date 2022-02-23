import discord
import config

config.init()

from constants import *

@config.bot.event
async def on_ready():
    print("Here, Ready!")


if __name__ == "__main__":
    config.bot.run(BOT_TOKEN)
