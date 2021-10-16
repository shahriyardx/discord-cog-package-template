from .cog import CogName


def setup(bot):
    bot.add_cog(CogName(bot))


__version__ = "0.0.1"
