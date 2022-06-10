import discord
from discord.ext import commands

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='clanker ', intents=intents)

client = MyClient(intents=intents)

@bot.command()
async def ping(ctx): await ctx.send('pong')
async def salute(ctx): await ctx.send('roger roger')


bot.run('token')
client = MyClient()
client.run('token')