import os
from dotenv import load_dotenv
import discord
from enum_class import Classe
from typing import Literal
from discord.ext import commands
from discord import app_commands
from gestion_levels import *
from keep_alive import keep_alive

load_dotenv()

token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents = intents)

#@bot.hybrid_command(
#        description="Ebauche WIP",
#)
#async def stele(ctx,name,item1,qt1,item2,qt2,item3,qt3,item4,qt4,item5,qt5,item6,qt6):
#    await ctx.send(f"stele {name}:\n- {item1}: 0/{qt1}\n- {item2}: 0/{qt2}\n- {item3}: 0/{qt3}\n- {item4}: 0/{qt4}\n- {item5}: 0/{qt5}\n- {item6}: 0/{qt6}")

@app_commands.describe(classes='La classe en question')
@bot.hybrid_command(
    description="Ajoute vos niveaux opti sur vos personnes",
    brief="Ajoute vos niveaux opti sur vos personnes",
    help = "Mettez votre pseudo suivi de la classe puis de la liste des niveaux. Exemple /addopti DarkLastumus Osamodas 200,215,185,110"
    )
async def addopti(ctx: discord.context_managers,pseudo : str,classes : Classe,levels: str) -> None:
    await ctx.defer()
    player_levels = set()
    for level in levels.split(","):
        player_levels.add(int(level))
    set_opti(str.capitalize(pseudo),classes.value,player_levels)
    await ctx.send(f"Ajout du joueur {pseudo.capitalize()} les levels optis {levels}")

@app_commands.describe(levels='le level en question')
@bot.hybrid_command(
    description="Recupère tout les joueurs avec un perso opti au niveau",
    brief = "Joueur opti pour un certain niveau.",
    help = "Mettez la tranche de niveau recherché pour obtenir tout les joueurs avec un stuff opti à ce niveau. Exemple /getopti 200"
    )
async def getopti(ctx: discord.context_managers,levels : Literal[20,35,50,65,80,95,110,125,140,155,170,185,200,215,230,245]):
    print(f"recherche joueur dans la tranche {levels}")
    await ctx.defer()
    dict_player = get_opti(int(levels))
    list_player = []
    delimiter = "\n"
    for player in dict_player:
        temp = ", "
        list_levels = temp.join(dict_player[player])
        list_player.append(f"- {player} : {list_levels}")
    res = delimiter.join(list_player)
    await ctx.send(f"Joueur opti a la tranche {levels}:\n{res}")

@app_commands.describe(levels='le level en question')
@bot.hybrid_command(
    description="Recupère tout les joueurs avec au moins un perso low cost au niveau recherché",
    brief = "Joueur low cost pour un certain niveau.",
    help = "Mettez la tranche de niveau recherché pour obtenir tout les joueurs avec un stuff low cost à ce niveau. Exemple /getlowcost 200"
    )
async def getlowcost(ctx: discord.context_managers,levels : Literal[20,35,50,65,80,95,110,125,140,155,170,185,200,215,230,245]):
    print(f"recherche joueur dans la tranche {levels}")
    await ctx.defer()
    dict_player = get_low_cost(int(levels))
    list_player = []
    delimiter = "\n"
    for player in dict_player:
        temp = ", "
        list_levels = temp.join(dict_player[player])
        list_player.append(f"- {player} : {list_levels}")
    res = delimiter.join(list_player)
    await ctx.send(f"Joueur low cost a la tranche {levels}:\n{res}")

@app_commands.describe(levels='le level en question')
@bot.hybrid_command(
    description="Recupère tout les joueurs avec un stuff au niveau recherché",
    brief = "Joueur low cost et opti pour un certain niveau.",
    help = "Mettez la tranche de niveau recherché. Exemple /getstuffer 200"
    )
async def getstuffer(ctx: discord.context_managers,levels : Literal[20,35,50,65,80,95,110,125,140,155,170,185,200,215,230,245]):
    print(f"recherche joueur dans la tranche {levels}:")
    await ctx.defer()
    dict_player = get_stuffer(int(levels))
    list_player = []
    delimiter = "\n"
    for player in dict_player:
        temp = ", "
        list_levels = temp.join(dict_player[player])
        list_player.append(f"- {player} : {list_levels}")
    res = delimiter.join(list_player)
    await ctx.send(f"Joueur avec un stuff a la tranche {levels}:\n{res}")

@bot.event
async def on_ready():
    try:
        sync = await bot.tree.sync()
        print(f"{len(sync)} commande chargé")
    except Exception as e:
        print(e)

keep_alive()
bot.run(token=token)