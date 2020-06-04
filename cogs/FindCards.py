import discord
from discord.ext import commands

	
class FindCards(commands.Cog):
    """VF Cog that does a Scryfall search"""

    def __init__(self, bot):
        self.bot = bot

	@commands.Cog.listener()
	aync def on_ready(self):
        print("FindCards Cog Ready!")
	
    @commands.command()
    async def mycom(self):
        """This does stuff!"""
        await self.bot.say("Yay!")	
		
	@commands.command(pass_context=True)
    async def on_message(self, message):
        """Build a Scryfall Query"""
		text = message
			
		if text.find("with text ") > 0 :
			(colortext,withtext) = text.split("with text ",1)
		else:
			colortext = text
			withtext = ""
		
		
		if colortext.find("or") > 0 :
			colors = "color%3E%3D"
		elsif colortext.find("only") > 0 :
			colors = "color%3C%3D"
		else:
			colors = "color%3D"
		
		if colortext.find("red") > 0 : 
			colors = colors + 'R'			
		
		if colortext.find("black") > 0 :
			colors = colors + 'B'	
			
		if colortext.find("blue") > 0 :
			colors = colors + 'U'	
			
		if colortext.find("white") > 0 :
			colors = colors + 'W'		
			
		if colortext.find("green") > 0 :
			colors = colors + 'G'	
			
		theURL = "https://scryfall.com/search?as=grid&order=name&q=legal%3Amodern"
		
		if len(colors) > 6:
			theURL + '+' + colors			
		
		if len(withtext) > 0:
			theURL + '+%28oracle%3A' + withtext.replace(' ','+oracle%3A') + '%29'
		
		self.bot.say(theURL)		

def setup(bot):
		bot.add_cog(FindCards(bot))