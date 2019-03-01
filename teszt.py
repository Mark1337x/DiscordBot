import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game



client = commands.Bot(command_prefix = '!')


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='      '))
    print('Ready, Freddy') 
@client.event
async def on_message(message):
    if message.content == '!teszteles':
        await client.send_message(message.channel,'Ez egy teszt')
client.run('NTE2MDM2MTM5MjQ1ODk1NzAx.D1rfaQ.uBr60osAgsZY9LNGjsuoequfOwM')
