import discord
from dotenv import load_dotenv
from discord.ext import commands
import os


load_dotenv()

token = token = os.getenv('DISCORD_TOKEN')

class DarkLastumus(commands.Bot):
    async def setup_hook(self):
        await self.load_extension(f'cogs.donjon')

intents = discord.Intents.all()
bot = DarkLastumus(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    try:
        sync = await bot.tree.sync()
        print(f"{len(sync)} commande chargé")
    except Exception as e:
        print(e)

bot.run(token=token)