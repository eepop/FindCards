import discord
from discord.ext import commands

	
class FindCards:
    """VF Cog that does a Scryfall search"""

    def __init__(self, bot):
        self.bot = bot

	
    @commands.command()
    async def mycom(self):
        """This does stuff!"""

        await self.bot.say("Yay!")	
		

def setup(bot):
		bot.add_cog(FindCards(bot))