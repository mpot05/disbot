import discord
from discord.ext import commands
import random
from dotenv import load_dotenv
from dotenv import dotenv_values
import serial

# serial port for communication with microbit
ser = serial.Serial("COM14", 9600)

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
    # a's
    a = "A" * random.randint(1,999)

    # h's
    h = "H" * random.randint(1,999)

    # generate the message in varying degress of italicized and bold.
    walls_norm = "THE NOISES IN THE WALLS " * random.randint(1, 5)
    walls_ital = "*THE NOISES IN THE WALLS* " * random.randint(0, 5)
    walls_bold = "**THE NOISES IN THE WALLS** " * random.randint(0, 5)
    walls_both = "***THE NOISES IN THE WALLS*** " * random.randint(0, 5)

    if len(a) + len(h) + len(". ") + len(walls_norm) + len(walls_ital) + len(walls_bold) + len(walls_both) >= 2000:
        a = a[0:len(a)//2]
        h = h[0:len(h)//2]

    # send all of it! this is awesome
    await ctx.send(a + h + ". " + walls_norm + walls_ital + walls_bold + walls_both)

async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.reply('Hello!', mention_author=True)

config = dotenv_values(".env")
bot.run(config.get("TOKEN"))
