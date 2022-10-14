from email import message
import discord
from discord.ext import commands
import os
import random
import requests
from bs4 import BeautifulSoup
from imme import I, category, random_photo, random_num, playgame, game, bet
TOKEN = ('MTAxMzExNTk4NjUyMzcxNzY2Mw.GKDQit.NgI62hZXj6Z_stIo-7cmLk5KM_M3Itg-t7_HwA')
bot = commands.Bot(command_prefix='Dz', intents = discord.Intents.default())
client = discord.Client( intents = discord.Intents.default())

@bot.event
async def on_ready():
    print("Logged in as DzBot")
    
prev = ''
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return    
    punctuations = '!()-[]{};:\'"\\,<>./?#$%^&*_~'
    # remove punctuation from the string
    msg = ""
    for char in message.content.lower():
        if char not in punctuations:
            msg = msg + char    
    content = msg.split(' ')
    if content[0] == '@1013115986523717663':
        await message.channel.send(I['mentioned'].format(user='<@{id}>'.format(id=message.author.id)))
    elif content[0] in I :
        await message.channel.send(I[content[1]])
    elif len(content) > 1:
        if content[1] in I:
            await message.channel.send(I[content[1]])
    
        # SAO Easter Egg
    if len(content) > 1:
        if msg.startswith("system call "):
            content = msg[12:].split(" ")
            if content[0].lower() == "inspect":
                if content[1].lower() == "entire":
                    if content[2].lower() == "command":
                        if content[3].lower() == "list":
                            em = discord.Embed(title=f"🍢 SAO Command List", color=0x7400FF)
                            em.set_thumbnail(
                                url="https://cdn.discordapp.com/attachments/668816286784159763/674285661510959105/Kirito-Sao-Logo-1506655414__76221.1550241566.png")
                            em.add_field(name='Commands',
                                        value="generate xx element\ngenerate xx element xx shape\ninspect entire command list\n")

                            await message.channel.send(embed=em)
            elif content[0].lower() == "generate":
                if content[-1].lower() == "element":
                    em = discord.Embed(title=f"✏ Generated {content[1].lower()} element!",
                                    color=0xFF0000)
                    await message.channel.send(embed=em)
                if content[-1].lower() == "shape":
                    if content[2].lower() == "element":
                        em = discord.Embed(
                            title=f"✏ Generated {content[-2].lower()} shaped {content[1].lower()} element!",
                            color=0xFF0000)
                        await message.channel.send(embed=em)
                        
        elif content[0] == 'dz':
            if content[1] in category:
                await message.channel.send(random_photo(content[1]))
                print('done')
            elif len(content) > 2 and content[1] != 'random' and (content[2] == 'all' or content[2][0] in '0987654321'):
                await message.channel.send(bet(content[1]).format(id=message.author.id, money=[content[2], '150,000'][content[2] == 'all']))
            elif content[1] == 'random':
                if str(message.author.id) == '884071714038878258':
                    await message.channel.send('<:emoji_60:1022132953800781875> <@{id}> u killed {number} people <:anime1:1023528700593049610>'.format(id = message.author.id, number = str(int(content[2])-1)))
                else:
                    await message.channel.send('<:emoji_60:1022132953800781875> <@{id}> u killed {number} people <:anime1:1023528700593049610>'.format(id = message.author.id, number = random_num(content[2])))
            elif content[1] in game:
                await message.channel.send(playgame(content[1]).format(id=message.author.id))
                
        
    await bot.process_commands(message)




bot.run(TOKEN)
#MTAxMzExNTk4NjUyMzcxNzY2Mw.GKDQit.NgI62hZXj6Z_stIo-7cmLk5KM_M3Itg-t7_HwA