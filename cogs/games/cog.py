from discord.ext import commands


class Games(commands.Cog, name="Games Cog"):
    """Simple Games Cog"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print("WeebBot.cogs.games.cog.py has been loaded!")


def setup(bot: commands.Bot):
    bot.add_cog(Games(bot))
