from discord.ext import commands


class Greetings(commands.Cog, name='Greetings module'):

    def __init__(self, bot):
        self.bot = bot
        print("WeebBot.cogs.greetings.cog.py has been loaded!")


    @commands.command()
    async def heya(self, ctx: commands.Context):
        await ctx.send(f'O hai you go zai masu! {ctx.author.name}')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'{member.mention} has joined Kowaii Weebo Trash!')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('You have entered an invalid command D:')


def setup(bot):
    bot.add_cog(Greetings(bot))
    
