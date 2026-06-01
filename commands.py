import os
from dotenv import load_dotenv
import discord
from enum_class import Classe
from discord.ext import commands
from discord import app_commands
from typing import Literal
from gestion_levels import *
from liste_donjon import *
from cogs.donjon import *

load_dotenv()

token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents = intents)

#@bot.hybrid_command(
#        description="Ebauche WIP",
#)
#async def stele(ctx,name,item1,qt1,item2,qt2,item3,qt3,item4,qt4,item5,qt5,item6,qt6):
#    await ctx.send(f"stele {name}:\n- {item1}: 0/{qt1}\n- {item2}: 0/{qt2}\n- {item3}: 0/{qt3}\n- {item4}: 0/{qt4}\n- {item5}: 0/{qt5}\n- {item6}: 0/{qt6}")

@app_commands.describe(
        classes='La classe en question',
        levels="Liste des levels optis pour cette classe séparé par des virgules")
@bot.hybrid_command(
    description="Ajoute vos niveaux opti sur vos personnages",
    brief="Ajoute vos niveaux opti sur vos personnages",
    help = "Mettez votre pseudo suivi de la classe puis de la liste des niveaux. Exemple /addopti DarkLastumus Osamodas 200,215,185,110"
    )
async def addopti(ctx: discord.context_managers,classes : Classe, levels: str) -> None:
    await ctx.defer()
    player_levels = set()
    for level in levels.split(","):
        player_levels.add(int(level))
    set_opti(ctx.author.id,classes.value,player_levels)
    await ctx.send(f"Ajout du joueur {ctx.author.name.capitalize()} les levels optis {levels}")

@app_commands.describe(
        classes='La classe en question',
        levels="Liste des levels low costs pour cette classe séparé par des virgules")
@bot.hybrid_command(
    description="Ajoute vos niveaux low cost sur vos personnes",
    brief="Ajoute vos niveaux low cost sur vos personnes",
    help = "Mettez votre pseudo suivi de la classe puis de la liste des niveaux. Exemple /addlowcost DarkLastumus Osamodas 200,215,185,110"
    )
async def addlowcost(ctx: discord.context_managers,classes : Classe,levels: str) -> None:
    await ctx.defer()
    player_levels = set()
    for level in levels.split(","):
        player_levels.add(int(level))
    set_low_cost(ctx.author.id,classes.value,player_levels)
    await ctx.send(f"Ajout du joueur {ctx.author.name.capitalize()} les levels low cost {levels}")

@app_commands.describe(
        classes='La classe en question',
        levels="Liste des levels optis pour cette classe séparé par des virgules")
@bot.hybrid_command(
    description="Retire vos niveaux opti sur vos personnages",
    brief="Retire vos niveaux opti sur vos personnages",
    help = "Mettez votre pseudo suivi de la classe puis de la liste des niveaux. Exemple /removeopti DarkLastumus Osamodas 200,215,185,110"
    )
async def removelowcost(ctx: discord.context_managers,classes : Classe, levels: list_levels) -> None:
    await ctx.defer()
    del_low_cost(ctx.author.id,classes.value,levels)
    await ctx.send(f"Retrait du level {levels} à la classe {classes.value} du joueur {ctx.author.name.capitalize()}")

@app_commands.describe(
        classes='La classe en question',
        levels="Liste des levels optis pour cette classe séparé par des virgules")
@bot.hybrid_command(
    description="Retire vos niveaux opti sur vos personnages",
    brief="Retire vos niveaux opti sur vos personnages",
    help = "Mettez votre pseudo suivi de la classe puis de la liste des niveaux. Exemple /removeopti DarkLastumus Osamodas 200,215,185,110"
    )
async def removeopti(ctx: discord.context_managers,classes : Classe, levels: list_levels) -> None:
    await ctx.defer()
    del_opti(ctx.author.id,classes.value,levels)
    await ctx.send(f"Retrait du level {levels} à la classe {classes.value} du joueur {ctx.author.name.capitalize()}")

@app_commands.describe(levels='le level en question')
@bot.hybrid_command(
    description="Recupère tout les joueurs avec un perso opti au niveau",
    brief = "Joueur opti pour un certain niveau.",
    help = "Mettez la tranche de niveau recherché pour obtenir tout les joueurs avec un stuff opti à ce niveau. Exemple /getopti 200"
    )
async def getopti(ctx: discord.context_managers,levels : list_levels):
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

@app_commands.describe(levels='le level en question')
@bot.hybrid_command(
    description="Recupère tout les joueurs avec au moins un perso low cost au niveau recherché",
    brief = "Joueur low cost pour un certain niveau.",
    help = "Mettez la tranche de niveau recherché pour obtenir tout les joueurs avec un stuff low cost à ce niveau. Exemple /getlowcost 200"
    )
async def getlowcost(ctx: discord.context_managers,levels : list_levels):
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

@app_commands.describe(levels='le level en question')
@bot.hybrid_command(
    description="Recupère tout les joueurs avec un stuff au niveau recherché",
    brief = "Joueur low cost et opti pour un certain niveau.",
    help = "Mettez la tranche de niveau recherché. Exemple /getstuffer 200"
    )
async def getstuffer(ctx: discord.context_managers,levels : list_levels):
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

@bot.hybrid_command(description='Bonjour?')
async def bonjour(ctx: discord.context_managers):
    await ctx.send(f"Bonsoir c'est moi Lastumus, je déteste les péruches, le hockey et ma soeur. Par contre j'adore les Tacos!")

@bot.event
async def on_reaction_add(reaction, user):
    message = reaction.message
    channel = discord.utils.get(message.guild.channels, name="commande-bot") #our channel
    test_full = False
    id = 0
    if message.channel.id == channel.id: # checking if it's the same channel
        if message.author == bot.user: #checking if it's sent by the bot
            if user != bot.user:
                if reaction.emoji.name in classe_list: #checking the emoji
                    id = message.interaction.id
                    test_full = add_player_dj(id,user.id,reaction.emoji.name)
                    text = construction_message(id)
                    await message.edit(content=text)
    if test_full:
        liste = message.mentions
        await message.clear_reactions()
        liste_mention = []
        for joueur in liste:
            liste_mention.append(bot.get_user(joueur.id).mention)
        delete_dj(id)
        await message.reply(f"{','.join(liste_mention)} votre donjon est prêt !")
    
@bot.event
async def on_reaction_remove(reaction, user): #Vishaa tu casses les couilles, même si tu as raison
    message = reaction.message
    channel = discord.utils.get(message.guild.channels, name="commande-bot") #our channel
    if message.channel.id == channel.id: # checking if it's the same channel
        if message.author == bot.user: #checking if it's sent by the bot
            if user != bot.user:
                if reaction.emoji.name in classe_list: #checking the emoji
                    id = message.interaction.id
                    remove_player_dj(id,user.id)
                    text = construction_message(id)
                    await message.edit(content=text)

@bot.event
async def on_ready():
    try:
        sync = await bot.tree.sync()
        print(f"{len(sync)} commande chargé")
    except Exception as e:
        print(e)

bot.run(token=token)