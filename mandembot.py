import os
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user.name}')

@bot.command(name='wys?', help="Responds with a random mandem quote (what are you saying?)")
async def what_you_saying(ctx):
    mandem_quotes = [
        'Mans are blessed styll',
        'You already know, talking to bare tings',
        'Tryna ball up, wys?',
        'Don\'t worry Cuzzo, keep it moving.',
        'Pining your ting',
        'Nize dat Bucket',
        'Ask your mom dukes',
        'Bout to chef a man, tryna reach?'
    ]

    response = random.choice(mandem_quotes)
    await ctx.send(response)

@bot.command(name='Blessed?', help="Responds with blessed phrases.")
async def you_blessed(ctx):
    mandem_quotes = [
        'I\'m blessed still',
        'Ye ye, good looks my yute',
        'Yea, unlike your hair line',
        'I\'m blessed...if you run your kicks cuzzo',
        'Of course, you don\'t see the ice im wearing right now?',
        'Do I know you? Keep it moving waste yute'
    ]

    response = random.choice(mandem_quotes)
    await ctx.send(response)

@bot.command(name='CatchIt?', help="Responds who is getting hands")
async def whos_catching_it(ctx):
    
    while True:
        user = random.choice(ctx.channel.guild.members)

        if(not user.bot):
            break

    mandem_quotes = [
        f'Lowkey might have to clap {user.name}',
        f'{user.name} might have to run me some money styll',
        f'Might take those kicks from {user.name}'
    ]

    response = random.choice(mandem_quotes)
    await ctx.send(response)

@bot.command(name='Scrap', help="Sees who would win in a fight. Needs a min of 2 members mentioned")
async def scrap(ctx, memberOne: discord.Member, memberTwo: discord.Member, *args: discord.Member):

    memberList = [memberOne, memberTwo, *args]
    print(memberList)
    winner = random.choice(memberList)
    response = '{} wins the scrap still'.format(winner.mention)

    await ctx.send(response)

@bot.event
async def on_command_error(ctx, error):
    if(isinstance(error,commands.MissingRequiredArgument)):
        print(error)
        await ctx.send('Yo, you need to include at least 2 people. Try again.')

bot.run(TOKEN)