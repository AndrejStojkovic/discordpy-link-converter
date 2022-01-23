import discord

token = 'insert token'

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as: {0}'.format(self.user))

    async def on_message(self, message):
        if 'https://media.discordapp.net' in message.content:
            msg = message.content.replace('https://media.discordapp.net', 'https://cdn.discordapp.com')
            await message.channel.send(msg)
            await message.delete()

client = MyClient()
client.run(token, bot=True)
