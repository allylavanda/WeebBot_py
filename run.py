import discord
from clients.custom_bot_client import TOKEN
from clients.custom_bot_client import CustomBotClient
from cogs.greetings import Greetings


def main():
    intents = discord.Intents.default()
    intents.members = True

    bot = CustomBotClient(
        command_prefix='$',
        intents=intents
    )
    bot.add_cog(Greetings(bot))

    bot.run(TOKEN)


if __name__ == '__main__':
    main()
