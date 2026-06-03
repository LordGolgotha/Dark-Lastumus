from discord.ext import commands
import discord

class TrollCog(commands.Cog):
    def __init__(self,bot):
        super().__init__()
        self.bot = bot

    @commands.hybrid_command(description="Bonjour?")
    async def bonjour(self, ctx):
        await ctx.send(f"Bonsoir c'est moi Lastumus, je déteste les péruches, le hockey et ma soeur. Par contre j'adore les Tacos!")

async def setup(bot):
    await bot.add_cog(TrollCog(bot))