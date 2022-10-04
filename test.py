import discord

Token = 'MTAxMzExNTk4NjUyMzcxNzY2Mw.GKDQit.NgI62hZXj6Z_stIo-7cmLk5KM_M3Itg-t7_HwA'
GuildName = 'cuộc họp của những ông trùm đệ thầy bống'
intents = discord.Intents.default()
intents.messages = True
intents.members = True
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
    print("received")
    print(message.content)
    if message.content == 'wlc':
        await message.channel.send()
    
client.run(Token)
