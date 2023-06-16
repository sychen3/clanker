import discord, random, time, string
from discord.ext import commands
# from twiceDiscog import *
from ../clanker-current/botData import token

description = "twice fan bot"
loggers = "logger2.txt"

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')
    game = discord.Game("I'm Gonna Be A Star")
    listening = 0
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
    print(m.activities)
    await respond(m.content, m)

async def respond(content, m):
    for c in string.punctuation: content = content.replace(c, "")
    for song in songs:
        parsedSong = song
        for c in string.punctuation: parsedSong = parsedSong.replace(c, "")
        if len(parsedSong) < 3:
            if parsedSong in content:
                await m.reply(f"omg {song} like from twice")
                return
        else:
            parsedSong = song.replace(" ", "").lower()
            if parsedSong in content.lower():
                await m.reply(f"omg {song} like from twice")
                return
    M = list(members); random.shuffle(M)
    for member in M:
        if member in content:
            if member == 'jihyo': member = 'god ' + member
            await m.reply(f"omg {member} like from twice")
            return
    if 'twice' in content:
        await m.reply("https://twitter.com/i/status/1534547498210979841")
        return

client.run(token)
