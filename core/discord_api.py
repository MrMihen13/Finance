import discord

from discord.ext import commands

from django.conf import settings

# TODO Настроить запуск бота для Дискорда


class DiscordClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return print(f'Author is {message.author}')
        if message.content == 'ping':
            await message.channel.send('pong')
        if message.content.startswith('/help'):
            await message.channel.send(f'come help {message.author}')


# bot = commands.Bot(command_prefix='/')
#
# @bot.command()
# async def test(ctx, args):
#     await ctx.send(f'You wrote {args}')


# if __name__ == '__main__':
#     print('Bot is running')
#     bot.run('OTUzMzE4MjgyNzI1ODQyOTc0.YjC01g.lTZ0E7bSiNJm6_L9Erp-rF8lxXk')
#     print('Bot was run')
