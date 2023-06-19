import asyncio, discord, sys, botData

class SingleMessageSender(discord.Client):
    def __init__(self, message, channel_id):
        # Intents passed don't really matter as we don't connect to the gateway
        super().__init__(intents=discord.Intents.default())

        self.message = message
        self.channel_id = channel_id

    async def send_message(self, token):
        await self.login(token)  # Ensure the internal HTTP client is initialized with a token

        channel = await self.fetch_channel(self.channel_id)
        await channel.send(self.message)

        await self.close()  # Close the HTTP client again

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
    return 1011851229716037722 if path == "channel5" else 999415862069039144
    # TODO: add the rest of the path parser here, and then document
    # how path input should work

def find_msg(id):
    return None

async def main():
    (channel, msg, reply) = parse_args(sys.argv)
    client = SingleMessageSender(msg, channel)
    await client.send_message(botData.token)

if __name__ == "__main__":
    asyncio.run(main())
