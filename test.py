import discord

Token = 'MTAxMzExNTk4NjUyMzcxNzY2Mw.GKDQit.NgI62hZXj6Z_stIo-7cmLk5KM_M3Itg-t7_HwA'
GuildName = 'cuộc họp của những ông trùm đệ thầy bống'
intents = discord.Intents.default()
intents.messages = True
intents.members = True
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    guild = client.get_guild(1003713859594489926)
    print(guild.name)

    
client.run(Token)
