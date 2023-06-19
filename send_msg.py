import discord, sys, botData
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.',intents=intents)

def parse_args(argv):
    argv.pop(0)
    channel, msg, reply = None, None, None
    while argv:
        curr_arg = argv.pop(0)
        # stops the count before we try to parse a missing arg
        if not argv: return (None, None, None)
        elif curr_arg == "-c":
            channel = get_channel(argv.pop(0))
        elif curr_arg == "-m":
            msg = argv.pop(0)
        elif curr_arg == "-r":
            reply = find_msg(argv.pop(0))
    return (channel, msg, reply)

def get_channel(path):
    return 1014608064646746112 if path == "channel5" else 999415862069039144
    if path.isdigit():
        return bot.get_channel(int(path))
    else:
        separator_index = path.find('/')
        serverName = path[:separator_index]
        if serverName not in serverMap:
            print(f"could not find server {server}")
            return None
        guild = bot.get_guild(serverMap[serverName])
        channelName = path[separator_index + 1:]
        for channel in guild.channels:
            if channel.name == channelName:
                return channel

def find_msg(id):
    return None

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})\n------")

    print((channel, msg))
    await channel.send(msg)
    await bot.close()
    exit(0)

(channel, msg, reply) = None, None, None
def main():
    (channel, msg, reply) = parse_args(sys.argv)
    print((channel, msg, reply))

    if None in (channel, msg): return
    bot.run(botData.token)

if __name__ == "__main__":
    main()
