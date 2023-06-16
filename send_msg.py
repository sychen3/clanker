import discord, botData
from discord.ext import commands

bot = commands.Bot(command_prefix = '.')

msg = "(you know that talk is cheap)"

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})\n------")

    channel = bot.get_channel(1014608064646746112)
    print(channel)

    if channel: await channel.send(msg)

    await bot.close()

bot.run(botData.token)
