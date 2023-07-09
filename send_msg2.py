import asyncio, discord, sys, botData

class SingleMessageSender(discord.Client):
    def __init__(self, message, channel_id, reply_id):
        # Intents passed don't really matter as we don't connect to the gateway
        super().__init__(intents=discord.Intents.all())

        self.message = message
        self.channel_id = channel_id
        self.reply_id = reply_id

    async def send_message(self, token):
        await self.login(token)  # Ensure the internal HTTP client is initialized with a token

        channel = await self.fetch_channel(self.channel_id)
        warning = f"""\
replyto: {self.reply_id}
channel: {channel.name}
message text:
{self.message}\n
proceed? [y/n]\n"""
        if input(warning) != 'y':
            await self.close()
            return
        
        if self.reply_id:
            try:
                msg = await channel.fetch_message(self.reply_id)
                await msg.reply(self.message)
            except:
                print("invalid message-channel combination")
        else:
            await channel.send(self.message)

        await self.close()  # Close the HTTP client again

def parse_args(argv):
    argv.pop(0)
    channel, msg, reply = None, None, None
    while argv:
        curr_arg = argv.pop(0)
        # stops the count before we try to parse a missing arg
        if curr_arg == "-h":
            print("usage: python send_msg2.py [-m <message> | -c <channel] [-r <reply_id>]")
            return 2

        elif not argv: return (None, None, None)
        elif curr_arg == "-c":
            channel = get_channel(argv.pop(0))
        elif curr_arg == "-m":
            msg = argv.pop(0)
        elif curr_arg == "-r":
            reply = argv.pop(0)
    return (channel, msg, reply)

def get_channel(path):
    if path == "channel2": return 999415862069039144
    elif path == "channel5": return 1011851229716037722
    elif path.isdigit():
        return path
    else:
        print(f"could not retrieve channel from {path}")
        return None
    # TODO: add the rest of the path parser here, and then document
    # how path input should work

async def main():
    args = parse_args(sys.argv)
    if args == 2: return
    (channel, msg, reply) = args
    client = SingleMessageSender(msg, channel, reply)
    await client.send_message(botData.token)

if __name__ == "__main__":
    asyncio.run(main())
