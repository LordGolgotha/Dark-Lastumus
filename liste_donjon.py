from typing import Literal

list_levels = Literal[20,35,50,65,80,95,110,125,140,155,170,185,200,215,230,245]

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

donjons_data = {
    20: [
        ("Pâturages Des Bouftous", "https://wakfu.guide/donjons/1-20/#p%C3%A2turages-des-bouftous", 6),
        ("Le Tofulailler", "https://wakfu.guide/donjons/1-20/#le-tofulailler", 6),
        ("Larventura", "https://wakfu.guide/donjons/1-20/#larventura", 6),
        ("Tournée 20", "https://wakfu.guide/donjons/1-20", 6),
    ],
    35: [
        ("Donjon des Abraknes", "https://wakfu.guide/donjons/21-35/#donjon-des-abraknes", 6),
        ("Le Caveau Relevé", "https://wakfu.guide/donjons/21-35/#le-caveau-relev%C3%A9", 6),
        ("Piou Lahoupe", "https://wakfu.guide/donjons/21-35/#piou-lahoupe", 6),
        ("Tournée 35", "https://wakfu.guide/donjons/21-35/", 6),
    ],
    50: [
        ("Le Papaturage Royal", "https://wakfu.guide/donjons/36-50/#le-papaturage-royal", 6),
        ("La Montagne Adezieu", "https://wakfu.guide/donjons/36-50/#la-montagne-adezieu", 6),
        ("Donjon Equipage Du Poulpe", "https://wakfu.guide/donjons/36-50/#donjon-equipage-du-poulpe", 6),
        ("Les Champs Pourchan", "https://wakfu.guide/donjons/36-50/#les-champs-pourchan", 6),
        ("Donjon Morts-Brûlés", "https://wakfu.guide/donjons/36-50/#donjon-morts-br%C3%BBl%C3%A9s", 6),
        ("La Tour Minérale 50", "https://wakfu.guide/donjons/36-50/#la-tour-min%C3%A9rale", 3),
        ("Tournée 50", "https://wakfu.guide/donjons/36-50/", 6),
    ],
    65: [
        ("L'Antre Oubliée", "https://wakfu.guide/donjons/51-65/#lantre-oubli%C3%A9e", 6),
        ("Donjon Bwork", "https://wakfu.guide/donjons/51-65/#donjon-bwork", 6),
        ("La Skouale Séchée", "https://wakfu.guide/donjons/51-65/#la-skouale-s%C3%A9ch%C3%A9e", 6),
        ("Donjon Mollusky", "https://wakfu.guide/donjons/51-65/#donjon-mollusky", 6),
        ("Kokokolantha", "https://wakfu.guide/donjons/51-65/#kokokolantha", 6),
        ("Château des Cwabes", "https://wakfu.guide/donjons/51-65/#ch%C3%A2teau-des-cwabes", 6),
        ("Donjon Marteaux-Aigris", "https://wakfu.guide/donjons/51-65/#donjon-marteaux-aigris", 6),
        ("Tour des Miss Moches", "https://wakfu.guide/donjons/51-65/#tour-des-miss-moches", 3),
        ("Tournée 65", "https://wakfu.guide/donjons/51-65/", 6),
    ],
    80: [
        ("Les Ratacombes", "https://wakfu.guide/donjons/66-80/#les-ratacombes", 6),
        ("La Corbeau-Cave", "https://wakfu.guide/donjons/66-80/#la-corbeau-cave", 6),
        ("Domaine du Petit Groin", "https://wakfu.guide/donjons/66-80/#domaine-du-petit-groin", 6),
        ("Palais du Tsu", "https://wakfu.guide/donjons/66-80/#palais-du-tsu", 6),
        ("Donjon Mulou", "https://wakfu.guide/donjons/66-80/#donjon-mulou", 6),
        ("Antre d'Excarnus", "https://wakfu.guide/donjons/66-80/#antre-dexcarnus", 6),
        ("Donjon Arakne", "https://wakfu.guide/donjons/66-80/#donjon-arakne", 6),
        ("Truchière Abandonnée", "https://wakfu.guide/donjons/66-80/#truchi%C3%A8re-abandonn%C3%A9e", 6),
        ("Temple du grand Orrok", "https://wakfu.guide/donjons/66-80/#temple-du-grand-orrok", 6),
        ("Tournée 80", "https://wakfu.guide/donjons/66-80/", 6),
    ],
    95: [
        ("Le Hammamamoule", "https://wakfu.guide/donjons/81-95/#le-hammamamoule", 6),
        ("Sliptorium", "https://wakfu.guide/donjons/81-95/#sliptorium", 6),
        ("Le Misolée", "https://wakfu.guide/donjons/81-95/#le-misol%C3%A9e", 6),
        ("Scarrière Abandonnée", "https://wakfu.guide/donjons/81-95/#scarri%C3%A8re-abandonn%C3%A9e", 6),
        ("Caverne des Slekymoses", "https://wakfu.guide/donjons/81-95/#caverne-des-slekymoses", 6),
        ("Château de Wagnar", "https://wakfu.guide/donjons/81-95/#ch%C3%A2teau-de-wagnar", 6),
        ("Académie Trool", "https://wakfu.guide/donjons/81-95/#acad%C3%A9mie-trool", 3),
        ("Nécropoil de Morbax", "https://wakfu.guide/donjons/81-95/#n%C3%A9cropoil-de-morbax", 6),
        ("Antre du Meulou", "https://wakfu.guide/donjons/81-95/#antre-du-meulou", 6),
        ("Tournée 95", "https://wakfu.guide/donjons/81-95/", 6),  
    ],
    110: [
        ("Le Glaglacier Cornu", "https://wakfu.guide/donjons/96-110/#le-glaglacier-cornu", 6),
        ("Niche du Yech'Ti'Wawa", "https://wakfu.guide/donjons/96-110/#niche-du-yechtiwawa", 6),
        ("Repaire des Magik Riktus", "https://wakfu.guide/donjons/96-110/#repaire-des-magik-riktus", 6),
        ("Chuchobase", "https://wakfu.guide/donjons/96-110/#chuchobase", 6),
        ("Repaire des Super-Vilains", "https://wakfu.guide/donjons/96-110/#repaire-des-super-vilains", 3),
        ("L'Arène Dansante", "https://wakfu.guide/donjons/96-110/#lar%C3%A8ne-dansante", 6),
        ("Donjon Gelée", "https://wakfu.guide/donjons/96-110/#donjon-gel%C3%A9e", 6),
        ("Antre du Corbeau Noir", "https://wakfu.guide/donjons/96-110/#antre-du-corbeau-noir", 6),
        ("Antre du Boufrog", "https://wakfu.guide/donjons/96-110/#antre-du-boufrog", 6),
        ("Tournée 110", "https://wakfu.guide/donjons/96-110/", 6),  
    ],
    125: [
        ("Le pot d'Hagen-Glass", "https://wakfu.guide/donjons/111-125/#le-pot-dhagen-glass", 6),
        ("Donjon flaqueux", "https://wakfu.guide/donjons/111-125/#donjon-flaqueux", 6),
        ("Caverne Smarrante", "https://wakfu.guide/donjons/111-125/#caverne-smarrante", 6),
        ("Fosse du Tourmenteur", "https://wakfu.guide/donjons/111-125/#fosse-du-tourmenteur", 3),
        ("Donjon Cacterre", "https://wakfu.guide/donjons/111-125/#donjon-cacterre", 6),
        ("La Tour Gelée 125", "https://wakfu.guide/donjons/111-125/#la-tour-gel%C3%A9e", 6),
        ("Aile de L'Ambassadrice", "https://wakfu.guide/donjons/111-125/#aile-de-lambassadrice", 6),
        ("La Pichine", "https://wakfu.guide/donjons/111-125/#la-pichine", 6),
        ("Antre du Dragon-Cochon", "https://wakfu.guide/donjons/111-125/#antre-du-dragon-cochon", 6),
        ("Tournée 125", "https://wakfu.guide/donjons/111-125/", 6),  
    ],
    140: [
        ("Domaine de la Trouffe Salée", "https://wakfu.guide/donjons/126-140/#domaine-de-la-trouffe-sal%C3%A9e", 6),
        ("Donjon Noirespore", "https://wakfu.guide/donjons/126-140/#donjon-noirespore", 6),
        ("Sanctuaire de Mihmol", "https://wakfu.guide/donjons/126-140/#sanctuaire-de-mihmol", 3),
        ("Donjon Abraknyde", "https://wakfu.guide/donjons/126-140/#donjon-abraknyde", 6),
        ("Compost du grand Potofeu", "https://wakfu.guide/donjons/126-140/#compost-du-grand-potofeu", 6),
        ("Palais Lenald", "https://wakfu.guide/donjons/126-140/#palais-lenald", 6),
        ("Jawdin de la Weine", "https://wakfu.guide/donjons/126-140/#jawdin-de-la-weine", 6),
        ("Tournée 140", "https://wakfu.guide/donjons/126-140/", 6),  
    ],
    155: [
        ("Le Vignoble Ignoble", "https://wakfu.guide/donjons/141-155/#le-vignoble-ignoble", 6),
        ("Donjon Srambad", "https://wakfu.guide/donjons/141-155/#donjon-srambad", 6),
        ("Donjon Enutrosor", "https://wakfu.guide/donjons/141-155/#donjon-enutrosor", 6),
        ("Donjon Blopéra", "https://wakfu.guide/donjons/141-155/#donjon-blop%C3%A9ra", 6),
        ("Source du Mal", "https://wakfu.guide/donjons/141-155/#source-du-mal", 6),
        ("Donjon Sabléoptère", "https://wakfu.guide/donjons/141-155/#donjon-sabl%C3%A9opt%C3%A8re", 6),
        ("Laboratoire de Womewo", "https://wakfu.guide/donjons/141-155/#laboratoire-de-womewo", 6),
        ("Château du Wa Wabbit", "https://wakfu.guide/donjons/141-155/#ch%C3%A2teau-du-wa-wabbit", 3),
        ("Tal Kasha", "https://wakfu.guide/talkasha/", 6),
        ("Tournée 155", "https://wakfu.guide/donjons/141-155/", 6),  
    ],
    170: [
        ("Donjon Patapoutrerie", "https://wakfu.guide/donjons/156-170/#donjon-patapoutrerie", 6),
        ("Donjon Lampionaute", "https://wakfu.guide/donjons/156-170/#donjon-lampionaute", 6),
        ("Donjon Roub Bar", "https://wakfu.guide/donjons/156-170/#donjon-roub-bar", 6),
        ("Donjon Riktus Elite", "https://wakfu.guide/donjons/156-170/#donjon-riktus-elite", 6),
        ("Donjon E-Bou", "https://wakfu.guide/donjons/156-170/#donjon-e-bou", 6),
        ("Fabrique Méka", "https://wakfu.guide/donjons/156-170/#fabrique-m%C3%A9ka", 6),
        ("Repaire de Kali", "https://wakfu.guide/donjons/156-170/#repaire-de-kali", 3),
        ("Plateau des Haut-Vents: Serre d'Acier", "https://wakfu.guide/donjons/156-170/#boss-ultime--serre-dacier", 6),
        ("Tournée 170", "https://wakfu.guide/donjons/156-170/", 6),  
    ],
    185: [
        ("Donjon des Crocodailles", "https://wakfu.guide/donjons/171-185/#donjon-des-crocodailles", 6),
        ("Donjon des Kannivores", "https://wakfu.guide/donjons/171-185/#donjon-des-kannivores", 6),
        ("Donjon des Tropikes", "https://wakfu.guide/donjons/171-185/#donjon-des-tropikes", 6),
        ("Donjon des Kannibouls", "https://wakfu.guide/donjons/171-185/#donjon-des-kannibouls", 6),
        ("Cité Interdite", "https://wakfu.guide/donjons/171-185/#cit%C3%A9-interdite", 3),
        ("Cime du Grand Totem", "https://stratfu.fr/boss_ultime/grand_totem/", 6),
        ("Tournée 185", "https://wakfu.guide/donjons/171-185/", 6),  
    ],
    200: [
        ("Sanctuaire des Dragoeufs", "https://wakfu.guide/donjons/186-200/#sanctuaire-des-dragoeufs", 6),
        ("Tombeau de Pandala", "https://wakfu.guide/donjons/186-200/#tombeau-de-pandala", 6),
        ("La Crête Givrée", "https://wakfu.guide/donjons/186-200/#la-cr%C3%AAte-givr%C3%A9e", 6),
        ("Canyon des Fléopards", "https://wakfu.guide/donjons/186-200/#canyon-des-fl%C3%A9opards", 6),
        ("Volcan Or'Hodruin", "https://wakfu.guide/donjons/186-200/#volcan-orhodruin", 6),
        ("Tanière des Blérox", "https://wakfu.guide/donjons/186-200/#tani%C3%A8re-des-bl%C3%A9rox", 6),
        ("Usine Hibourg", "https://wakfu.guide/donjons/186-200/#usine-hibourg", 6),
        ("Ogrest 200", "https://wakfu.guide/ogrest/", 6),  
        ("Antre de Nogord l'Ezarélé", "https://methodwakfu.com/pvm/boss-ultimes/antre-de-nogord-l-ezarele/", 6),  
        ("Dimension-Objet d'Ombrage", "https://methodwakfu.com/pvm/boss-ultimes/dimension-objet-dombrage/", 6),  
        ("Tour Minérale 200", "https://wakfu.guide/donjons/186-200/#tour-min%C3%A9rale", 3),
        ("Tournée 200", "https://wakfu.guide/donjons/186-200/", 6),  
    ],
    215: [
        ("Donjon Carapattes", "https://wakfu.guide/donjons/201-215/#donjon-carapattes", 6),
        ("Donjon Plantigardes", "https://wakfu.guide/donjons/201-215/#donjon-plantigardes", 6),
        ("Donjon Mansots", "https://wakfu.guide/donjons/201-215/#donjon-mansots", 6),
        ("Donjon Vandaliénés", "https://wakfu.guide/donjons/201-215/#donjon-vandali%C3%A9n%C3%A9s", 6),
        ("Donjon Crustargneux", "https://wakfu.guide/donjons/201-215/#donjon-crustargneux", 6),
        ("Donjon Cagnardeurs", "https://wakfu.guide/donjons/201-215/#donjon-cagnardeurs", 6),
        ("Donjon Toundrasoirs", "https://wakfu.guide/donjons/201-215/#donjon-toundrasoirs", 6),
        ("Donjon Tour Minérale 215", "https://wakfu.guide/donjons/201-215/#donjon-tour-min%C3%A9rale-215", 3),
        ("Ogrest 215", "https://wakfu.guide/ogrest/", 6),  
        ("Tournée 215", "https://wakfu.guide/donjons/201-215/", 6),  
    ],
    230: [
        ("Donjon Phytomorphe", "https://wakfu.guide/donjons/216-230/#donjon-phytomorphe", 6),
        ("Donjon Vidéants", "https://wakfu.guide/donjons/216-230/#donjon-vid%C3%A9ants", 6),
        ("Donjon Démhorribles", "https://wakfu.guide/donjons/216-230/#donjon-d%C3%A9mhorribles", 6),
        ("Donjon Vidéants", "https://wakfu.guide/donjons/216-230/#donjon-vid%C3%A9ants", 6),
        ("Ogrest 230", "https://wakfu.guide/ogrest/", 6),  
        ("Donjon Égarés", "https://stratfu.fr/230/egare/", 6),  
        ("Donjon Ravageurs", "https://stratfu.fr/230/ravageur/", 6),  
        ("Palais de Rushu", "", 6),  #TODO inexistant
        ("Nécromonde", "https://stratfu.fr/230/necrome/", 3),  
        ("Donjon Steamers", "https://stratfu.fr/230/steam/", 6),  
        ("Donjon Poisseux abyssaux", "https://stratfu.fr/230/poisseux/", 6),  
        ("Tournée 230", "https://stratfu.fr", 6),  
    ],
    245: [
        ("Théatre intemporel", "https://stratfu.fr/245/theatre/", 6),  
        ("Donjon Machine de Nox", "https://stratfu.fr/245/machine_nox/", 6),  
        ("Donjon Clan de Bworkana", "https://stratfu.fr/245/clan_bworkana/", 6),  
        ("Donjon Savanastraux", "https://stratfu.fr/245/savane", 6),  
        ("Donjon Primassifs", "https://stratfu.fr/245/prima/", 6),  
        ("Donjon Férociraptors", "https://stratfu.fr/245/fero/", 6),  
        ("Coeur de l'horloge de Nox", "", 6),  #TODO inexistant
        ("Tournée 245", "https://stratfu.fr", 6),  
    ],
}

donjon_link_map = {}
donjon_level_map = {}
donjon_nb_joueur_map = {}

for level, data in donjons_data.items():
    names = tuple(d[0] for d in data)
    vars()[f"liste_donjon_{level}"] = Literal.__getitem__(names)
    donjon_level_map[level] = vars()[f"liste_donjon_{level}"]
    for name, link, nb_j in data:
        donjon_link_map[name] = link
        donjon_nb_joueur_map[name] = nb_j

emoji_classe_map = {}
for i in range(len(classe_list)):
    emoji_classe_map[classe_list[i]] = f"{emoji_list[i]} {classe_list[i]}"