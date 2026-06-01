
import discord
from discord.ext import commands
from discord import app_commands
from liste_donjon import *
from enum_class import Classe

from gestion_levels import create_dj, get_dj_info

class TestButton(discord.ui.View):

    @discord.ui.button(style=discord.ButtonStyle.blurple,emoji=emoji_list[0])
    async def button_osa(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("eni réussi")

    @discord.ui.button(style=discord.ButtonStyle.red,emoji=emoji_list[1])
    async def button_enu(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("ougi réussi")

    @discord.ui.button(style=discord.ButtonStyle.gray,emoji=emoji_list[2])
    async def button_sram(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("ougi réussi")

    @discord.ui.button(style=discord.ButtonStyle.green,emoji=emoji_list[3])
    async def button_xelor(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("ougi réussi")

    @discord.ui.button(style=discord.ButtonStyle.blurple,emoji=emoji_list[4])
    async def button_eca(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("ougi réussi")

    @discord.ui.button(style=discord.ButtonStyle.red,emoji=emoji_list[5])
    async def button_eni(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("ougi réussi")

    @discord.ui.button(style=discord.ButtonStyle.gray,emoji=emoji_list[6])
    async def button_iop(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("ougi réussi")

    @discord.ui.button(style=discord.ButtonStyle.green,emoji=emoji_list[7])
    async def button_cra(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("ougi réussi")

    @discord.ui.button(style=discord.ButtonStyle.blurple,emoji=emoji_list[8])
    async def button_sadi(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("ougi réussi")

    @discord.ui.button(style=discord.ButtonStyle.red,emoji=emoji_list[9])
    async def button_sacri(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("ougi réussi")

    @discord.ui.button(style=discord.ButtonStyle.gray,emoji=emoji_list[10])
    async def button_panda(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("ougi réussi")

    @discord.ui.button(style=discord.ButtonStyle.green,emoji=emoji_list[11])
    async def button_roub(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("ougi réussi")

    @discord.ui.button(style=discord.ButtonStyle.blurple,emoji=emoji_list[12])
    async def button_zobal(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("ougi réussi")

    @discord.ui.button(style=discord.ButtonStyle.red,emoji=emoji_list[13])
    async def button_ougi(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("ougi réussi")

    @discord.ui.button(style=discord.ButtonStyle.gray,emoji=emoji_list[14])
    async def button_steamer(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("ougi réussi")

    @discord.ui.button(style=discord.ButtonStyle.green,emoji=emoji_list[15])
    async def button_elio(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("ougi réussi")

    @discord.ui.button(style=discord.ButtonStyle.blurple,emoji=emoji_list[16])
    async def button_hupper(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("ougi réussi")

    @discord.ui.button(style=discord.ButtonStyle.red,emoji=emoji_list[17])
    async def button_feca(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("ougi réussi")



def build_construction_message(bot, id_message):
        info_dj = get_dj_info(id_message)
        text = f"Donjon **{info_dj['donjon']}** modulé au niveau de statis **S{info_dj['statis']}**"
        if info_dj['date'] != "":
            text += f"le {info_dj['date']}"
        if info_dj['besoin'] != "":
            text += f"\n __**Info**__ : {info_dj['besoin']}"
        for j in info_dj['joueurs']:
            text += f"\n- {bot.get_user(j[0]).mention}: {str.capitalize(j[1])}"
        return text



async def new_message(ctx, contenu):
        message = await ctx.send(contenu, view=TestButton())
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
        if info_dj['besoin'] != "":
            text += f"\n __**Info**__ : {info_dj['besoin']}"
        for j in info_dj['joueurs']:
            text += f"\n- {self.bot.get_user(j[0]).mention}: {str.capitalize(j[1])}"
        return text

    def dj_generique(self, ctx, donjon, statis, classe, date ="",besoin =""):
        id_message = ctx.message.id
        #TODO gérer le nombre de joueur
        nb_joueur = 6
        create_dj(id_message,donjon,date,statis,ctx.message.author.id,classe,nb_joueur,besoin)
        contenu = self.construction_message(id_message)
        return contenu

    @commands.command(
        description="Organiser un groupe de donjon lvl 20"
        )
    @app_commands.describe(donjon='Le donjon en question',
                        classe='La classe que vous comptez jouer',
                        statis= 'Le niveau de statis',
                        date= 'La date souhaitée dans le format JJ/MM/AAAA HH:MM heure française. Exemple: "24/02/1999 23:45"',
                        info = 'Info supplémentaire (exemple: besoin d\'une eniripsa, besoin d\'une personne expérimenté, 1/2/3 stele(s),  ...)')
    async def dj20(self, interaction: discord.Interaction,
                donjon : liste_donjon_20,
                statis : str,
                classe : str,
                date="",
                info = ""):
        contenu = self.dj_generique(interaction,donjon,statis,classe,date,info)
        await new_message(interaction, contenu)

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

async def setup(bot):
    await bot.add_cog(DonjonCog(bot))   