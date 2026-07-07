from gestion_levels import get_dj_info, delete_dj, get_compo
import time

def construction_message(bot,id):
        info_dj = get_dj_info(id)
        text = f"Donjon **{info_dj['donjon']}** modulé **S{info_dj['stasis']}**"
        nb_joueur = len(info_dj['joueurs'])
        if info_dj['date'] == "invalid":
            text += f" date entrée invalide"
        elif info_dj['date'] != "":
            text += f" le <t:{info_dj['date']}:f> <t:{info_dj['date']}:R>"
        if info_dj['info'] != "":
            text += f"\n __**Info**__ : {info_dj['info']}"
        if 8 < nb_joueur < 4 :
             color = "31m"
        elif nb_joueur == 6:
            color = "32m"
        else:
            color = "33m"
        text += f"\nChoisissez votre classe :"
        text += f"\n```ansi\n\u001b[1;{color}{nb_joueur}/{info_dj['nb_joueur']} joueurs\u001b[0m```"
        for j in info_dj['joueurs']:
            text += f"\n- {bot.get_user(j[0]).mention}: {str.capitalize(j[1])} {get_compo(id,j[0])}"
        return text