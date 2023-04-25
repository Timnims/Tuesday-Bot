import discord
import time
import random
from datetime import datetime
from discord.ext import commands
import pytz

start = time.time()

time_zone = pytz.timezone('US/Pacific')
bot = commands.Bot(command_prefix='~')
bot.remove_command('help')


@bot.event
async def on_ready():
    print(bot.user, 'Is Ready.')
    end = time.time()
    totalTime = end - start
    print(f'It took {totalTime:.2f} seconds!')


@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title='Is it Tuesday?',
        description='Find out if its tuesday by doing the command ~tuesday\n'
                    'Learn a new tuesday fact by doing ~fact!',
        colour=discord.Colour.green()
    )

    await ctx.send(embed=embed)


@bot.command()
async def tuesday(ctx):
    now = datetime.now(time_zone)
    if now.strftime("%A") == "Tuesday":
        await ctx.send('It is Tuesday! :D')
    else:
        await ctx.send('It is not Tuesday :(')


@bot.command()
async def fact(ctx):
    now = datetime.now(time_zone)
    if now.strftime("%A") == "Tuesday":
        with open('facts.txt', 'r', encoding="utf8") as f:
            lines = f.readlines()
            tuesday_fact = random.choice(lines)

            await ctx.send(f'{str(tuesday_fact)}')
    else:
        await ctx.send('It is not Tuesday :(')




bot.run('[BOT_TOKEN]')
