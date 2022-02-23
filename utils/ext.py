import discord
from discord.ext import commands

import psycopg2
from psycopg2 import extras

import functools

import requests 

import sys
import os

import errors

def output_to_channel(*channels):
    def inner(cog_function):
        @functools.wraps(cog_function)
        async def wrapper(cls, ctx, *args, **kwargs):

            output_channels = []
            for channel in cls.bot.get_all_channels():
                if str(channel.type) == "text":
                    if channel.name.lower() in [i.lower() for i in channels]:
                        output_channels.append(channel)
                    elif str(channel.id) in channels:
                        output_channels.append(channel)
            ctx.output_channels = output_channels

            await cog_function(cls, ctx, *args, **kwargs)

        return wrapper

    return inner


def dm_only(cog_function):
    @functools.wraps(cog_function)
    async def wrapper(cls, ctx, *args, **kwargs):
        if ctx.guild:
            raise errors.PrivateMessageOnly("This has personal information in it!")
        return await cog_function(cls, ctx, *args, **kwargs)

    return wrapper


def send_to_dm(cog_function):
    @functools.wraps(cog_function)
    async def wrapper(cls, ctx, *args, **kwargs):
        ctx.channel = await ctx.author.create_dm()
        return await cog_function(cls, ctx, *args, **kwargs)

    return wrapper


