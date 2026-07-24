import discord
from discord.ext import commands
from discord import app_commands
from liste_donjon import *
from ClasseButton import ClassButton
from gestion_levels import create_dj, convert_date
from gestion_message import *

MAX_LEVEL = 245

class DonjonCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        for level in range(20,MAX_LEVEL+1,15):
            self._add_dj_command(level)

    def dj_generique(self, id, donjon, stasis, date ="",info =""):
        id_message = id
        nb_joueur = donjon_nb_joueur_map.get(donjon)
        t_date = convert_date(date)
        create_dj(id_message,donjon,t_date,stasis,nb_joueur,info)
        contenu = construction_message(self.bot, id_message)
        return contenu

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
            link = donjon_link_map.get(donjon, "")
            channel = discord.utils.get(ctx.guild.text_channels, name="activité")
            interaction_dj = await channel.send("Création de votre donjon, veuillez patientez...", view=ClassButton(bot,donjon_nb_joueur_map.get(donjon), link=link))
            await interaction_dj.create_thread(name=f"Donjon {donjon} stasis {stasis} lvl {level}")
            contenu = dj_generique(id=interaction_dj.id, donjon=donjon, stasis=stasis, date=date, info=info)
            await ctx.send(f"Votre donjon a été créé avec succès! [Ici]({interaction_dj.jump_url})")
            await interaction_dj.edit(content=contenu)

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