import discord


class Greetings(discord.ext.commands.Cog, name='Greetings module'):
    print("WeebBot.cogs.greetings has been loaded!")

    def __init__(self, bot):
        self.bot = bot

    @discord.ext.commands.command(name="hey")
    async def adhoc_play(self, ctx):
        await ctx.send(f'O hai you go zai masu! {ctx.author.name}')

    @discord.ext.commands.Cog.listeneer()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'{member.mention} has joined Kowaii Weebo Trash!')

    @discord.ext.commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.CommandNotFound):
            await ctx.send('You have entered an invalid command D:')
