import discord
from liste_donjon import emoji_list

class ClassButton(discord.ui.View):

    @discord.ui.button(style=discord.ButtonStyle.blurple,emoji=emoji_list[0])
    async def button_osa(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f"{interaction.user} est un osamodas pour le dj {interaction.original_response}")

    @discord.ui.button(style=discord.ButtonStyle.red,emoji=emoji_list[1])
    async def button_enu(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("enu réussi")

    @discord.ui.button(style=discord.ButtonStyle.gray,emoji=emoji_list[2])
    async def button_sram(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("sram réussi")

    @discord.ui.button(style=discord.ButtonStyle.green,emoji=emoji_list[3])
    async def button_xelor(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("xelor réussi")

    @discord.ui.button(style=discord.ButtonStyle.blurple,emoji=emoji_list[4])
    async def button_eca(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("eca réussi")

    @discord.ui.button(style=discord.ButtonStyle.red,emoji=emoji_list[5])
    async def button_eni(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("eni réussi")

    @discord.ui.button(style=discord.ButtonStyle.gray,emoji=emoji_list[6])
    async def button_iop(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("iop réussi")

    @discord.ui.button(style=discord.ButtonStyle.green,emoji=emoji_list[7])
    async def button_cra(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("cra réussi")

    @discord.ui.button(style=discord.ButtonStyle.blurple,emoji=emoji_list[8])
    async def button_sadi(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("sadi réussi")

    @discord.ui.button(style=discord.ButtonStyle.red,emoji=emoji_list[9])
    async def button_sacri(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("sacri réussi")

    @discord.ui.button(style=discord.ButtonStyle.gray,emoji=emoji_list[10])
    async def button_panda(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("panda réussi")

    @discord.ui.button(style=discord.ButtonStyle.green,emoji=emoji_list[11])
    async def button_roub(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("roub réussi")

    @discord.ui.button(style=discord.ButtonStyle.blurple,emoji=emoji_list[12])
    async def button_zobal(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("zobal réussi")

    @discord.ui.button(style=discord.ButtonStyle.red,emoji=emoji_list[13])
    async def button_ougi(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("ougi réussi")

    @discord.ui.button(style=discord.ButtonStyle.gray,emoji=emoji_list[14])
    async def button_steamer(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("steamer réussi")

    @discord.ui.button(style=discord.ButtonStyle.green,emoji=emoji_list[15])
    async def button_elio(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("elio réussi")

    @discord.ui.button(style=discord.ButtonStyle.blurple,emoji=emoji_list[16])
    async def button_hupper(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("hupper réussi")

    @discord.ui.button(style=discord.ButtonStyle.red,emoji=emoji_list[17])
    async def button_feca(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("féca réussi")