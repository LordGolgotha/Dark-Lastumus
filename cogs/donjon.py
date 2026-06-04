import discord
from discord.ext import commands
from discord import app_commands
from liste_donjon import *
from ClasseButton import ClassButton
from gestion_levels import create_dj
from gestion_message import *

MAX_LEVEL = 245

class DonjonCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        for level in range(20,MAX_LEVEL+1,15):
            self._add_dj_command(level)

    def dj_generique(self, id, ctx, donjon, stasis, date ="",info =""):
        id_message = id
        #TODO gérer le nombre de joueur
        nb_joueur = 6
        print(f"author id: {ctx.message.author.id}")
        create_dj(id_message,donjon,date,stasis,nb_joueur,info)
        contenu, nb_joueur = construction_message(self.bot, id_message)
        return contenu, nb_joueur

    def _add_dj_command(self, level):
        donjon_level = donjon_level_map[level]
        bot = self.bot
        dj_generique = self.dj_generique

        @commands.hybrid_command(
            name=f"dj{level}",
            description=f"Organiser un groupe de donjon lvl {level}"
        )
        @app_commands.describe(
            donjon='Le donjon en question',
            stasis='Le niveau de stasis',
            date='La date souhaitée dans le format JJ/MM/AAAA HH:MM heure française. Exemple: "24/02/1999 23:45"',
            info='Info supplémentaire (exemple: besoin d\'une eniripsa, besoin d\'une personne expérimenté, 1/2/3 stele(s),  ...)'
        )
        async def callback(ctx: discord.context_managers, donjon: donjon_level, stasis: Literal[1,2,3,4,5,6,7,8,9,10], date="", info=""): # type: ignore
            interaction_dj = await ctx.send("Création de votre donjon, veuillez patientez...", view=ClassButton(bot))
            contenu, nb_joueur = dj_generique(id=interaction_dj.id, ctx=ctx, donjon=donjon, stasis=stasis, date=date, info=info)
            await modif_message(interaction_dj, contenu, nb_joueur, bot)

        self.bot.add_command(callback)

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            sync = await self.bot.tree.sync()
            print(f"{len(sync)} commande chargé")
        except Exception as e:
            print(e)

async def setup(bot):
    await bot.add_cog(DonjonCog(bot))   