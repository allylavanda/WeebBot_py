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

    @commands.command()
    async def iam(self, ctx: commands.Context):
        pass

    @commands.command()
    async def bestmmo(self, ctx: commands.Context):
        await ctx.send("Final Fantasy XIV has a free trial up to level 60 which includes the award winning "
                       "Heavensward expansion; therefore making it the superior MMORPG to date.")


def setup(bot: commands.Bot):
    bot.add_cog(Ffxiv(bot))
