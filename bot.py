import discord
import os

TOKEN = os.getenv('TOKEN')
GuildName = 'cuộc họp của những ông trùm đệ thầy bống'
intents = discord.Intents.default()
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GuildName)
    print('{name} logged in {guildname} with the id:{id}'.format(name=client.user, guildname=guild.name, id=guild.id))

@client.event
async def on_message(message):
    print("received")
    if message.author == client.user:
        print("stop")
        return
    a = input("what do u wanna say?")
    await message.channel.send(a)
    
client.run(TOKEN)

#MTAxMzExNTk4NjUyMzcxNzY2Mw.GKDQit.NgI62hZXj6Z_stIo-7cmLk5KM_M3Itg-t7_HwA