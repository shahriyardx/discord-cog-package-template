from discord.ext import commands


class CogName(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.send("The test command")

    def cog_unload(self):
        # Do some stuff if needed
        pass
