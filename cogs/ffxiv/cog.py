from discord.ext import commands


class Ffxiv(commands.Cog, name="FFXIV"):
    """All things Final Fantasy XIV Online free trial up to level 60, including the award winning
    Heavensward expansion!..."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print("WeebBot.cogs.ffxiv.cog.py has been loaded!")

    @commands.command()
    async def whoami(self, ctx: commands.Context):
        pass


def setup(bot: commands.Bot):
    bot.add_cog(Ffxiv(bot))
