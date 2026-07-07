import discord
from liste_donjon import emoji_list,classe_list
from gestion_levels import add_player_dj, remove_player_dj,get_dj_info, modif_compo
from gestion_message import *

class ClassButton(discord.ui.View):
    def __init__(self, bot, nb_joueur_max,link= "http://www.google.fr"):
        super().__init__(timeout=None)
        self.bot = bot
        
        for n, (emoji, classe) in enumerate(zip(emoji_list, classe_list)):
            name = f"Button-{n}"
            row =  n // 5
            self._add_class_button(emoji, classe, name, row,nb_joueur_max)
        if link == "":
            self.add_item(discord.ui.Button(style=discord.ButtonStyle.red,label="Pas de guide dispo",emoji="🖕",disabled=True, row=4))
        else:
            self.add_item(discord.ui.Button(style=discord.ButtonStyle.url,label="Guide du dj",url=link, row=4))
        self._add_sub_button(nb_joueur_max)
            
    def _add_class_button(self, emoji, classe, name, row,nb_joueur_max):
        button = discord.ui.Button(style=discord.ButtonStyle.gray, emoji=emoji, custom_id=name, row=row)
        async def callback(interaction: discord.Interaction):
            predicat = await self.gestion_interaction_generique(interaction, classe,nb_joueur_max)
            button.style = discord.ButtonStyle.blurple if predicat else discord.ButtonStyle.gray
            await interaction.response.edit_message(view=self)
        button.callback = callback
        self.add_item(button)

    def _add_sub_button(self,nb_joueur_max):
        buttons_data = [
            ("dpt", "DPT", discord.ButtonStyle.red, "<:dpt:1522301255043776552>"),
            ("tank", "TANK", discord.ButtonStyle.green, "<:tank:1522298751631364248>"),
            ("support", "SUPPORT", discord.ButtonStyle.blurple, "<:Armor_soin:1521639697657499890>"),
        ]
        for custom_id, label, style, emoji in buttons_data:
            button = discord.ui.Button(style=style, custom_id=custom_id, label=label, row=4)
            async def callback(interaction: discord.Interaction, _emoji=emoji):
                await interaction.response.defer()
                id_dj = interaction.message.id
                player_id = interaction.user.id
                modif_compo(id_dj, player_id, _emoji)
                contenu = construction_message(self.bot, id_dj)
                await interaction.message.edit(content=contenu, view=self)
            button.callback = callback
            self.add_item(button)

    async def gestion_interaction_generique(self, interaction,classe,nb_joueur_max):
        id_dj = interaction.message.id
        player_id = interaction.user.id
        joueurs = get_dj_info(id_dj)['joueurs']
        result = False
        if [player_id,classe] in joueurs:
            remove_player_dj(id_dj,player_id)
        else:
            add_player_dj(id_dj,player_id,classe)
            result = True
        contenu = construction_message(self.bot,id_dj)
        await interaction.message.edit(content=contenu, view=self)
        return result