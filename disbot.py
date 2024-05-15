import discord
from discord.ext import commands

import random

from dotenv import load_dotenv
from dotenv import dotenv_values

import serial

import serial_utils

# serial port constants (sourced from link 2 in links.md)
MICROBIT_PID = 516
MICROBIT_VID = 3368
BAUD = 115200

# serial port of the microbit. can be "None" if no port was found
ser = serial_utils.find_port(MICROBIT_PID, MICROBIT_VID, BAUD)

description = '''
    Merry fitness
'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='😀', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f"Loggin in as {bot.user}")
    print("Microbit detected? " + "No" if ser == None else "Yes")
    print("--------")
    await bot.change_presence(activity=discord.CustomActivity(name='Glooping'))
    await bot.change_presence(activity=discord.Game("Team Defense Fort 2"))

@bot.command(help="adds two numbers")
async def add(ctx, left: float, right: float):
    await ctx.send("%g" % (left + right))

@bot.command(help="subtracts two numbers")
async def sub(ctx, left: float, right: float):
    await ctx.send("%g" % (left - right))

@bot.command(help="multiplies two numbers")
async def mult(ctx, left: float, right: float):
    await ctx.send("%g" % (left * right))

@bot.command(help="divides two numbers")
async def div(ctx, left: float, right: float):
    await ctx.send("%g" % (left / right))

@bot.command(help="beeps")
async def beep(ctx):
    # make sure that the microbit is actually connected (ser != None)
    if ser == None:
        await ctx.send("no microbit connected.")
        return

    ser.write(b'BEEP.') # implement this on the microbit later

    await ctx.send("serial code sent.")

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

# this is currently doing nothing
async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.reply('Hello!', mention_author=True)

config = dotenv_values(".env")
bot.run(config.get("TOKEN"))
