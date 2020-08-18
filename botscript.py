from discord.ext import commands
from time import time

import re
import discord

bot = commands.Bot(command_prefix='do ')

# EDIT STUFF HERE
with open('inputs', 'r') as f:
    TOKEN, channelList = f.read().splitlines()

# dank memer related stuff
fishDetectionText = "ahhhhh the fish is too strong and your line is at risk to break! quick, type the phrase below in the next 10 seconds"
searchDetectionText = "Where do you want to search? Pick from the list below and type it in chat."
dragonDetectionText = "Holy fucking shit god forbid you find something innocent like a duck, ITS A DRAGON! Type the phrase below in the next 10 seconds or you're toast!"

searchOptionRanking = [
    ["Dresser", "Tree", "Attic"],
    ["Bed", "Pantry", "Coat", "Pocket", "Couch", "Mailbox", "Laundromat"],
    ["Discord", "Shoe", "Dumpster", "Grass", "Dog", "Sewer", "Hospital"],
    ["Street", "Purse", "Car"]
]

iteration = 0

@bot.event
async def on_ready():
    print('Connected')

@bot.event
async def on_message(message):
    con = message.content

    # Detects fish typing event
    if str(message.channel) in channelList and fishDetectionText in con:
        mainText = con.split()[25:]

        with open('ggwp.txt', 'w', encoding='utf-8') as f:
            f.write(' '.join(mainText)[1:-1])
        
        print('Fish.. ', ' '.join(mainText)[1:-1], f'{message.channel}')
    
    # Detects search options
    if str(message.channel) in channelList and searchDetectionText in con:
        mainText = [i.replace('`', '').replace(',', '') for i in con.split()[16:]]
        rankedList = [0, 0, 0]
    
        for c, i in enumerate(searchOptionRanking):
            for b, option in enumerate(mainText):
                if option.capitalize() in i:
                    rankedList[b] = c
        
        with open('ggwp2.txt', 'w') as f: 
            f.write(mainText[rankedList.index(min(rankedList))])

    # Detects dragon events
    if str(message.channel) in channelList and dragonDetectionText in con:
        mainText = con.split()[28:]

        with open('ggwp3.txt', 'w', encoding='utf-8') as f:
            f.write(' '.join(mainText)[1:-1])
        
        print('Dragon.. ', ' '.join(mainText)[1:-1], f' {message.channel}')
    
    # Detects general events
    try:
        eventString = re.search(r"(typing|Type)\s[`](.*)[`]", con)
        s, e = eventString.span()
       
        checkList = [True if i not in con else False for i in [dragonDetectionText, fishDetectionText]]

        if str(message.channel) in channelList and all(elem == True for elem in checkList) and eventString:
            with open('ggwp4.txt', 'w', encoding='utf-8') as f:
                event = ' '.join(eventString.string[s:e].replace('`', '').split()[1:])
                
                print(f"Event.. {event}")
                f.write(event)

    except AttributeError:
        pass

        
bot.run(TOKEN)
