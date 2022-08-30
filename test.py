import discord
import os

TOKEN = os.getenv('TOKEN')
GuildName = 'cuộc họp của những ông trùm đệ thầy bống'
intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GuildName)
    print('{name} logged in {guildname} with the id:{id}'.format(name=client.user, guildname=guild.name, id=guild.id))

@client.event
async def on_message(message):
    if message.author == client.user:
        print("stop")
        return
    prefix = 'Dz '
    print("received")
    channel = message.channel.name
    command = message.content[len(prefix):]
    
        
async def getmsg(ctx, channel, member):
    msg = discord.utils.get(await channel.history(limit = 1).flatten(), author = member)
    return msg
client.run(TOKEN)
