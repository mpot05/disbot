import discord
from discord.ext import commands

import random
import datetime

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

# initialize
@bot.event
async def on_ready():
    print(f"Loggin in as {bot.user}")
    print("Microbit detected? " + "No" if ser == None else "Yes")
    print("--------")
    await bot.change_presence(activity=discord.CustomActivity(name='Glooping'))
    await bot.change_presence(activity=discord.Game("Team Defense Fort 2"))

@bot.command(help="wildly innacurate")
async def ping(ctx: commands.Context):
    # get timestamps
    msg_time = ctx.message.created_at
    cur_time = datetime.datetime.now(tz=datetime.timezone.utc)

    # ping time
    ping_time = cur_time - msg_time

    # turn ping time to milis and send it
    await ctx.reply("🏓 pong - %gms" % (ping_time.total_seconds() * 1000))

# math ops
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

# microbit stuff
@bot.command(help="beeps")
async def beep(ctx):
    # make sure that the microbit is actually connected (ser != None)
    if ser == None:
        await ctx.send("no microbit connected.")
        return

    ser.write(b'BEEP.') # implement this on the microbit later

    await ctx.send("serial code sent.")

# silly stuff
@bot.command(help="replies with a message")
async def reply(ctx, *message):
    st = ""

    # add everything in the message
    for i in message:
        st += i + " "

    await ctx.reply(st)

# literally just reply without replying
@bot.command(help="Have the bot say something (use at own risk)")
async def say(ctx, *message):
    st = ""

    for i in message:
        st += i + " "
    
    await ctx.send(st)

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

config = dotenv_values(".env")
bot.run(config.get("TOKEN"))
