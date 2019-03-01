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
    id = client.get_guild(511573334966665226)
    channels = ["commands"]

@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if channel.name == 'lobby':
            await client.send_message(channel, f"Üdvözöllek, {member.mention}!")
                                     
           
@client.event
async def on_member_remove(member):
    for channel in member.server.channels:
        if channel.name == 'lobby':
            await client.send_message(channel, f"Itt hagyott minket {member.mention}!")
    
@client.event
async def on_ready():
    await client.change_presence(game=Game(name='Fornax2'))
    print('Kész!')
    
@client.event
async def on_message(message):
    if message.content == '!event':
        await client.send_message(message.channel,'Hétvégi eventeink a következők: **Okey kártya :okey:** event **szombat 23:59-ig**,')
        await client.send_message(message.channel,'**Hatszög kincsesláda :hatszog:** event **szombat 23:59-ig**,')
        await client.send_message(message.channel,'**Holdfény kincsesláda :HF:** event **szombat 23:59-től vasárnap 23:59-ig**,')
        await client.send_message(message.channel,'**Ezen felül +30% tárgy dropp van a szerveren, egész hétvégén!**')
        await client.send_message(message.channel,'**(2019.03.02-03.03)**')
        
    
client.run('NTE2MDM2MTM5MjQ1ODk1NzAx.D1rihg.LxhU3j9lN_Db1tZZgsgkQc2GR6I')
