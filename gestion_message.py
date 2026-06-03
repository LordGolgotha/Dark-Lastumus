from gestion_levels import get_dj_info, delete_dj
import time

async def modif_message(message, contenu, nb_joueur,bot):
        if nb_joueur >=6:
            liste = message.mentions
            liste_mention = []
            for joueur in liste:
                liste_mention.append(bot.get_user(joueur.id).mention)
            delete_dj(message.id)
            await message.reply(f"{','.join(liste_mention)} votre donjon est prêt !")
            time.sleep(1)
            await message.edit(content=contenu,view=None)
        else:
             await message.edit(content=contenu)

def construction_message(bot,id):
        info_dj = get_dj_info(id)
        text = f"Donjon **{info_dj['donjon']}** modulé au niveau de stasis **S{info_dj['stasis']}**"
        if info_dj['date'] != "":
            text += f"le {info_dj['date']}"
        if info_dj['info'] != "":
            text += f"\n __**Info**__ : {info_dj['info']}"
        if len(info_dj['joueurs']) < 6:
             text += f"\nChoisissez votre classe"
        for j in info_dj['joueurs']:
            text += f"\n- {bot.get_user(j[0]).mention}: {str.capitalize(j[1])}"
        return text, len(info_dj['joueurs'])