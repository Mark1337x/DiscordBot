import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import logging
import time
import random
from discord import Game


client = commands.Bot(command_prefix = '!')
client = discord.Client()



@client.event
async def on_message(message):
    id = client.get_guild(551076327025803291)
    channels = ["commands"]

@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if channel.name == 'general':
            await client.send_message(channel, f"Üdvözöllek, {member.mention}! Kérlek olvasd el a #❌szabályzat❌-ot!")
                                     
           
@client.event
async def on_member_remove(member):
    for channel in member.server.channels:
        if channel.name == 'general':
            await client.send_message(channel, f"Itt hagyott minket {member.mention}!")
    
@client.event
async def on_ready():
    await client.change_presence(game=Game(name='Fornax2'))
    print('Kész!')
    
@client.event
async def on_message(message):
    if message.content == '!teszteles':
        await client.send_message(message.channel,'Ez egy teszt')
        
    
client.run('NTE2MDM2MTM5MjQ1ODk1NzAx.D1rihg.LxhU3j9lN_Db1tZZgsgkQc2GR6I')
