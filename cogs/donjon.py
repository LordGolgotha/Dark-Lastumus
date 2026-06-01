
import discord
from discord.ext import commands
from discord import app_commands
from liste_donjon import *
from enum_class import Classe
from ClasseButton import ClassButton
from gestion_levels import create_dj, get_dj_info

async def new_message(ctx, contenu):
        message = await ctx.edit(content=contenu)
        for emoji in emoji_list:
            await message.add_reaction(emoji)

class DonjonCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def construction_message(self,id):
        info_dj = get_dj_info(id)
        text = f"Donjon **{info_dj['donjon']}** modulé au niveau de statis **S{info_dj['statis']}**"
        if info_dj['date'] != "":
            text += f"le {info_dj['date']}"
        if info_dj['info'] != "":
            text += f"\n __**Info**__ : {info_dj['info']}"
        for j in info_dj['joueurs']:
            text += f"\n- {self.bot.get_user(j[0]).mention}: {str.capitalize(j[1])}"
        return text

    def dj_generique(self, id, ctx, donjon, statis, classe, date ="",info =""):
        id_message = id
        #TODO gérer le nombre de joueur
        nb_joueur = 6
        print(f"author id: {ctx.message.author.id}")
        create_dj(id_message,donjon,date,statis,ctx.message.author.id,classe,nb_joueur,info)
        contenu = self.construction_message(id_message)
        return contenu

    @commands.hybrid_command(
        description="Organiser un groupe de donjon lvl 20"
        )
    @app_commands.describe(donjon='Le donjon en question',
                        classe='La classe que vous comptez jouer',
                        statis= 'Le niveau de statis',
                        date= 'La date souhaitée dans le format JJ/MM/AAAA HH:MM heure française. Exemple: "24/02/1999 23:45"',
                        info = 'Info supplémentaire (exemple: besoin d\'une eniripsa, besoin d\'une personne expérimenté, 1/2/3 stele(s),  ...)')
    async def dj20(self, ctx: discord.context_managers,
                donjon : liste_donjon_20,
                statis : Literal[1,2,3,4,5,6,7,8,9,10],
                classe : Classe,
                date="",
                info = ""):
        id_dj = await ctx.send("test",view = ClassButton())
        contenu = self.dj_generique(id=id_dj,ctx=ctx,donjon=donjon,statis=statis,classe=classe.name,date=date,info=info)
        await new_message(ctx, contenu)

    @app_commands.describe(donjon='Le donjon en question',
                        classe='La classe que vous comptez jouer',
                        statis= 'Le niveau de statis',
                        date= 'La date souhaitée dans le format JJ/MM/AAAA HH:MM heure française. Exemple: "24/02/1999 23:45"',
                        info = 'Info supplémentaire (exemple: besoin d\'une eniripsa, besoin d\'une personne expérimenté, 1/2/3 stele(s),  ...)')
    @commands.command(
            description="Organiser un groupe de donjon lvl 35"
            )
    async def dj35(self, interaction: discord.Interaction,
                donjon : liste_donjon_35,
                statis : Literal[1,2,3,4,5,6,7,8,9,10],
                classe : Classe,
                date="",
                info = ""):
        contenu = self.dj_generique_i(interaction,donjon,statis,classe.name,date,info)
        await new_message(interaction, contenu)

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