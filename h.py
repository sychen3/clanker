import discord, random

async def ban(user, server, reason=None, erase_msg=0):
    channel = server.system_channel
    try:
        await server.ban(user, reason=reason, delete_message_days=erase_msg)
        bantext = f'{user} was banned. reason `{reason}`'
        await channel.send(bantext)
        print(bantext)
    except:
        failban = f'could not ban {user}'
        await channel.send(failban)
        print(failban)

async def kick(user, server, reason=None):
    channel = server.system_channel
    try:
        await server.kick(user, reason=reason)
        bantext = f'{user} was kicked. reason `{reason}`'
        await channel.send(bantext)
        print(bantext)
    except:
        failban = f'could not kick {user}'
        await channel.send(failban)
        print(failban)