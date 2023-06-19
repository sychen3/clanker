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


async def main():
    client = SingleMessageSender('Hello, World', 999415862069039144)
    await client.send_message(botData.token)

if __name__ == "__main__":
    asyncio.run(main())
