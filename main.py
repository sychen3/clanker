import discord, random, h
from discord.ext import commands
from botData import *

intents = discord.Intents.all()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        author, content = message.author, message.content
        channel, guild = message.channel, message.guild
        print(author, content)
        # we do not want the bot to reply to itself
        if author.id == self.user.id:
            return

        if content == 'ping':
            await message.reply('pong')
        
        if '<:dittosalute:989635895978233986>' in content:
            await message.reply('<:dittosalute:989635895978233986> roger roger')
        
        if 'fronks2' in content:
            await message.reply('<:fronks2:983138681294573641>')

        if content.startswith('!hello'):
            await message.reply('Hello!', mention_author=True)
        
        lowerContent = content.lower()
        for word in bannedWords:
            if word in lowerContent:
                reason = f'banned word: "{word}"'
                await h.kick(author, guild, reason)
        
    # activity ban checker
    async def on_member_update(self, before, after):
        activity = after.activity
        if activity != None:
            for activity in after.activities:
                if (activity.type == discord.ActivityType.playing and
                    activity.name in bannedActivities):
                    user, server = after, after.guild
                    reason = f'banned activity: "{activity.name}"'
                    await h.kick(user, server, reason)

client = MyClient(intents=intents)
client.run(token)


#####################################################################

# COMMANDS

#####################################################################


description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

bot = commands.Bot(command_prefix='!',
                   description=description,
                   intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def ban(ctx, member: discord.abc.User):
    guild = discord.Guild
    await guild.ban(member)

@bot.command()
async def kick(ctx, user: discord.abc.User):
    guild = discord.Guild
    await guild.kick(user)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def ping(ctx):
    await ctx.send('fuck pong krell')

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(
        f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.group()
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')
      

@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

# bot.run(token)