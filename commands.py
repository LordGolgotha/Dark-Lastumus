import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
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


"""@bot.event
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
                    await message.edit(content=text)"""

@bot.event
async def on_ready():
    try:
        sync = await bot.tree.sync()
        print(f"{len(sync)} commande chargé")
    except Exception as e:
        print(e)

bot.run(token=token)