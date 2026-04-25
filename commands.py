import os
from dotenv import load_dotenv
import discord
from enum_class import Classe
from discord.ext import commands
from discord import app_commands
from typing import Literal
from gestion_levels import *
from liste_donjon import *

load_dotenv()

emoji_list = [
    '<:osamodas:1483790487356706868>',
    '<:enutrof:1483790486023176372>',
    '<:sram:1483790484542459955>',
    '<:xelor:1483790482793562112>',
    '<:ecaflip:1483790481367236608>',
    '<:eniripsa:1483790480054419537>',
    '<:iop:1483790477986627615>',
    '<:cra:1483790476959289434>',
    '<:sadida:1483790475638083784>',
    '<:sacrieur:1483790474363011152>',
    '<:pandawa:1483790472286572614>',
    '<:roublard:1483790471154368533>',
    '<:zobal:1483790469291966526>',
    '<:ouginak:1483790467639410698>',
    '<:steamer:1483790466230255646>',
    '<:eliotrope:1483790464573505589>',
    '<:huppermage:1483790462593794190>',
    '<:feca:1483790196263620669>'
]
classe_list = [
    'osamodas',
    'enutrof',
    'sram',
    'xelor',
    'ecaflip',
    'eniripsa',
    'iop',
    'cra',
    'sadida',
    'sacrieur',
    'pandawa',
    'roublard',
    'zobal',
    'ouginak',
    'steamer',
    'eliotrope',
    'huppermage',
    'feca'
]

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
        pseudo='Votre pseudo le plus connus par la guilde',
        levels="Liste des levels optis pour cette classe séparé par des virgules")
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

@app_commands.describe(
        classes='La classe en question',
        pseudo='Votre pseudo le plus connus par la guilde',
        levels="Liste des levels low costs pour cette classe séparé par des virgules")
@bot.hybrid_command(
    description="Ajoute vos niveaux low cost sur vos personnes",
    brief="Ajoute vos niveaux low cost sur vos personnes",
    help = "Mettez votre pseudo suivi de la classe puis de la liste des niveaux. Exemple /addlowcost DarkLastumus Osamodas 200,215,185,110"
    )
async def addlowcost(ctx: discord.context_managers,pseudo : str,classes : Classe,levels: str) -> None:
    await ctx.defer()
    player_levels = set()
    for level in levels.split(","):
        player_levels.add(int(level))
    set_low_cost(str.capitalize(pseudo),classes.value,player_levels)
    await ctx.send(f"Ajout du joueur {pseudo.capitalize()} les levels low cost {levels}")


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

def dj_generique(ctx,  donjon, statis, classe,lvl, date ="",besoin =""):
    contenu = f"Donjon **{donjon}** modulé niveau **{lvl}**, niveau de statis **S{statis}**"
    if date != "":
        utc = int(ctx.interaction.created_at.strftime("%z"))
        contenu += f" le {convert_date(date,utc)}"
    if besoin != "":
        contenu += f": \n - Besoin d'au moins: {besoin}"
    

    contenu += f"\n- {ctx.author.mention}: {classe}"
    return contenu


async def new_message(ctx, contenu):
    message = await ctx.send(contenu)
    
    for emoji in emoji_list:
        await message.add_reaction(emoji)

@app_commands.describe(donjon='Le donjon en question',
                       classe='La classe que vous comptez jouer',
                       statis= 'Le niveau de statis',
                       date= 'La date souhaitée dans le format JJ/MM/AAAA HH:MM heure française. Exemple: "24/02/1999 23:45"',
                       info = 'Info supplémentaire (exemple: besoin d\'une eniripsa, besoin d\'une personne expérimenté, 1/2/3 stele(s),  ...)')
@bot.hybrid_command(
    description="Organiser un groupe de donjon lvl 20"
    )
async def dj20(ctx: discord.context_managers,
               donjon : liste_donjon_20,
               statis : Literal[1,2,3,4,5,6,7,8,9,10],
               classe : Classe,
               date="",
               info = ""):
    contenu = dj_generique(ctx,donjon,statis,classe.name,20,date,info)
    await new_message(ctx, contenu)
    
@app_commands.describe(donjon='Le donjon en question',
                       classe='La classe que vous comptez jouer',
                       statis= 'Le niveau de statis',
                       date= 'La date souhaitée dans le format JJ/MM/AAAA HH:MM heure française. Exemple: "24/02/1999 23:45"',
                       info = 'Info supplémentaire (exemple: besoin d\'une eniripsa, besoin d\'une personne expérimenté, 1/2/3 stele(s),  ...)')
@bot.hybrid_command(
    description="Organiser un groupe de donjon lvl 35"
    )
async def dj35(ctx: discord.context_managers,
               donjon : liste_donjon_35,
               statis : Literal[1,2,3,4,5,6,7,8,9,10],
               classe : Classe,
               date="",
               info = ""):
    contenu = dj_generique(ctx,donjon,statis,classe.name,35,date,info)
    await new_message(ctx, contenu)

@app_commands.describe(donjon='Le donjon en question',
                       classe='La classe que vous comptez jouer',
                       statis= 'Le niveau de statis',
                       date= 'La date souhaitée dans le format JJ/MM/AAAA HH:MM heure française. Exemple: "24/02/1999 23:45"',
                       info = 'Info supplémentaire (exemple: besoin d\'une eniripsa, besoin d\'une personne expérimenté, 1/2/3 stele(s),  ...)')
@bot.hybrid_command(
    description="Organiser un groupe de donjon lvl 50"
    )
async def dj50(ctx: discord.context_managers,
               donjon : liste_donjon_50,
               statis : Literal[1,2,3,4,5,6,7,8,9,10],
               classe : Classe,
               date="",
               info = ""):
    contenu = dj_generique(ctx,donjon,statis,classe.name,65,date,info)
    await new_message(ctx, contenu)

@app_commands.describe(donjon='Le donjon en question',
                       classe='La classe que vous comptez jouer',
                       statis= 'Le niveau de statis',
                       date= 'La date souhaitée dans le format JJ/MM/AAAA HH:MM heure française. Exemple: "24/02/1999 23:45"',
                       info = 'Info supplémentaire (exemple: besoin d\'une eniripsa, besoin d\'une personne expérimenté, 1/2/3 stele(s),  ...)')
@bot.hybrid_command(
    description="Organiser un groupe de donjon lvl 65"
    )
async def dj65(ctx: discord.context_managers,
               donjon : liste_donjon_65,
               statis : Literal[1,2,3,4,5,6,7,8,9,10],
               classe : Classe,
               date="",
               info = ""):
    contenu = dj_generique(ctx,donjon,statis,classe.name,65,date,info)
    await new_message(ctx, contenu)

@app_commands.describe(donjon='Le donjon en question',
                       classe='La classe que vous comptez jouer',
                       statis= 'Le niveau de statis',
                       date= 'La date souhaitée dans le format JJ/MM/AAAA HH:MM heure française. Exemple: "24/02/1999 23:45"',
                       info = 'Info supplémentaire (exemple: besoin d\'une eniripsa, besoin d\'une personne expérimenté, 1/2/3 stele(s),  ...)')
@bot.hybrid_command(
    description="Organiser un groupe de donjon lvl 80"
    )
async def dj80(ctx: discord.context_managers,
               donjon : liste_donjon_80,
               statis : Literal[1,2,3,4,5,6,7,8,9,10],
               classe : Classe,
               date="",
               info = ""):
    contenu = dj_generique(ctx,donjon,statis,classe.name,80,date,info)
    await new_message(ctx, contenu)

@app_commands.describe(donjon='Le donjon en question',
                       classe='La classe que vous comptez jouer',
                       statis= 'Le niveau de statis',
                       date= 'La date souhaitée dans le format JJ/MM/AAAA HH:MM heure française. Exemple: "24/02/1999 23:45"',
                       info = 'Info supplémentaire (exemple: besoin d\'une eniripsa, besoin d\'une personne expérimenté, 1/2/3 stele(s),  ...)')
@bot.hybrid_command(
    description="Organiser un groupe de donjon lvl 95"
    )
async def dj95(ctx: discord.context_managers,
               donjon : liste_donjon_95,
               statis : Literal[1,2,3,4,5,6,7,8,9,10],
               classe : Classe,
               date="",
               info = ""):
    contenu = dj_generique(ctx,donjon,statis,classe.name,95,date,info)
    await new_message(ctx, contenu)

@app_commands.describe(donjon='Le donjon en question',
                       classe='La classe que vous comptez jouer',
                       statis= 'Le niveau de statis',
                       date= 'La date souhaitée dans le format JJ/MM/AAAA HH:MM heure française. Exemple: "24/02/1999 23:45"',
                       info = 'Info supplémentaire (exemple: besoin d\'une eniripsa, besoin d\'une personne expérimenté, 1/2/3 stele(s),  ...)')
@bot.hybrid_command(
    description="Organiser un groupe de donjon lvl 110"
    )
async def dj110(ctx: discord.context_managers,
               donjon : liste_donjon_110,
               statis : Literal[1,2,3,4,5,6,7,8,9,10],
               classe : Classe,
               date="",
               info = ""):
    contenu = dj_generique(ctx,donjon,statis,classe.name,110,date,info)
    await new_message(ctx, contenu)

@app_commands.describe(donjon='Le donjon en question',
                       classe='La classe que vous comptez jouer',
                       statis= 'Le niveau de statis',
                       date= 'La date souhaitée dans le format JJ/MM/AAAA HH:MM heure française. Exemple: "24/02/1999 23:45"',
                       info = 'Info supplémentaire (exemple: besoin d\'une eniripsa, besoin d\'une personne expérimenté, 1/2/3 stele(s),  ...)')
@bot.hybrid_command(
    description="Organiser un groupe de donjon lvl 125"
    )
async def dj125(ctx: discord.context_managers,
               donjon : liste_donjon_125,
               statis : Literal[1,2,3,4,5,6,7,8,9,10],
               classe : Classe,
               date="",
               info = ""):
    contenu = dj_generique(ctx,donjon,statis,classe.name,125,date,info)
    await new_message(ctx, contenu)

@app_commands.describe(donjon='Le donjon en question',
                       classe='La classe que vous comptez jouer',
                       statis= 'Le niveau de statis',
                       date= 'La date souhaitée dans le format JJ/MM/AAAA HH:MM heure française. Exemple: "24/02/1999 23:45"',
                       info = 'Info supplémentaire (exemple: besoin d\'une eniripsa, besoin d\'une personne expérimenté, 1/2/3 stele(s),  ...)')
@bot.hybrid_command(
    description="Organiser un groupe de donjon lvl 140"
    )
async def dj140(ctx: discord.context_managers,
               donjon : liste_donjon_140,
               statis : Literal[1,2,3,4,5,6,7,8,9,10],
               classe : Classe,
               date="",
               info = ""):
    contenu = dj_generique(ctx,donjon,statis,classe.name,140,date,info)
    await new_message(ctx, contenu)

@app_commands.describe(donjon='Le donjon en question',
                       classe='La classe que vous comptez jouer',
                       statis= 'Le niveau de statis',
                       date= 'La date souhaitée dans le format JJ/MM/AAAA HH:MM heure française. Exemple: "24/02/1999 23:45"',
                       info = 'Info supplémentaire (exemple: besoin d\'une eniripsa, besoin d\'une personne expérimenté, 1/2/3 stele(s),  ...)')
@bot.hybrid_command(
    description="Organiser un groupe de donjon lvl 155"
    )
async def dj155(ctx: discord.context_managers,
               donjon : liste_donjon_155,
               statis : Literal[1,2,3,4,5,6,7,8,9,10],
               classe : Classe,
               date="",
               info = ""):
    contenu = dj_generique(ctx,donjon,statis,classe.name,155,date,info)
    await new_message(ctx, contenu)

@app_commands.describe(donjon='Le donjon en question',
                       classe='La classe que vous comptez jouer',
                       statis= 'Le niveau de statis',
                       date= 'La date souhaitée dans le format JJ/MM/AAAA HH:MM heure française. Exemple: "24/02/1999 23:45"',
                       info = 'Info supplémentaire (exemple: besoin d\'une eniripsa, besoin d\'une personne expérimenté, 1/2/3 stele(s),  ...)')
@bot.hybrid_command(
    description="Organiser un groupe de donjon lvl 170"
    )
async def dj170(ctx: discord.context_managers,
               donjon : liste_donjon_170,
               statis : Literal[1,2,3,4,5,6,7,8,9,10],
               classe : Classe,
               date="",
               info = ""):
    contenu = dj_generique(ctx,donjon,statis,classe.name,170,date,info)
    await new_message(ctx, contenu)

@app_commands.describe(donjon='Le donjon en question',
                       classe='La classe que vous comptez jouer',
                       statis= 'Le niveau de statis',
                       date= 'La date souhaitée dans le format JJ/MM/AAAA HH:MM heure française. Exemple: "24/02/1999 23:45"',
                       info = 'Info supplémentaire (exemple: besoin d\'une eniripsa, besoin d\'une personne expérimenté, 1/2/3 stele(s),  ...)')
@bot.hybrid_command(
    description="Organiser un groupe de donjon lvl 185"
    )
async def dj185(ctx: discord.context_managers,
               donjon : liste_donjon_185,
               statis : Literal[1,2,3,4,5,6,7,8,9,10],
               classe : Classe,
               date="",
               info = ""):
    contenu = dj_generique(ctx,donjon,statis,classe.name,185,date,info)
    await new_message(ctx, contenu)

@app_commands.describe(donjon='Le donjon en question',
                       classe='La classe que vous comptez jouer',
                       statis= 'Le niveau de statis',
                       date= 'La date souhaitée dans le format JJ/MM/AAAA HH:MM heure française. Exemple: "24/02/1999 23:45"',
                       info = 'Info supplémentaire (exemple: besoin d\'une eniripsa, besoin d\'une personne expérimenté, 1/2/3 stele(s),  ...)')
@bot.hybrid_command(
    description="Organiser un groupe de donjon lvl 200"
    )
async def dj200(ctx: discord.context_managers,
               donjon : liste_donjon_200,
               statis : Literal[1,2,3,4,5,6,7,8,9,10],
               classe : Classe,
               date="",
               info = ""):
    contenu = dj_generique(ctx,donjon,statis,classe.name,20,date,info)
    await new_message(ctx, contenu)

@app_commands.describe(donjon='Le donjon en question',
                       classe='La classe que vous comptez jouer',
                       statis= 'Le niveau de statis',
                       date= 'La date souhaitée dans le format JJ/MM/AAAA HH:MM heure française. Exemple: "24/02/1999 23:45"',
                       info = 'Info supplémentaire (exemple: besoin d\'une eniripsa, besoin d\'une personne expérimenté, 1/2/3 stele(s),  ...)')
@bot.hybrid_command(
    description="Organiser un groupe de donjon lvl 215"
    )
async def dj215(ctx: discord.context_managers,
               donjon : liste_donjon_215,
               statis : Literal[1,2,3,4,5,6,7,8,9,10],
               classe : Classe,
               date="",
               info = ""):
    contenu = dj_generique(ctx,donjon,statis,classe.name,215,date,info)
    await new_message(ctx, contenu)

@app_commands.describe(donjon='Le donjon en question',
                       classe='La classe que vous comptez jouer',
                       statis= 'Le niveau de statis',
                       date= 'La date souhaitée dans le format JJ/MM/AAAA HH:MM heure française. Exemple: "24/02/1999 23:45"',
                       info = 'Info supplémentaire (exemple: besoin d\'une eniripsa, besoin d\'une personne expérimenté, 1/2/3 stele(s),  ...)')
@bot.hybrid_command(
    description="Organiser un groupe de donjon lvl 230"
    )
async def dj230(ctx: discord.context_managers,
               donjon : liste_donjon_230,
               statis : Literal[1,2,3,4,5,6,7,8,9,10],
               classe : Classe,
               date="",
               info = ""):
    contenu = dj_generique(ctx,donjon,statis,classe.name,230,date,info)
    await new_message(ctx, contenu)

@app_commands.describe(donjon='Le donjon en question',
                       classe='La classe que vous comptez jouer',
                       statis= 'Le niveau de statis',
                       date= 'La date souhaitée dans le format JJ/MM/AAAA HH:MM heure française. Exemple: "24/02/1999 23:45"',
                       info = 'Info supplémentaire (exemple: besoin d\'une eniripsa, besoin d\'une personne expérimenté, 1/2/3 stele(s),  ...)')
@bot.hybrid_command(
    description="Organiser un groupe de donjon lvl 245"
    )
async def dj245(ctx: discord.context_managers,
               donjon : liste_donjon_245,
               statis : Literal[1,2,3,4,5,6,7,8,9,10],
               classe : Classe,
               date="",
               info = ""):
    contenu = dj_generique(ctx,donjon,statis,classe.name,245,date,info)
    await new_message(ctx, contenu)

@bot.hybrid_command()
async def test(ctx):
    dt = ctx.interaction.created_at
    date = convert_date("24/02/1999 13:00")
    print(date)
    await ctx.send(dt.strftime("%z"))

@bot.event
async def on_reaction_add(reaction, user):
    message = reaction.message
    channel = discord.utils.get(message.guild.channels, name="commande-bot") #our channel
    if message.channel.id == channel.id: # checking if it's the same channel
        if message.author == bot.user: #checking if it's sent by the bot
            if user != bot.user:
                if reaction.emoji.name in classe_list: #checking the emoji
                    await message.edit(content = f"{message.content}\n- {user.mention}: {str.capitalize(reaction.emoji.name)}")
                    
    nb_reactions =0
    for r in message.reactions:
        nb_reactions+= r.count
    if nb_reactions >= 23:
        liste = message.mentions
        await message.clear_reactions()
        await message.edit(content = f"{message.content}\nGroupe au complet!")
        liste_mention = []
        for joueur in liste:
            liste_mention.append(bot.get_user(joueur.id).mention)
        await message.reply(f"{','.join(liste_mention)} votre donjon est prêt !")
    

@bot.event
async def on_ready():
    try:
        sync = await bot.tree.sync()
        print(f"{len(sync)} commande chargé")
    except Exception as e:
        print(e)

bot.run(token=token)