from discord.ext import commands
import discord
from random import randint
import os

liste_ustre = [
        ("Ustre l'originel",0),
        ("Ustre est parmis nous",0),
        ("Hommage à Ustre",0),

        ("Ustre est jaloux de ton \"talent\"",1),
        ("C'est ça qui te tacle quoi... ",1),
        ("Donc là tu passes à coté de ça et tu es taclé·e? ...",1),
        ("Il sait pas aligner un pas devant l'autre mais toi... il te tacle? ",1),

        ("Taclé mais t'es pas stab hein? .... t'es pas stab...",2),
        ("Pourquoi tu es allé·e te coller à ça aussi...",2),
        ("Bon ben tue le si tu veux bouger",2),

        ("\"Quelqu'un pour me déustrer?\"",3),
        ("Bon en même temps... voilà quoi...",3),
        ("Ce fut un plaisir de te connaitre o7",3),
        ("J'espère pour toi que tu n'es pas stab",3),
        ("\"Une immu? Une dépha? Pitié...\"", 3),

        ("Je... euh.. allo? Tu es encore conscient",4),
        ("IL A 0 DE TACLE! ZERO, FAIT UN EFFORT!",4),
        ("Ton esquive est négative, littéralement...",4),
        ("On pensait que c'était impossible, tu l'as fait GG",4),
        ("Sans commentaire...",4),

        ("Tu n'as pas été sage, Chuck viens te tacler","chuck.png"),
        ("Ustre est un hommage a un joueur écaflip qui devait venir réanimer un autre joueur mais qui n'a pas pu car il a été taclé par un cocon sabléoptère, voici d'ou viens: Ustre",None),
        ("Là c'est bien dur de sortir, n'est-ce pas Virtu?","virtu.png"),
        ("Se faire ustre deviens rentable","rentable.png"),
        ("Vous savez, moi je ne crois pas qu'il y ai de bonne ou de mauvaise manière d'être ustre. \
        Moi si je devais résumer ma vie aujourd'hui avec vous, je dirais que c'est d'abords des rencontres.\
        Des mobs qui m'ont taclé de fou, peut-être à un moment où je ne pouvais pas, où j'était seul et stab.\
        Et c'est assez curieux de se dire que les hasards, les rencontres forgent une destinée...\
        Parce que quand on a le goût de la chose, le goût de la chose bien faite, le beau geste,\
        parfois on ne met pas cette esquive sur notre anneau, cette esquive qui nous aide à avancer.\
        Alors ça n'est pas mon cas, comme je disais là, puisque moi au contraire, j'ai pu ; \
        et je dis merci à l'esquive, je lui dis merci, je chante l'esquive, je danse l'esquive... \
        je ne suis qu'évasion! Et finalement, quand des gens me disent \" \
        Mais comment fais-tu pour avoir cette esquive? \" \
        je leur réponds très simplement que c'est ce goût de l'évasion, \
        ce goût donc qui m'a poussé aujourd'hui à entreprendre ce donjon... \
        mais demain qui sait? Peut-être simplement à me mettre au service de la communauté, à devenir placeur, sram placeur",None)
    ]

class TrollCog(commands.Cog):
    def __init__(self,bot):
        super().__init__()
        self.bot = bot
        self.liste_img_1 = list()
        self.liste_img_2 = list()
        self.liste_img_3 = list()
        self.liste_img_4 = list()
        self.liste_img_5 = list()
        self.liste_img_6 = list()

        for filename in os.listdir('./images/1'):
            if filename.endswith('.png'):
                self.liste_img_1.append(filename)
        for filename in os.listdir('./images/2'):
            if filename.endswith('.png'):
                self.liste_img_2.append(filename)
        for filename in os.listdir('./images/3'):
            if filename.endswith('.png'):
                self.liste_img_3.append(filename)
        for filename in os.listdir('./images/4'):
            if filename.endswith('.png'):
                self.liste_img_4.append(filename)

    @commands.hybrid_command(description="Bonjour?")
    async def bonjour(self, ctx):
        await ctx.send(f"Bonsoir c'est moi Lastumus, je déteste les péruches, le hockey et ma soeur. Par contre j'adore les Tacos et Ben-Chest!")


    @commands.hybrid_command(description="Ca me tacle?")
    async def ustre(self,ctx):
        r1 = randint(0, len(liste_ustre)-1)
        elem = liste_ustre[r1]
        phrase = elem[0]
        file = ""
        if elem[1] is None:
            await ctx.send(elem[0])
            return 
        elif type(elem[1]) is not int:
            file = discord.File(f"./images/{elem[1]}")
        elif elem[1] == 0:
            file=discord.File("./images/Cocon.png")
        elif elem[1] == 1:
            r2 = randint(0, len(self.liste_img_1)-1)
            file = discord.File(f"./images/1/{self.liste_img_1[r2]}")
        elif elem[1] == 2:
            r2 = randint(0, len(self.liste_img_2)-1)
            file = discord.File(f"./images/2/{self.liste_img_2[r2]}")
        elif elem[1] == 3:
            r2 = randint(0, len(self.liste_img_3)-1)
            file = discord.File(f"./images/3/{self.liste_img_3[r2]}")
        elif elem[1] == 4:
            r2 = randint(0, len(self.liste_img_4)-1)
            file = discord.File(f"./images/4/{self.liste_img_4[r2]}")
        print(f"Ustre: {phrase} | {file}")
        await ctx.send(phrase,file=file)

async def new_ustre(self, ctx):
    r = randint(0,5)
    if r == 0:
        r2 = randint(len(p_ustre_0))
        r3 = randint(len(liste_img_0))

        phrase = p_ustre_0[r2]
        file = liste_img_0[r3]



async def setup(bot):
    await bot.add_cog(TrollCog(bot))