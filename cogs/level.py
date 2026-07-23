import discord
from discord.ext import commands
from discord import app_commands
from gestion_levels import get_opti, get_low_cost, get_stuffer, set_low_cost, set_opti, del_low_cost, del_opti
from enum_class import Classe
from liste_donjon import list_levels

#WIP
class LevelCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.describe(
        classes="La classe en question",
        levels="Liste des levels optis pour cette classe séparé par des virgules")
    @commands.hybrid_command(
        description="Ajoute vos niveaux opti sur vos personnages",
        brief="Ajoute vos niveaux opti sur vos personnages",
        help = "Mettez votre pseudo suivi de la classe puis de la liste des niveaux. Exemple /addopti DarkLastumus Osamodas 200,215,185,110"
        )
    async def addopti(self, ctx: commands.Context,classes : Classe, levels: str) -> None:
        await ctx.defer()
        player_levels = set()
        for level in levels.split(","):
            player_levels.add(int(level))
        set_opti(ctx.author.id,classes.value,player_levels)
        await ctx.send(f"Ajout du joueur {ctx.author.name.capitalize()} les levels optis {levels}")

    @app_commands.describe(
            classes="La classe en question",
            levels="Liste des levels low costs pour cette classe séparé par des virgules")
    @commands.hybrid_command(
        description="Ajoute vos niveaux low cost sur vos personnes",
        brief="Ajoute vos niveaux low cost sur vos personnes",
        help = "Mettez votre pseudo suivi de la classe puis de la liste des niveaux. Exemple /addlowcost DarkLastumus Osamodas 200,215,185,110"
        )
    async def addlowcost(self, ctx: discord.context_managers,classes : Classe,levels: str) -> None:
        await ctx.defer()
        player_levels = set()
        for level in levels.split(","):
            player_levels.add(int(level))
        set_low_cost(ctx.author.id,classes.value,player_levels)
        await ctx.send(f"Ajout du joueur {ctx.author.name.capitalize()} les levels low cost {levels}")

    @app_commands.describe(
            classes="La classe en question",
            levels="Liste des levels optis pour cette classe séparé par des virgules")
    @commands.hybrid_command(
        description="Retire vos niveaux opti sur vos personnages",
        brief="Retire vos niveaux opti sur vos personnages",
        help = "Mettez votre pseudo suivi de la classe puis de la liste des niveaux. Exemple /removeopti DarkLastumus Osamodas 200,215,185,110"
        )
    async def removelowcost(self, ctx: discord.context_managers,classes : Classe, levels: list_levels) -> None:
        await ctx.defer()
        del_low_cost(ctx.author.id,classes.value,levels)
        await ctx.send(f"Retrait du level {levels} à la classe {classes.value} du joueur {ctx.author.name.capitalize()}")

    @app_commands.describe(
            classes="La classe en question",
            levels="Liste des levels optis pour cette classe séparé par des virgules")
    @commands.hybrid_command(
        description="Retire vos niveaux opti sur vos personnages",
        brief="Retire vos niveaux opti sur vos personnages",
        help = "Mettez votre pseudo suivi de la classe puis de la liste des niveaux. Exemple /removeopti DarkLastumus Osamodas 200,215,185,110"
        )
    async def removeopti(self, ctx: discord.context_managers,classes : Classe, levels: list_levels) -> None:
        await ctx.defer()
        del_opti(ctx.author.id,classes.value,levels)
        await ctx.send(f"Retrait du level {levels} à la classe {classes.value} du joueur {ctx.author.name.capitalize()}")

    @app_commands.describe(levels="le level en question")
    @commands.hybrid_command(
        description="Recupère tout les joueurs avec un perso opti au niveau",
        brief = "Joueur opti pour un certain niveau.",
        help = "Mettez la tranche de niveau recherché pour obtenir tout les joueurs avec un stuff opti à ce niveau. Exemple /getopti 200"
        )
    async def getopti(self, ctx: discord.context_managers,levels : list_levels):
        print(f"recherche joueur dans la tranche {levels}")
        await ctx.defer()
        dict_player = get_opti(int(levels))
        list_player = []
        delimiter = "\n"
        for player in dict_player:
            temp = ", "
            list_levels = temp.join(dict_player[player])
            member = await commands.MemberConverter().convert(ctx, str(player))
            list_player.append(f"- {member.nick} : {list_levels}")
        res = delimiter.join(list_player)
        await ctx.send(f"Joueur opti a la tranche {levels}:\n{res}")

    @app_commands.describe(levels="le level en question")
    @commands.hybrid_command(
        description="Recupère tout les joueurs avec au moins un perso low cost au niveau recherché",
        brief = "Joueur low cost pour un certain niveau.",
        help = "Mettez la tranche de niveau recherché pour obtenir tout les joueurs avec un stuff low cost à ce niveau. Exemple /getlowcost 200"
        )
    async def getlowcost(self, ctx: discord.context_managers,levels : list_levels):
        print(f"recherche joueur dans la tranche {levels}")
        await ctx.defer()
        dict_player = get_low_cost(int(levels))
        list_player = []
        delimiter = "\n"
        for player in dict_player:
            temp = ", "
            list_levels = temp.join(dict_player[player])
            member = await commands.MemberConverter().convert(ctx, str(player))
            list_player.append(f"- {member.nick} : {list_levels}")
        res = delimiter.join(list_player)
        await ctx.send(f"Joueur low cost a la tranche {levels}:\n{res}")

    @app_commands.describe(levels="le level en question")
    @commands.hybrid_command(
        description="Recupère tout les joueurs avec un stuff au niveau recherché",
        brief = "Joueur low cost et opti pour un certain niveau.",
        help = "Mettez la tranche de niveau recherché. Exemple /getstuffer 200"
        )
    async def getstuffer(self, ctx: discord.context_managers,levels : list_levels):
        print(f"recherche joueur dans la tranche {levels}:")
        await ctx.defer()
        dict_player = get_stuffer(int(levels))
        list_player = []
        delimiter = "\n"
        for player in dict_player:
            temp = ", "
            list_levels = temp.join(dict_player[player])
            member = await commands.MemberConverter().convert(ctx, str(player))
            list_player.append(f"- {member.nick} : {list_levels}")
        res = delimiter.join(list_player)
        await ctx.send(f"Joueur avec un stuff a la tranche {levels}:\n{res}")


async def setup(bot):
    pass
    """
    WIP PROJET TROP AMATEUR POUR LE MOMENT, A REVOIR PLUS TARD SI LE BOT EST UTILISE
    await bot.add_cog(LevelCog(bot))
    """