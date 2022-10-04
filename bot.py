import discord
from discord.ext import commands
import os
import random
import response

TOKEN = ('MTAxMzExNTk4NjUyMzcxNzY2Mw.GKDQit.NgI62hZXj6Z_stIo-7cmLk5KM_M3Itg-t7_HwA')

bot = commands.Bot(command_prefix='Dz', intents = discord.Intents.default())
client = discord.Client( intents = discord.Intents.default())

@bot.event
async def on_ready():
    print("Logged in as DzBot")

@bot.event
async def on_member_join(member):
    welcome_channel = '1019629501719773295'
    await welcome_channel.send("Welcome " + member.name + " to join out Discord server")



@bot.event
async def on_message(message):
    print("received " + message.content)
    content_list = message.content.split(' ')
    if message.author == bot.user:
        return
    if ("<@1013115986523717663>") in message.content:
        await message.channel.send(response.mentioned)
    if message.content.startswith("Dztest"):
        await message.channel.send("Complete")
    if message.content.startswith('wlc'):
        await message.channel.send(response.wlc.format(user = content_list[1]))
    if message.content.startswith("Dz"):
        content = message.content[3:]
        if content == 'help':
            await message.channel.send(response.help)
        await res(content)
def res(content):
    k = response.content[0]

bot.run(TOKEN)
#MTAxMzExNTk4NjUyMzcxNzY2Mw.GKDQit.NgI62hZXj6Z_stIo-7cmLk5KM_M3Itg-t7_HwA