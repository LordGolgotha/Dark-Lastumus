import discord
from dotenv import load_dotenv
from discord.ext import commands
import os


load_dotenv()

token = token = os.getenv('DISCORD_TOKEN')

class DarkLastumus(commands.Bot):
    async def setup_hook(self):
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await self.load_extension(f'cogs.{filename[:-3]}')
                print(f'Fichier {filename[:-3]} chargé')

intents = discord.Intents.all()
bot = DarkLastumus(command_prefix='!', intents=intents)


bot.run(token=token)