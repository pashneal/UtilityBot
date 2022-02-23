import discord
import os

COMMAND_PREFIX = "!"
BOT_TOKEN = open("bot_token", "r").read()
DATABASE_URL = os.environ["DATABASE_URL"]

ERROR_COLOR = discord.Color(0xFF0000)
BOT_NAME = "Template"

# PRODUCTION SETTINGS
# GUILD_ID = 742543351126949930

# TEST SETTINGS
GUILD_ID = 730711352662032453
