import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


class CustomBotClient(commands.Bot):

    async def on_ready(self):
        print(f'{self.user.name} has connected to Discord!')


def main():
    print("WeebBot is Loading!")
    intents = discord.Intents.default()
    intents.members = True

    bot = CustomBotClient('$')

# Load Cogs
    for folder in os.listdir("cogs"):
        if os.path.exists(os.path.join("cogs", folder, "cog.py")):
            bot.load_extension(f"cogs.{folder}.cog")

    bot.run(TOKEN)


if __name__ == '__main__':
    main()
