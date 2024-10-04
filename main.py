from settings import settings
import discord
from logic import *
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logge in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def bye(ctx):
    await ctx.send(f'Nooo!! Bye then, {ctx.message.author}!')

@bot.command()
async def generate(ctx, count_gen = 10):
    await ctx.send(pass_gen(count_gen))

@bot.command()
async def smile(ctx):
    await ctx.send(gen_emodji())

@bot.command()
async def flipcoin(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def guess(ctx):
    await ctx.send('Guess a number between 1 and 10.')
    def is_correct(m):
        return int(m.content)

    answer = random.randint(1, 10)

    try:
        guess = await bot.wait_for('message', check=is_correct, timeout=10.0)
    except asyncio.TimeoutError:
        return await ctx.send(f'Sorry, you took too long it was {answer}.')

    if int(guess.content) == answer:
        await ctx.send('You are right!')
    else:
        await ctx.send(f'Oops. It is actually {answer}.')


bot.run(settings["TOKEN"])

