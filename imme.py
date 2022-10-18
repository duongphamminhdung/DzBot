import requests
import random

mentioned = '''
Hiii this is my mini bot
my prefix is "Dz"
find out our command? type
System call inspect entire command list
'''

help = '''

category

image:
waifu neko shinobu megumin bully cuddle cry hug awoo kiss lick pat
smug bonk yeet blush smile wave highfive handhold nom bite glomp slap 
kill kick happy wink poke dance cringe

game:
random, coin, dice

remember my Dz prefix

'''

game = '''random coin dice'''
category = '''waifu neko shinobu megumin bully cuddle cry hug awoo kiss lick pat
smug bonk yeet blush smile wave highfive handhold nom bite glomp slap 
kill kick happy wink poke dance cringe'''

wlc = '''
Hiiiii
Welcome to SCARS
please pick role at <#1014744282491523082>  
u can introduce ur self at <#1019612377861345382>
hope u enjoy your time with us
'''

I = dict()
I['wlc'] = wlc; I['help'] = help; I['mentioned'] = mentioned
I['category'] = category; I['game'] = game
def random_photo(category):
    print('running random_photo')
    url = 'https://api.waifu.pics/sfw/' + category
    r = requests.get(url).text
    return r[8:-3]
    
def random_num(N):
    return random.randint(0, int(N))

def playgame(game):
    print("playgame...")
    if game == 'coin':
        return ('<@{id}> Tossing the coin......... '+random.choice(['Head', 'Tail']))
    elif game == 'dice':
        return ('<@{id}> congrats, your dice rolled '+str(random.randint(1, 6)))

def bet(game):
    print('bet...')
    if game == 'coin':
        return ('''<@{id}> spent  ${money}..... and chose Xấp
                Tossing the coin..... and u '''+random.choice(['Win', 'Lost']) + ' ${money}')
