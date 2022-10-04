from discord.ext import commands
import discord
import os

TOKEN = ('MTAxMzExNTk4NjUyMzcxNzY2Mw.GKDQit.NgI62hZXj6Z_stIo-7cmLk5KM_M3Itg-t7_HwA')

bot = commands.Bot(command_prefix='Dz', intents = discord.Intents.default())

@bot.event
async def on_ready():
    print("Logged in as DzBot")

@bot.event
async def on_member_join(member):
    welcome_channel = '1019629501719773295'

@bot.event
async def on_message(message):
    print("received")
    if message.author == bot.user:
        return
    if message.content.startswith("!test"):
        await message.channel.send("Complete")
    a = input("wwhat do u wanna say")
    if a == '.':return
    else: await message.channel.send(a)
    
bot.run(TOKEN)

#MTAxMzExNTk4NjUyMzcxNzY2Mw.GKDQit.NgI62hZXj6Z_stIo-7cmLk5KM_M3Itg-t7_HwA