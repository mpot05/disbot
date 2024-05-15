import discord
from discord.ext import commands
import random
from dotenv import load_dotenv
from dotenv import dotenv_values

description = '''
    Merry fitness
'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='😀', description=description, intents=intents)

@bot.event
async def on_ready():
    print("Loggin in as {bot.user}")
    print("--------")
    await bot.change_presence(activity=discord.CustomActivity(name='Glooping'))
    await bot.change_presence(activity=discord.Game("Team Defense Fort 2"))

@bot.command()
async def add(ctx, left: float, right: float):
    await ctx.send("%g" % (left + right))

@bot.command()
async def sub(ctx, left: float, right: float):
    await ctx.send("%g" % (left - right))

@bot.command()
async def mult(ctx, left: float, right: float):
    await ctx.send("%g" % (left * right))

@bot.command()
async def div(ctx, left: float, right: float):
    await ctx.send("%g" % (left / right))

@bot.command()
async def fuck(ctx):
     h = "H" * random.randint(1,999)
     amount = random.randint(4, 999) # 4 so that they all show up
     amount /= 4 # four evenly-arranged sections
     await ctx.send("A" + h + ". THE NOISES IN THE WALLS")

async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.reply('Hello!', mention_author=True)

config = dotenv_values(".env")
bot.run(config.get("TOKEN"))