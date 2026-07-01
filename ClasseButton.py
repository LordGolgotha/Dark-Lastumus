import discord
from liste_donjon import emoji_list,classe_list
from gestion_levels import add_player_dj, remove_player_dj,get_dj_info
from gestion_message import *

class ClassButton(discord.ui.View):
    def __init__(self, bot, link= "http://www.google.fr"):
        super().__init__(timeout=None)
        self.bot = bot
        
        for n, (emoji, classe) in enumerate(zip(emoji_list, classe_list)):
            name = f"Button-{n}"
            row =  n // 5
            self._add_class_button(emoji, classe, name, row)
        self.add_item(discord.ui.Button(style=discord.ButtonStyle.url,label="Guide du dj",url=link, row=4))
        self.add_item(discord.ui.Button(style=discord.ButtonStyle.red,label="DPT", row=4))
        self.add_item(discord.ui.Button(style=discord.ButtonStyle.green,label="TANK", row=4))
        self.add_item(discord.ui.Button(style=discord.ButtonStyle.blurple,label="SUPPORT", row=4))
            
    def _add_class_button(self, emoji, classe, name, row):
        button = discord.ui.Button(style=discord.ButtonStyle.gray, emoji=emoji, custom_id=name, row=row)
        async def callback(interaction: discord.Interaction):
            predicat = await self.gestion_interaction_generique(interaction, classe)
            button.style = discord.ButtonStyle.blurple if predicat else discord.ButtonStyle.gray
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