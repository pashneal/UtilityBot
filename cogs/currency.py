from discord.ext import commands
import discord

import errors
import sys
import traceback

class Currency(commands.Cog):

    @errors.standard_error_handler
    async def cog_command_error(self, ctx, error):
        print("Ignoring exception in command {}:".format(ctx.command), file=sys.stderr)
        traceback.print_exception(
            type(error), error, error.__traceback__, file=sys.stderr
        )

