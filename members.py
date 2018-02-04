import discord
from discord.ext import commands

class Member():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def joined(member : discord.Member):
        """Finds when a member joined."""
        await self.bot.say('{0.name} joined at {0.joined_at}'.format(member))

def setup(bot):
    bot.add_cog(Member(bot))
