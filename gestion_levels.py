from pymongo_get_database import get_database
dbname = get_database('Level')
collection_opti = dbname["opti"]
collection_low_cost = dbname["low_cost"]

def set_opti(pseudo,classe,levels : set):
    collection = collection_opti
    set_level(pseudo, classe, levels, collection)

def set_low_cost(pseudo,classe,levels : set):
    collection = collection_low_cost
    set_level(pseudo, classe, levels, collection)

def set_level(pseudo,classe,levels : set,collection):
    #print(f"Ajout des levels {levels} pour la classe {classe} de {pseudo}\n")
    player = collection.find_one({"_id" : pseudo})
    if player == None:
        player = {
            "_id" : pseudo,
            "levels" : {classe : list(levels)}
        }
        collection.insert_one(player)
    else:
        new_dict_player = dict()
        ret, new_dict_player = modif_list(classe, levels, player)
        if not ret:
            print(f"La classe {classe} a été ajouté au joueur {pseudo} avec les levels: {levels}")
            new_dict_player[classe] = list(levels)
        #print(f"Les anciennes données étaient: {ancienne_data} \n Les nouvelles données sont: {new_dict_player}\n")
        collection.update_one({"_id" : pseudo}, {'$set': {"levels" : new_dict_player}}, upsert= True)

def modif_list(classe, levels, player):
    modif = False
    new_dict_player = dict()
    for player_classe in player['levels']:
        if player_classe != classe:
            new_dict_player[player_classe] = player['levels'][player_classe]
        else:
            modif = True
            temp = player['levels'][player_classe]
            res = set(temp) | set(levels)
            new_dict_player[player_classe] = list(res)
    return modif, new_dict_player

def get_low_cost(level:int):
    return get_level(level,collection_low_cost.find())

def get_opti(level:int):
    return get_level(level,collection_opti.find())

def get_stuffer(level:int):
    low_cost = get_low_cost(level)
    print(f"Les joueurs low cost {level} sont : {low_cost}")
    opti = get_opti(level)
    print(f"Les joueurs opti {level} sont : {opti}")
    res = dict()
    keys = set(low_cost) | set(opti)
    for player in keys:
        if player in opti and player in low_cost:
            res[player] = set(low_cost[player]) | set(opti[player])
        elif player in opti:
            res[player] = opti[player]
        else:
            res[player] = low_cost[player]
    print(f"Les joueurs stuffer sont {res}")
    return res

def get_level(level:int, collection):
    players = collection
    res = dict()
    for player in players:
        all_class_player = set()
        for classe in player["levels"]:
            if predicat_opti_classe(level, player['levels'][classe]):
                all_class_player.add(classe)
        if len(all_class_player) !=0:
            #print(f"Le player {player['_id']} a au moins une classe opti au niveau {level}")
            res[player["_id"]] = list(all_class_player)
    return res

def predicat_opti_classe(level, classe) -> bool:
    for classe_level in classe:
        if classe_level == level:
            return True
    return False

def del_opti(pseudo,classe,level: int):
    del_level(pseudo,classe,level,collection_opti)

def del_low_cost(pseudo,classe,level: int):
    del_level(pseudo,classe,level,collection_low_cost)

def del_level(pseudo,classe,level:int,collection):
    player = collection.find_one({"_id" : pseudo})
    if player == None:
        return False
    else:
        new_dict_player = dict()
        for player_classe in player['levels']:
            print(f"{player_classe} & {classe}")
            if classe in player_classe:
                player['levels'][player_classe].remove(level)
                print(player['levels'][player_classe])
            new_dict_player[player_classe] = player['levels'][player_classe].copy()
    collection.update_one({"_id" : pseudo}, {'$set': {"levels" : new_dict_player}})
    print(f"Suppression du level {level} pour la class {classe} de {pseudo}")
    


if __name__ == "__main__":
    #print(predicat_opti_classe(200,))
    #print(get_opti(200))
    set_opti("Lord","Huppermage <:huppermage:1483790462593794190>",[200,215,110])
    set_opti("Lord","Ouginak <:ouginak:1483790467639410698>",[200,65,20,110])
    set_opti("Lordgougougaga","Ouginak <:ouginak:1483790467639410698>",[200,215,185])
    set_opti("Lordgougougaga","Cra <:cra:1483790476959289434>",[185,215,20,50])
    set_low_cost("Lordgougougaga","Cra <:cra:1483790476959289434>",[185,215,65,50])
    del_low_cost("Lordgougougaga","Cra",185)
    del_opti("Lordgougougaga","Cra",185)