import discord
from liste_donjon import emoji_list,classe_list
from gestion_levels import add_player_dj, remove_player_dj,get_dj_info
from gestion_message import *

class ClassButton(discord.ui.View):
    def __init__(self,bot):
        super().__init__()
        self.bot = bot

    async def gestion_interaction_generique(self, interaction,classe):
        id_dj = interaction.message.id
        player_id = interaction.user.id
        joueurs = get_dj_info(id_dj)['joueurs']
        if [player_id,classe] in joueurs:
            remove_player_dj(id_dj,player_id)
        else:
            add_player_dj(id_dj,player_id,classe)
        contenu, nb_joueur = construction_message(self.bot,id_dj)
        await modif_message(interaction.message,contenu,nb_joueur,self.bot)

    @discord.ui.button(style=discord.ButtonStyle.blurple,emoji=emoji_list[0])
    async def button_osa(self,interaction: discord.Interaction, button: discord.ui.Button):
        await self.gestion_interaction_generique(interaction,classe_list[0])

    @discord.ui.button(style=discord.ButtonStyle.red,emoji=emoji_list[1])
    async def button_enu(self,interaction: discord.Interaction, button: discord.ui.Button):
        await self.gestion_interaction_generique(interaction,classe_list[1])

    @discord.ui.button(style=discord.ButtonStyle.gray,emoji=emoji_list[2])
    async def button_sram(self,interaction: discord.Interaction, button: discord.ui.Button):
        await self.gestion_interaction_generique(interaction,classe_list[2])

    @discord.ui.button(style=discord.ButtonStyle.green,emoji=emoji_list[3])
    async def button_xelor(self,interaction: discord.Interaction, button: discord.ui.Button):
        await self.gestion_interaction_generique(interaction,classe_list[3])

    @discord.ui.button(style=discord.ButtonStyle.blurple,emoji=emoji_list[4])
    async def button_eca(self,interaction: discord.Interaction, button: discord.ui.Button):
        await self.gestion_interaction_generique(interaction,classe_list[4])

    @discord.ui.button(style=discord.ButtonStyle.blurple,emoji=emoji_list[5])
    async def button_eni(self,interaction: discord.Interaction, button: discord.ui.Button):
        await self.gestion_interaction_generique(interaction,classe_list[5])

    @discord.ui.button(style=discord.ButtonStyle.red,emoji=emoji_list[6])
    async def button_iop(self,interaction: discord.Interaction, button: discord.ui.Button):
        await self.gestion_interaction_generique(interaction,classe_list[6])

    @discord.ui.button(style=discord.ButtonStyle.gray,emoji=emoji_list[7])
    async def button_cra(self,interaction: discord.Interaction, button: discord.ui.Button):
        await self.gestion_interaction_generique(interaction,classe_list[7])

    @discord.ui.button(style=discord.ButtonStyle.green,emoji=emoji_list[8])
    async def button_sadi(self,interaction: discord.Interaction, button: discord.ui.Button):
        await self.gestion_interaction_generique(interaction,classe_list[8])

    @discord.ui.button(style=discord.ButtonStyle.blurple,emoji=emoji_list[9])
    async def button_sacri(self,interaction: discord.Interaction, button: discord.ui.Button):
        await self.gestion_interaction_generique(interaction,classe_list[9])

    @discord.ui.button(style=discord.ButtonStyle.blurple,emoji=emoji_list[10])
    async def button_panda(self,interaction: discord.Interaction, button: discord.ui.Button):
        await self.gestion_interaction_generique(interaction,classe_list[10])

    @discord.ui.button(style=discord.ButtonStyle.red,emoji=emoji_list[11])
    async def button_roub(self,interaction: discord.Interaction, button: discord.ui.Button):
        await self.gestion_interaction_generique(interaction,classe_list[11])

    @discord.ui.button(style=discord.ButtonStyle.gray,emoji=emoji_list[12])
    async def button_zobal(self,interaction: discord.Interaction, button: discord.ui.Button):
        await self.gestion_interaction_generique(interaction,classe_list[12])

    @discord.ui.button(style=discord.ButtonStyle.green,emoji=emoji_list[13])
    async def button_ougi(self,interaction: discord.Interaction, button: discord.ui.Button):
        await self.gestion_interaction_generique(interaction,classe_list[13])

    @discord.ui.button(style=discord.ButtonStyle.blurple,emoji=emoji_list[14])
    async def button_steamer(self,interaction: discord.Interaction, button: discord.ui.Button):
        await self.gestion_interaction_generique(interaction,classe_list[14])

    @discord.ui.button(style=discord.ButtonStyle.blurple,emoji=emoji_list[15])
    async def button_elio(self,interaction: discord.Interaction, button: discord.ui.Button):
        await self.gestion_interaction_generique(interaction,classe_list[15])

    @discord.ui.button(style=discord.ButtonStyle.red,emoji=emoji_list[16])
    async def button_hupper(self,interaction: discord.Interaction, button: discord.ui.Button):
        await self.gestion_interaction_generique(interaction,classe_list[16])

    @discord.ui.button(style=discord.ButtonStyle.gray,emoji=emoji_list[17])
    async def button_feca(self,interaction: discord.Interaction, button: discord.ui.Button):
        await self.gestion_interaction_generique(interaction,classe_list[17])