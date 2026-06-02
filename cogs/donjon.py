
import discord
from discord.ext import commands
from discord import app_commands
from liste_donjon import *
from enum_class import Classe
from ClasseButton import ClassButton
from gestion_levels import create_dj, get_dj_info
from gestion_message import *

class DonjonCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def dj_generique(self, id, ctx, donjon, stasis, classe, date ="",info =""):
        id_message = id
        #TODO gérer le nombre de joueur
        nb_joueur = 6
        print(f"author id: {ctx.message.author.id}")
        create_dj(id_message,donjon,date,stasis,ctx.message.author.id,classe,nb_joueur,info)
        contenu, nb_joueur = construction_message(self.bot, id_message)
        return contenu, nb_joueur

    @commands.hybrid_command(
        description="Organiser un groupe de donjon lvl 20"
        )
    @app_commands.describe(donjon='Le donjon en question',
                        classe='La classe que vous comptez jouer',
                        stasis= 'Le niveau de stasis',
                        date= 'La date souhaitée dans le format JJ/MM/AAAA HH:MM heure française. Exemple: "24/02/1999 23:45"',
                        info = 'Info supplémentaire (exemple: besoin d\'une eniripsa, besoin d\'une personne expérimenté, 1/2/3 stele(s),  ...)')
    async def dj20(self, ctx: discord.context_managers,
                donjon : liste_donjon_20,
                stasis : Literal[1,2,3,4,5,6,7,8,9,10],
                classe : Classe,
                date="",
                info = ""):
        interaction_dj = await ctx.send("Création de votre donjon, veuillez patientez...",view = ClassButton(self.bot))
        contenu, nb_joueur = self.dj_generique(id=interaction_dj.id,ctx=ctx,donjon=donjon,stasis=stasis,classe=classe.name,date=date,info=info)
        await modif_message(interaction_dj, contenu, nb_joueur, self.bot)

    @app_commands.describe(donjon='Le donjon en question',
                        classe='La classe que vous comptez jouer',
                        stasis= 'Le niveau de stasis',
                        date= 'La date souhaitée dans le format JJ/MM/AAAA HH:MM heure française. Exemple: "24/02/1999 23:45"',
                        info = 'Info supplémentaire (exemple: besoin d\'une eniripsa, besoin d\'une personne expérimenté, 1/2/3 stele(s),  ...)')
    @commands.command(
            description="Organiser un groupe de donjon lvl 35"
            )
    async def dj35(self, interaction: discord.Interaction,
                donjon : liste_donjon_35,
                stasis : Literal[1,2,3,4,5,6,7,8,9,10],
                classe : Classe,
                date="",
                info = ""):
        contenu = self.dj_generique_i(interaction,donjon,stasis,classe.name,date,info)
        await modif_message(interaction, contenu)

    @commands.command
    async def ping(self,interact : discord.Interaction):
         await interact.context.send(f'pong')

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            sync = await self.bot.tree.sync()
            print(f"{len(sync)} commande chargé")
        except Exception as e:
            print(e)

async def setup(bot):
    await bot.add_cog(DonjonCog(bot))   