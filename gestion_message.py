from gestion_levels import get_dj_info, delete_dj, get_compo
from liste_donjon import emoji_classe_map

ROUGE = "31m"
VERT = "32m"
ORANGE = "33m"

def construction_message(bot,id):
        info_dj = get_dj_info(id)
        text = f"ID donjon: {id} \nDonjon **{info_dj['donjon']}** modulé **S{info_dj['stasis']}**"
        nb_joueur = len(info_dj['joueurs'])
        nb_joueur_max = info_dj['nb_joueur']
        nb_joueur_mid = nb_joueur_max // 2

        # Display additional info if available
        if info_dj['date'] == "invalid":
            text += f" date entrée invalide"
        elif info_dj['date'] != "":
            text += f" le <t:{info_dj['date']}:f> <t:{info_dj['date']}:R>"
        if info_dj['info'] != "":
            text += f"\n __**Info**__ : {info_dj['info']}"
        
        # Color coding based on the number of players
        if nb_joueur_max < nb_joueur < nb_joueur_mid+1:
             color = ORANGE
        elif nb_joueur == nb_joueur_max:
            color = VERT
        else:
            color = ROUGE

        # Display the number of players and their classes
        text += f"\nChoisissez votre classe :"
        text += f"\n```ansi\n\u001b[1;{color}{nb_joueur}/{nb_joueur_max} joueurs\u001b[0m```"
        for j in info_dj['joueurs']:
            text += f"\n- {bot.get_user(int(j)).mention}: {emoji_classe_map.get(info_dj['joueurs'][j])} {get_compo(id,j)}"
        return text