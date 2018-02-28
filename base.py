# imports
import discord
from discord.ext import commands
import random
import inspect
import asyncio
import importlib
import math
import datetime
from datetime import datetime
now = datetime.now()

client = discord.Client()
description = '''Hello nerds!


There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='>', description=description)



@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    #print(bot.user.id)
    print('------')



@bot.command()

async def add(left : int, right : int):

    """Adds two numbers together."""

    await bot.say(left + right)



@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.command()
async def rate():
    """Rates things on a scale of 0-10!"""
    YourList = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    result = random.choice(YourList)
    await bot.say(result)

@bot.command()
async def thoughts():
    """Gives Persistent's thoughts on a matter."""
    Opinion = (':ok_hand:', '<:notokay:356482747411333160>', 'Hard pass.',
               '<:vomit:358447414706831370>', 'Excellent.',
               "TOO BAD, THIS ISN'T AN EXHIBIT", 'Away with that.', 'Cease.',
               'You need help... <:help:386336801608040449>',
               'Where is the merge stick...'
               )
    result = random.choice(Opinion)
    await bot.say(result)

@bot.command(description='Either or!')
async def choose(*choices : str):
    """Chooses between choices. Bot can pick 'or'."""
    await bot.say(random.choice(choices))

@bot.command()

async def joined(member : discord.Member):

    """Says when a member joined. @ the person after >joined"""

    await bot.say('{0.name} joined in {0.joined_at}'.format(member))



#@bot.group(pass_context=True)

#async def cool(ctx):

#    """Says if a user is cool. Format = put name after command"""

#    if ctx.invoked_subcommand is None:

#        await bot.say('No, {0.subcommand_passed} is a nerd'.format(ctx))



#@cool.command(name='bot')

#async def _bot():

#    """Is the bot cool?"""

#    await bot.say('Yes, the bot is amazing!')


@bot.command()
async def colour():

    """Says Persistent's favorite colour based on his mood."""

    Colours = ('blue', 'red', 'green', 'purple', 'orange', 'yellow', 'white', 'black', 'brown', 'neon blue', 'electric brown', 'royal purple',
             'puke green', 'highlighter yellow', 'liquor sign orange', 'Thailand district red', 'two leagues from Barcelona, Spain blue',
             'watermellon green', 'vomit chunky orange', "Reese's peanut butter brown", 'sandwich', 'pineapple pizza yellow', 'vintage red wine red',
             'a crusty blood red', 'an ugly designer yellow', 'a designer blue', 'a designer black', 'a designer puke green', 'a designer purple', 'a designer pink',
             'a designer red', 'a designer green', 'a designer orange', 'a designer white', 'lasagna white', 'undercooked brown', 'popcorn magenta', 'a raw red',
             'vegan red', 'an overcooked cactus green', 'poopy brown', 'deep fried green', 'deep fried brown', 'deep fried purple', 'deep friend yellow','a disgustingly pink, pink')

    Colour = random.choice(Colours)
    Coloor = ('My favourite colour right now is... ')
    paste = (Coloor + Colour)
    await bot.say(paste)


#@bot.command()
#async def revive():
    
#    """GET THE BIOMASS YOU CHEMIST SHITS!"""

#    BiomassGot = 'Biomass acquired Chief Medical Officer! Stop robusting the HoS for powergaming the cryo cells already!'
    
#    await bot.say(BiomassGot)



@bot.command()
async def menu():
    """Gives you a randomized selection of food."""

    adjectives = ('awful', 'burnt', 'well-done', 'excellent', 'over-salted', 'bland',
                  'spicy', 'undercooked', 'yummy', 'satisfying', 'exciting',
                  'disgusting')
    mains = ('steak', 'lamb shank', 'pork loin', 'spinach & ricotta canneloni', 'shit sandwich',
             'lasagna', 'mediterranean chicken', 'veggie burger',
             'cheese tortellini', 'chicken pesto pasta',
             'chilli', 'ribs', 'lemon pepper tuna')
    sweets = ('cookie', 'mars bar', 'skittles', 'smokey bacon crisps',
              'popcorn', 'dried prunes', 'crackers', 'cheese curls',
              'granola bar', 'pound cake', 'nuts')
    drinks = ('water', 'flavoured water', 'salt water', 'bleach scented soda', 'soda water', 'orangeade', 'cola',
              'fruit juice', 'cherryade', 'appleade', 'lemonade', 'milkshake',
              'smoothie')

    adj = random.choice(adjectives)
    main = random.choice(mains)
    sweet = random.choice(sweets)
    drink = random.choice(drinks)

    rationsresult = 'Your order contain ' + adj +' '+ main +', '+ sweet +' and '+ drink + '. Top nosh!'

    await bot.say(rationsresult)

@bot.command()
async def poly():
    """Parrots past sayings!"""

    meme = ('Cody: JustWerks™', 'Cody: When in doubt, screech it out.',
                'Cody: I\'ll get around to it soon™', 'Cody: Brb forgot the )',
                 'Cody: It\'d sure be nice if we had a >status command :^)',
            'Brawler: Eventually™', 'Brawler: oh', 'Eyes: I can just threaten to ban people who dont compliment me.',
                 'Eyes: what kind of ss13 player doesn\'t know all about questionably ethical psychological experiments',
                 '''Eyes: robot tits are now heresy
any future mention of robo tits is a **DING DONG BANNU**''', '''Eyes: you know how ancient cities are built up upon the old foundations
atmos is ss13\'s neolithic shithouse''', 'Ukukuku: A mexican an italian chef and a greytide walk into a brig',
            'i\'ve been curing kiddos of their discord social disorders for years; thats why they call me the kiddo wisperer'
                 )
    memeresult = random.choice(meme)
    await bot.say(memeresult)


@bot.command()
async def movie():
    """Pastes movie information if relevant."""
    movie = 'http://www.montypython.net/grailmm2.php'
    title = 'Monty Python and the Holy Grail - PAUSED AT SCENE 14 -'
    await bot.say(movie)
    await bot.say(title)


# TESTING

@bot.command()
#@client.event()
async def re(ctx):
    if(ctx == 're' and time <= 1800):
        return(False)
    if(ctx == 're' and time >= 1800):
        return(True)
    if(False):
        await bot.say("'tis before 6 you nerd! <:harm:392794835666599936>")

@bot.command()
async def repeat(times: int, content: 'repeating...'):
    """You're all terrible people."""
    for i in range(times):
        await bot.send(content)


bot.run('token')
