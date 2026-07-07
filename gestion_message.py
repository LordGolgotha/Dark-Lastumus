from gestion_levels import get_dj_info, delete_dj, get_compo
import time

def construction_message(bot,id):
        info_dj = get_dj_info(id)
        text = f"Donjon **{info_dj['donjon']}** modulé au niveau de stasis **S{info_dj['stasis']}**"
        nb_joueur = len(info_dj['joueurs'])
        if info_dj['date'] == "invalid":
            text += f"date invalide"
        elif info_dj['date'] != "":
            text += f" le <t:{info_dj['date']}:f> <t:{info_dj['date']}:R>"
        if info_dj['info'] != "":
            text += f"\n __**Info**__ : {info_dj['info']}"
        text += f"\nChoisissez votre classe :"\
                f"\n**{nb_joueur}/{info_dj['nb_joueur']} joueurs**"
        for j in info_dj['joueurs']:
            text += f"\n- {bot.get_user(j[0]).mention}: {str.capitalize(j[1])} {get_compo(id,j[0])}"
        return text