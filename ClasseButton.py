import discord
from liste_donjon import emoji_list,classe_list
from gestion_levels import add_player_dj, remove_player_dj,get_dj_info
from gestion_message import *

class ClassButton(discord.ui.View):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        for emoji, classe in zip(emoji_list, classe_list):
            self._add_class_button(emoji, classe)

    def _add_class_button(self, emoji, classe):
        button = discord.ui.Button(style=discord.ButtonStyle.gray, emoji=emoji)
        async def callback(interaction: discord.Interaction):
            predicat = await self.gestion_interaction_generique(interaction, classe)
            button.style = discord.ButtonStyle.red if predicat else discord.ButtonStyle.gray
            await interaction.response.edit_message(view=self)
        button.callback = callback
        self.add_item(button)

    async def gestion_interaction_generique(self, interaction,classe):
        id_dj = interaction.message.id
        player_id = interaction.user.id
        joueurs = get_dj_info(id_dj)['joueurs']
        result = False
        if [player_id,classe] in joueurs:
            remove_player_dj(id_dj,player_id)
        else:
            add_player_dj(id_dj,player_id,classe)
            result = True
        contenu, nb_joueur = construction_message(self.bot,id_dj)
        await modif_message(interaction.message,contenu,nb_joueur,self.bot)
        return result