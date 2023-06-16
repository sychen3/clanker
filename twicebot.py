import discord, random, time, string
from discord.ext import commands
# from twiceDiscog import *
from botData import token

description = "twice fan bot"
loggers = "logger2.txt"

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')
    game = discord.Game("God")
    await client.change_presence(status=discord.Status.idle, activity=game)

@client.event
async def on_message(m):
    reportFormat = """text: "%s"
    attachments: %s
    channel: %s
    channel id: %s
    sender: %s
    message id: %s
    time: %s"""
    
    report = reportFormat % (m.content, m.attachments, m.channel, m.channel.id,
                           m.author, m.id, time.asctime())
    print(report)
    with open(loggers, 'a') as f:
        f.write(report + '\n')
    if m.author == client.user and "sam" not in m.content: return
    # guild = m.channel.guild
    print(m.author.activities)
    await respond(m.content, m)

async def respond(content, m):
    if 'twice' in content.lower():
        await m.reply("https://twitter.com/i/status/1534547498210979841")
        return

client.run(token)
