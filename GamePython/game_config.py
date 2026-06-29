# Configuration du RPG Text-Based

GAME_CONFIG = {
    "title": "GamePython - RPG Adventure",
    "starting_location": "forest",
    "player_stats": {
        "health": 100,
        "max_health": 100,
        "mana": 50,
        "max_mana": 50,
        "level": 1,
        "exp": 0,
        "exp_for_next_level": 100,
        "gold": 0,
        "attack": 5,
        "defense": 0,
        "armor": 0,
        "weapon": "Mains nues",
        "armor_stat": 0
    }
}

# Systeme de classes
CLASSES = {
    "Guerrier": {
        "description": "Fort et robuste. Excelle en combat direct.",
        "base_stats": {
            "health": 120,
            "max_health": 120,
            "attack": 8,
            "defense": 3,
            "mana": 30,
            "max_mana": 30
        },
        "bonus": "+2 Defense, +1 Attack par niveau",
        "skill": "Coup Puissant - Double dégâts, coûte 20 mana"
    },
    "Mage": {
        "description": "Contrôle la magie. Puissantes attaques à distance.",
        "base_stats": {
            "health": 70,
            "max_health": 70,
            "attack": 3,
            "defense": 0,
            "mana": 100,
            "max_mana": 100
        },
        "bonus": "+2 Mana, +0.5 Attack par niveau",
        "skill": "Éclair - Dégâts haute, coûte 25 mana"
    },
    "Archer": {
        "description": "Rapide et précis. Équilibre entre force et agilité.",
        "base_stats": {
            "health": 90,
            "max_health": 90,
            "attack": 6,
            "defense": 1,
            "mana": 50,
            "max_mana": 50
        },
        "bonus": "+1.5 Attack, +1 Mana par niveau",
        "skill": "Tir Rapide - 2 attaques rapides, coûte 15 mana"
    }
}

# Systeme de competences par classe
SKILLS = {
    "Guerrier": {
        "Coup Puissant": {
            "description": "Attaque double avec vos deux armes",
            "mana_cost": 20,
            "damage_multiplier": 2.0,
            "icon": "⚔️",
            "unlocked_at": 1
        },
        "Défense Renforcée": {
            "description": "Augmente votre défense temporairement (+5 DEF, 3 tours)",
            "mana_cost": 15,
            "defense_boost": 5,
            "duration": 3,
            "icon": "🛡️",
            "unlocked_at": 1
        }
    },
    "Mage": {
        "Éclair": {
            "description": "Attaque magique puissante (1.8x dégâts)",
            "mana_cost": 25,
            "damage_multiplier": 1.8,
            "icon": "⚡",
            "unlocked_at": 1
        },
        "Soin": {
            "description": "Restaure 60 points de santé",
            "mana_cost": 30,
            "heal": 60,
            "icon": "💚",
            "unlocked_at": 1
        }
    },
    "Archer": {
        "Tir Rapide": {
            "description": "Deux attaques rapides (1.5x dégâts chacune)",
            "mana_cost": 15,
            "damage_multiplier": 1.5,
            "hits": 2,
            "icon": "🏹",
            "unlocked_at": 1
        },
        "Esquive": {
            "description": "Réduit les dégâts reçus (temporaire)",
            "mana_cost": 10,
            "damage_reduction": 0.5,
            "duration": 2,
            "icon": "💨",
            "unlocked_at": 1
        }
    }
}

# Compétences débloquables par niveau - Ajoutées au-delà des compétences de base
PROGRESSIVE_SKILLS = {
    "Guerrier": [
        {
            "name": "Charge Furieuse",
            "level": 3,
            "description": "Fonce sur l'ennemi pour 2.5x dégâts",
            "mana_cost": 25,
            "damage_multiplier": 2.5,
            "icon": "🔥"
        },
        {
            "name": "Berserk",
            "level": 5,
            "description": "Triple votre attaque pendant 2 tours (coûte 35 mana)",
            "mana_cost": 35,
            "attack_multiplier": 3,
            "duration": 2,
            "icon": "💢"
        },
        {
            "name": "Contre-Attaque",
            "level": 8,
            "description": "Riposte automatique si ennemi vous frappe (50% dégâts)",
            "mana_cost": 20,
            "counter_damage_percent": 0.5,
            "duration": 3,
            "icon": "⚔️⚔️"
        },
        {
            "name": "Coup Mortel",
            "level": 12,
            "description": "Attaque spéciale avec 3x dégâts",
            "mana_cost": 40,
            "damage_multiplier": 3.0,
            "icon": "💀"
        }
    ],
    "Mage": [
        {
            "name": "Boule de Feu",
            "level": 3,
            "description": "Explose autour de l'ennemi pour 2x dégâts",
            "mana_cost": 30,
            "damage_multiplier": 2.0,
            "icon": "🔥🔥"
        },
        {
            "name": "Glaciation",
            "level": 5,
            "description": "Gèle l'ennemi et réduit son attaque (40% ATK moins, 2 tours)",
            "mana_cost": 28,
            "enemy_attack_reduction": 0.4,
            "duration": 2,
            "icon": "❄️"
        },
        {
            "name": "Téléportation",
            "level": 8,
            "description": "Évite tous les dégâts du prochain tour",
            "mana_cost": 25,
            "evasion_duration": 1,
            "icon": "✨"
        },
        {
            "name": "Météorite",
            "level": 12,
            "description": "Invoque une météorite pour 3.5x dégâts",
            "mana_cost": 50,
            "damage_multiplier": 3.5,
            "icon": "☄️"
        }
    ],
    "Archer": [
        {
            "name": "Tir Perçant",
            "level": 3,
            "description": "Flèche qui ignore 30% de la défense de l'ennemi",
            "mana_cost": 18,
            "damage_multiplier": 1.8,
            "armor_penetration": 0.3,
            "icon": "🏹🏹"
        },
        {
            "name": "Pluie de Flèches",
            "level": 5,
            "description": "Lance 5 flèches pour 1.2x dégâts chacune",
            "mana_cost": 32,
            "damage_multiplier": 1.2,
            "hits": 5,
            "icon": "🌧️"
        },
        {
            "name": "Volée Explosive",
            "level": 8,
            "description": "Flèches explosives pour 2.2x dégâts",
            "mana_cost": 28,
            "damage_multiplier": 2.2,
            "hits": 2,
            "icon": "💥"
        },
        {
            "name": "Tir de Précision",
            "level": 12,
            "description": "Coup critique garanti pour 4x dégâts",
            "mana_cost": 45,
            "damage_multiplier": 4.0,
            "critical": True,
            "icon": "🎯"
        }
    ]
}


# Systeme de quetes quotidiennes
DAILY_QUESTS = {
    "Tueur de Gobelins": {
        "description": "Vaincre 5 Gobelins",
        "target_enemy": "Gobelin",
        "target_count": 5,
        "reward_exp": 500,
        "reward_gold": 100,
        "reward_item": None,
        "icon": "🐢"
    },
    "Chasseur de Loups": {
        "description": "Vaincre 3 Loups",
        "target_enemy": "Loup",
        "target_count": 3,
        "reward_exp": 400,
        "reward_gold": 80,
        "reward_item": None,
        "icon": "🐺"
    },
    "Tueur d'Orcs": {
        "description": "Vaincre 4 Orcs",
        "target_enemy": "Orc",
        "target_count": 4,
        "reward_exp": 600,
        "reward_gold": 120,
        "reward_item": None,
        "icon": "👹"
    },
    "Collectionneur de Pièces": {
        "description": "Amasser 500 or",
        "type": "gold",
        "target_gold": 500,
        "reward_exp": 300,
        "reward_gold": 50,
        "reward_item": "Potion Santé Majeure",
        "icon": "💰"
    },
    "Aventurier Expérimenté": {
        "description": "Gagner 1000 XP",
        "type": "exp",
        "target_exp": 1000,
        "reward_exp": 500,
        "reward_gold": 200,
        "reward_item": None,
        "icon": "⭐"
    },
    "Chasseur de Dragons": {
        "description": "Vaincre 2 Dragons",
        "target_enemy": "Dragon",
        "target_count": 2,
        "reward_exp": 1000,
        "reward_gold": 300,
        "reward_item": "Potion Protection",
        "icon": "🐉"
    }
}

# Configuration des niveaux de difficulte
DIFFICULTY_SETTINGS = {
    "facile": {
        "max_level_offset": 2,
        "description": "Ennemis faibles (+1 à +2 de votre niveau)"
    },
    "moyen": {
        "max_level_offset": 5,
        "description": "Ennemis equilibres (+0 à +5 de votre niveau)"
    },
    "difficile": {
        "max_level_offset": 8,
        "description": "Ennemis forts (+0 à +8 de votre niveau)"
    }
}

# Systeme de loot avec probabilites
LOOT_TABLE = {
    "commun": 0.50,      # 50%
    "rare": 0.30,        # 30%
    "epique": 0.15,      # 15%
    "legendaire": 0.05   # 5%
}

# Items par rareté pour le loot
LOOT_BY_RARITY = {
    "commun": [
        "Épée de Fer",
        "Arc Longue Portée",
        "Bâton de Mana",
        "Armure Cuir",
        "Potion Santé",
        "Potion Mana"
    ],
    "rare": [
        "Hache de Bataille",
        "Arc de Chasse",
        "Bâton Flamboyant",
        "Armure de Fer",
        "Potion Santé Majeure",
        "Potion Mana Majeure",
        "Potion Force",
        "Potion Protection"
    ],
    "epique": [
        "Marteau de Guerre",
        "Arc Élémental",
        "Bâton du Sage",
        "Armure Dragon",
        "Potion Force",
        "Potion Protection"
    ],
    "legendaire": [
        "Épée de Feu",
        "Éclair Éternel"
    ]
}

# Items du jeu - Organisés par classe et rareté
ITEMS = {
    # ARMES GUERRIER
    "Épée de Fer": {
        "type": "weapon",
        "attack_bonus": 7,
        "class": "Guerrier",
        "rarity": "commun",
        "price": 80,
        "description": "Épée standard pour guerrier"
    },
    "Hache de Bataille": {
        "type": "weapon",
        "attack_bonus": 10,
        "class": "Guerrier",
        "rarity": "rare",
        "price": 150,
        "description": "Hache puissante pour combat rapproché"
    },
    "Marteau de Guerre": {
        "type": "weapon",
        "attack_bonus": 12,
        "class": "Guerrier",
        "rarity": "epique",
        "price": 250,
        "description": "Écrase les ennemis"
    },
    
    # ARMES MAGE
    "Bâton de Mana": {
        "type": "weapon",
        "attack_bonus": 4,
        "mana_bonus": 20,
        "class": "Mage",
        "rarity": "commun",
        "price": 80,
        "description": "Amplifie la magie"
    },
    "Bâton Flamboyant": {
        "type": "weapon",
        "attack_bonus": 8,
        "mana_bonus": 40,
        "class": "Mage",
        "rarity": "rare",
        "price": 150,
        "description": "Lance des feux puissants"
    },
    "Bâton du Sage": {
        "type": "weapon",
        "attack_bonus": 12,
        "mana_bonus": 60,
        "class": "Mage",
        "rarity": "epique",
        "price": 250,
        "description": "Ancien bâton de grand pouvoir"
    },
    
    # ARMES ARCHER
    "Arc Longue Portée": {
        "type": "weapon",
        "attack_bonus": 6,
        "class": "Archer",
        "rarity": "commun",
        "price": 80,
        "description": "Arc de chasseur"
    },
    "Arc de Chasse": {
        "type": "weapon",
        "attack_bonus": 9,
        "class": "Archer",
        "rarity": "rare",
        "price": 150,
        "description": "Arc parfaitement équilibré"
    },
    "Arc Élémental": {
        "type": "weapon",
        "attack_bonus": 13,
        "class": "Archer",
        "rarity": "epique",
        "price": 250,
        "description": "Flèches en feu et glaçon"
    },
    
    # ARMURES
    "Armure Cuir": {
        "type": "armor",
        "defense_bonus": 2,
        "price": 40,
        "description": "Armure légère en cuir"
    },
    "Armure de Fer": {
        "type": "armor",
        "defense_bonus": 5,
        "rarity": "commun",
        "price": 100,
        "description": "Armure solide en fer"
    },
    "Armure Dragon": {
        "type": "armor",
        "defense_bonus": 10,
        "rarity": "epique",
        "price": 300,
        "description": "Armure faite de peau de dragon"
    },
    "Armure Céleste": {
        "type": "armor",
        "defense_bonus": 15,
        "rarity": "legendaire",
        "price": 500,
        "description": "Armure des anges"
    },
    
    # CONSOMMABLES
    "Potion Santé": {
        "type": "consumable",
        "heal": 50,
        "rarity": "commun",
        "price": 20,
        "description": "Restaure 50 points de santé"
    },
    "Potion Santé Majeure": {
        "type": "consumable",
        "heal": 150,
        "rarity": "rare",
        "price": 50,
        "description": "Restaure 150 points de santé"
    },
    "Potion Mana": {
        "type": "consumable",
        "mana": 30,
        "rarity": "commun",
        "price": 25,
        "description": "Restaure 30 points de mana"
    },
    "Potion Mana Majeure": {
        "type": "consumable",
        "mana": 100,
        "rarity": "rare",
        "price": 60,
        "description": "Restaure 100 points de mana"
    },
    "Potion Force": {
        "type": "consumable",
        "attack_boost": 10,
        "duration": 3,
        "rarity": "epique",
        "price": 80,
        "description": "+10 Attack pendant 3 tours"
    },
    "Potion Protection": {
        "type": "consumable",
        "defense_boost": 10,
        "duration": 3,
        "rarity": "epique",
        "price": 80,
        "description": "+10 Defense pendant 3 tours"
    },
    
    # LÉGENDAIRES
    "Épée de Feu": {
        "type": "weapon",
        "attack_bonus": 50,
        "rarity": "legendaire",
        "class": "Guerrier",
        "price": 0,
        "description": "Épée légendaire enflammée"
    },
    "Éclair Éternel": {
        "type": "weapon",
        "attack_bonus": 40,
        "mana_bonus": 80,
        "rarity": "legendaire",
        "class": "Mage",
        "price": 0,
        "description": "Bâton du dieu de l'orage"
    },
    
    # ARMES GUERRIER SUPPLÉMENTAIRES
    "Épée Acérée": {
       "type": "weapon",
       "attack_bonus": 8,
       "class": "Guerrier",
       "rarity": "commun",
       "price": 100,
       "description": "Épée bien affûtée"
    },
    "Épée de Lumière": {
       "type": "weapon",
       "attack_bonus": 11,
       "defense_bonus": 2,
       "class": "Guerrier",
       "rarity": "rare",
       "price": 180,
       "description": "Épée sacrée brillante"
    },
    "Lame Sombre": {
       "type": "weapon",
       "attack_bonus": 14,
       "health_bonus": 20,
       "class": "Guerrier",
       "rarity": "epique",
       "price": 280,
       "description": "Lame maudite qui renforce le porteur"
    },
    "Glaive du Guerrier": {
       "type": "weapon",
       "attack_bonus": 15,
       "defense_bonus": 1,
       "class": "Guerrier",
       "rarity": "epique",
       "price": 300,
       "description": "Arme légendaire du guerrier ancien"
    },
    
    # ARMES MAGE SUPPLÉMENTAIRES
    "Bâton Glacial": {
       "type": "weapon",
       "attack_bonus": 7,
       "mana_bonus": 30,
       "defense_bonus": 1,
       "class": "Mage",
       "rarity": "rare",
       "price": 160,
       "description": "Bâton de glace éternelle"
    },
    "Sceptre Arcaniste": {
       "type": "weapon",
       "attack_bonus": 10,
       "mana_bonus": 50,
       "class": "Mage",
       "rarity": "rare",
       "price": 170,
       "description": "Sceptre des arcanes"
    },
    "Orbe de Puissance": {
       "type": "weapon",
       "attack_bonus": 13,
       "mana_bonus": 70,
       "health_bonus": 30,
       "class": "Mage",
       "rarity": "epique",
       "price": 320,
       "description": "Orbe cosmique d'une puissance infinie"
    },
    "Bâton Infernal": {
       "type": "weapon",
       "attack_bonus": 14,
       "mana_bonus": 65,
       "class": "Mage",
       "rarity": "epique",
       "price": 310,
       "description": "Bâton craché par le feu infernal"
    },
    
    # ARMES ARCHER SUPPLÉMENTAIRES
    "Arc de Précision": {
       "type": "weapon",
       "attack_bonus": 8,
       "class": "Archer",
       "rarity": "commun",
       "price": 110,
       "description": "Arc très précis"
    },
    "Arc Sylvain": {
       "type": "weapon",
       "attack_bonus": 10,
       "defense_bonus": 1,
       "class": "Archer",
       "rarity": "rare",
       "price": 160,
       "description": "Arc de la forêt ancienne"
    },
    "Arc Flamboyant": {
       "type": "weapon",
       "attack_bonus": 11,
       "health_bonus": 15,
       "class": "Archer",
       "rarity": "rare",
       "price": 175,
       "description": "Arc qui tire des flèches enflammées"
    },
    "Arc du Chasseur Légendaire": {
       "type": "weapon",
       "attack_bonus": 15,
       "defense_bonus": 2,
       "health_bonus": 25,
       "class": "Archer",
       "rarity": "epique",
       "price": 350,
       "description": "Arc du grand chasseur d'antan"
    },
    "Arc Glacé": {
       "type": "weapon",
       "attack_bonus": 14,
       "mana_bonus": 40,
       "class": "Archer",
       "rarity": "epique",
       "price": 330,
       "description": "Arc qui tire des flèches glaciales"
    },
    
    # ARMURES SUPPLÉMENTAIRES
    "Armure Légère": {
       "type": "armor",
       "defense_bonus": 3,
       "rarity": "commun",
       "price": 60,
       "description": "Armure légère et flexible"
    },
    "Armure Acier": {
       "type": "armor",
       "defense_bonus": 7,
       "rarity": "rare",
       "price": 120,
       "description": "Armure d'acier renforcé"
    },
    "Armure Mithril": {
       "type": "armor",
       "defense_bonus": 12,
       "health_bonus": 40,
       "rarity": "epique",
       "price": 350,
       "description": "Armure légendaire de mithril"
    },
    "Armure du Mage": {
       "type": "armor",
       "defense_bonus": 3,
       "mana_bonus": 50,
       "rarity": "rare",
       "price": 140,
       "description": "Tunique magique pour mage"
    },
    "Armure de Brume": {
       "type": "armor",
       "defense_bonus": 8,
       "mana_bonus": 30,
       "rarity": "epique",
       "price": 320,
       "description": "Armure spectrale de brume magique"
    },
    "Armure Abyssale": {
       "type": "armor",
       "defense_bonus": 11,
       "health_bonus": 50,
       "rarity": "epique",
       "price": 340,
       "description": "Armure noire des abysses"
    },
    "Armure Sacrée": {
       "type": "armor",
       "defense_bonus": 14,
       "health_bonus": 60,
       "rarity": "legendaire",
       "price": 600,
       "description": "Armure benedite par les dieux"
    },
    
    # ACCESSOIRES (Anneaux, Amulettes, etc.)
    "Anneau de Santé": {
       "type": "accessory",
       "health_bonus": 30,
       "rarity": "commun",
       "price": 50,
       "description": "Anneau qui augmente la vitalité"
    },
    "Anneau de Force": {
       "type": "accessory",
       "attack_bonus": 3,
       "rarity": "commun",
       "price": 60,
       "description": "Anneau qui augmente l'attaque"
    },
    "Anneau de Protection": {
       "type": "accessory",
       "defense_bonus": 3,
       "rarity": "commun",
       "price": 60,
       "description": "Anneau qui augmente la défense"
    },
    "Amulette de Mana": {
       "type": "accessory",
       "mana_bonus": 40,
       "rarity": "rare",
       "price": 120,
       "description": "Amulette qui restaure le mana"
    },
    "Anneau du Guerrier": {
       "type": "accessory",
       "attack_bonus": 5,
       "health_bonus": 25,
       "rarity": "rare",
       "price": 140,
       "description": "Anneau ancestral des guerriers"
    },
    "Anneau du Mage": {
       "type": "accessory",
       "mana_bonus": 60,
       "attack_bonus": 2,
       "rarity": "rare",
       "price": 150,
       "description": "Anneau qui amplifie la magie"
    },
    "Amulette du Chasseur": {
       "type": "accessory",
       "attack_bonus": 4,
       "defense_bonus": 2,
       "rarity": "rare",
       "price": 130,
       "description": "Amulette du chasseur de renom"
    },
    "Couronne de Pouvoir": {
       "type": "accessory",
       "attack_bonus": 8,
       "health_bonus": 50,
       "defense_bonus": 5,
       "rarity": "epique",
       "price": 400,
       "description": "Couronne qui confère puissance et prestige"
    },
    "Anneau de l'Archimage": {
       "type": "accessory",
       "mana_bonus": 100,
       "attack_bonus": 5,
       "rarity": "epique",
       "price": 420,
       "description": "Anneau du grand archimage"
    },
    "Bague de Régénération": {
       "type": "accessory",
       "health_bonus": 80,
       "rarity": "epique",
       "price": 380,
       "description": "Bague qui régénère la santé constamment"
    },
    "Anneau Infini": {
       "type": "accessory",
       "attack_bonus": 10,
       "defense_bonus": 8,
       "health_bonus": 60,
       "mana_bonus": 50,
       "rarity": "legendaire",
       "price": 800,
       "description": "Anneau qui balance tous les attributs parfaitement"
    },
    
    # CONSOMMABLES SUPPLÉMENTAIRES
    "Élixir de Vie": {
       "type": "consumable",
       "heal": 200,
       "rarity": "epique",
       "price": 120,
       "description": "Restaure 200 points de santé d'un coup"
    },
    "Élixir de Mana Cosmique": {
       "type": "consumable",
       "mana": 150,
       "rarity": "epique",
       "price": 130,
       "description": "Restaure 150 points de mana d'un coup"
    },
    "Potion Poison": {
       "type": "consumable",
       "attack_boost": 15,
       "duration": 2,
       "rarity": "rare",
       "price": 70,
       "description": "+15 Attack pendant 2 tours (toxine)"
    },
    "Potion d'Acier": {
       "type": "consumable",
       "defense_boost": 15,
       "duration": 2,
       "rarity": "rare",
       "price": 70,
       "description": "+15 Defense pendant 2 tours"
    }
}

# Systeme de magasins - Quels items vend chaque marchand
SHOPS = {
    "Marchand de potions": {
        "description": "Bienvenue! Je vends des potions magiques.",
        "items": ["Potion Santé", "Potion Mana", "Potion Santé Majeure", "Potion Mana Majeure", "Élixir de Vie", "Élixir de Mana Cosmique", "Potion Poison", "Potion d'Acier"]
    },
    "Forgeron": {
        "description": "Bienvenue dans ma forge! Voici mes meilleures créations.",
        "items": ["Épée de Fer", "Épée Acérée", "Hache de Bataille", "Marteau de Guerre", "Lame Sombre", "Glaive du Guerrier", "Armure Cuir", "Armure Légère", "Armure de Fer", "Armure Acier", "Armure Mithril", "Armure Abyssale"]
    },
    "Marchand de Magie": {
        "description": "Bienvenue! Les meilleurs bâtons magiques du royaume.",
        "items": ["Bâton de Mana", "Bâton Flamboyant", "Bâton du Sage", "Bâton Glacial", "Sceptre Arcaniste", "Orbe de Puissance", "Bâton Infernal", "Armure du Mage", "Armure de Brume", "Amulette de Mana", "Anneau du Mage", "Anneau de l'Archimage"]
    },
    "Aubergiste": {
        "description": "Bienvenue à l'auberge! Nous avons de bons produits.",
        "items": ["Potion Santé", "Potion Mana", "Potion Force", "Potion Protection", "Potion Poison", "Potion d'Acier", "Anneau de Santé", "Anneau de Force", "Anneau de Protection"]
    },
    "Marchande d'Arcs": {
        "description": "Bienvenue! Les meilleurs arcs et équipements pour archer.",
        "items": ["Arc Longue Portée", "Arc de Précision", "Arc de Chasse", "Arc Sylvain", "Arc Flamboyant", "Arc Élémental", "Arc du Chasseur Légendaire", "Arc Glacé", "Amulette du Chasseur"]
    },
    "Joaillier": {
        "description": "Bienvenue! Consultez mes bijoux extraordinaires.",
        "items": ["Anneau de Santé", "Anneau de Force", "Anneau de Protection", "Anneau du Guerrier", "Anneau du Mage", "Amulette du Chasseur", "Couronne de Pouvoir", "Anneau de l'Archimage", "Bague de Régénération", "Amulette de Mana"]
    },
    "Marchand Légendaire": {
        "description": "Bienvenue! J'ai des items très rares.",
        "items": ["Armure Dragon", "Armure Céleste", "Armure Sacrée", "Épée de Lumière", "Épée de Feu", "Éclair Éternel", "Couronne de Pouvoir", "Anneau Infini"]
    }
}

# Locations du jeu
LOCATIONS = {
    "forest": {
        "name": "Foret Sombre",
        "description": "Vous entrez dans une foret dense et mystérieuse. Les arbres sont énormes et la lumière filtre a peine.",
        "enemies": ["Goblin", "Goblin", "Loup", "Loup"],
        "npcs": ["Marchand de potions"],
        "exits": {
            "nord": "village",
            "est": "cave",
            "ouest": "river"
        },
        "x": 50,
        "y": 70
    },
    "village": {
        "name": "Village Paisible",
        "description": "Un petit village avec quelques maisons en bois. Les habitants vous regardent avec curiosité.",
        "enemies": [],
        "npcs": ["Aubergiste", "Forgeron"],
        "exits": {
            "sud": "forest",
            "est": "temple"
        },
        "x": 50,
        "y": 40
    },
    "cave": {
        "name": "Caverne Ancienne",
        "description": "Une caverne sombre et humide. Vous entendez des bruits etranges...",
        "enemies": ["Goblin Guerrier", "Goblin Guerrier", "Chauve-souris", "Chauve-souris", "Dragon Jeune"],
        "npcs": [],
        "exits": {
            "ouest": "forest",
            "bas": "treasure_room"
        },
        "x": 75,
        "y": 70
    },
    "river": {
        "name": "Riviere Magique",
        "description": "Une belle riviere avec de l'eau cristalline. L'air sent la magie.",
        "enemies": ["Nymphe Enragee", "Nymphe Enragee"],
        "npcs": ["Pecheur"],
        "exits": {
            "est": "forest",
            "nord": "waterfall"
        },
        "x": 25,
        "y": 70
    },
    "temple": {
        "name": "Temple Antique",
        "description": "Un ancien temple avec des hieroglyphes sur les murs. Une aura mystique remplit le lieu.",
        "enemies": ["Golem", "Golem", "Pretre Noir"],
        "npcs": ["Pretre Sage"],
        "exits": {
            "ouest": "village"
        },
        "x": 75,
        "y": 40
    },
    "treasure_room": {
        "name": "Chambre au Tresor",
        "description": "Vous avez trouve le tresor! L'or brille sous la faible lumiere.",
        "enemies": ["Gardien du Tresor"],
        "npcs": [],
        "exits": {
            "haut": "cave"
        },
        "x": 85,
        "y": 85
    },
    "waterfall": {
        "name": "Cascade",
        "description": "Une magnifique cascade d'eau avec un arc-en-ciel. C'est incroyablement beau.",
        "enemies": [],
        "npcs": ["Druide"],
        "exits": {
            "sud": "river"
        },
        "x": 25,
        "y": 20
    },
    "mountain": {
        "name": "Montagne Glacée",
        "description": "Une montagne imposante couverte de neige éternelle. Le vent glacial vous mord la peau.",
        "enemies": ["Loup Blanc", "Loup Blanc", "Géant des Glaces"],
        "npcs": [],
        "exits": {
            "sud": "forest",
            "est": "summit"
        },
        "x": 15,
        "y": 15
    },
    "summit": {
        "name": "Sommet de la Montagne",
        "description": "Vous atteignez le sommet! La vue sur le monde est spectaculaire. L'air est rare.",
        "enemies": ["Dragon Blanc", "Chevalier des Cieux"],
        "npcs": [],
        "exits": {
            "ouest": "mountain",
            "bas": "cloud_realm"
        },
        "x": 35,
        "y": 5
    },
    "cloud_realm": {
        "name": "Royaume des Nuages",
        "description": "Vous flottez parmi les nuages éternels. Le sol disparaît sous vos pieds.",
        "enemies": ["Élémental d'Air", "Phénix"],
        "npcs": [],
        "exits": {
            "haut": "summit",
            "bas": "valley"
        },
        "x": 50,
        "y": 5
    },
    "valley": {
        "name": "Vallée de l'Écho",
        "description": "Une vallée profonde où votre voix résonne infiniment. Des cristaux brillent sur les murs.",
        "enemies": ["Spectre", "Golem de Cristal"],
        "npcs": [],
        "exits": {
            "haut": "cloud_realm",
            "nord": "forest",
            "est": "crypt"
        },
        "x": 65,
        "y": 15
    },
    "crypt": {
        "name": "Crypte Ancienne",
        "description": "Une crypte souterraine antique. Des sépultures alignent les murs. L'air sent la mort.",
        "enemies": ["Squelette Guerrier", "Zombie", "Liche"],
        "npcs": [],
        "exits": {
            "ouest": "valley",
            "south": "underworld"
        },
        "x": 80,
        "y": 15
    },
    "underworld": {
        "name": "Monde Souterrain",
        "description": "Les entrailles de la terre. Du magma coule sur les murs. C'est incroyablement chaud.",
        "enemies": ["Démon des Flammes", "Golem de Lave"],
        "npcs": [],
        "exits": {
            "haut": "crypt",
            "est": "volcano"
        },
        "x": 80,
        "y": 30
    },
    "volcano": {
        "name": "Volcan Actif",
        "description": "Un volcan en éruption. La lave coule partout. La chaleur est insupportable.",
        "enemies": ["Dragon de Feu", "Chevalier Noir"],
        "npcs": [],
        "exits": {
            "ouest": "underworld",
            "nord": "forest"
        },
        "x": 90,
        "y": 30
    },
    "castle": {
        "name": "Château des Ombres",
        "description": "Un immense château noir qui se dresse vers le ciel. Des drapeaux déchirés flottent dans le vent.",
        "enemies": ["Garde du Château", "Assassin", "Roi des Ombres"],
        "npcs": [],
        "exits": {
            "nord": "village",
            "est": "tower"
        },
        "x": 35,
        "y": 40
    },
    "tower": {
        "name": "Tour du Mage",
        "description": "Une haute tour remplie de magie ancienne. Des ruines flottent autour d'elle.",
        "enemies": ["Mage Noir", "Golem Volant"],
        "npcs": [],
        "exits": {
            "ouest": "castle",
            "nord": "mountain"
        },
        "x": 20,
        "y": 40
    }
}

# Enemis
ENEMIES = {
    "Goblin": {
        "health": 40,
        "attack": 10,
        "defense": 2,
        "level": 1,
        "exp_reward": 50,
        "gold_reward": 10
    },
    "Loup": {
        "health": 55,
        "attack": 15,
        "defense": 4,
        "level": 2,
        "exp_reward": 75,
        "gold_reward": 20
    },
    "Goblin Guerrier": {
        "health": 65,
        "attack": 18,
        "defense": 6,
        "level": 3,
        "exp_reward": 100,
        "gold_reward": 30
    },
    "Chauve-souris": {
        "health": 35,
        "attack": 12,
        "defense": 2,
        "level": 2,
        "exp_reward": 40,
        "gold_reward": 15
    },
    "Dragon Jeune": {
        "health": 200,
        "attack": 30,
        "defense": 12,
        "level": 20,
        "exp_reward": 500,
        "gold_reward": 200
    },
    "Nymphe Enragee": {
        "health": 80,
        "attack": 18,
        "defense": 5,
        "level": 4,
        "exp_reward": 120,
        "gold_reward": 50
    },
    "Golem": {
        "health": 110,
        "attack": 22,
        "defense": 15,
        "level": 5,
        "exp_reward": 200,
        "gold_reward": 100
    },
    "Pretre Noir": {
        "health": 90,
        "attack": 20,
        "defense": 8,
        "level": 5,
        "exp_reward": 150,
        "gold_reward": 80
    },
    "Gardien du Tresor": {
        "health": 180,
        "attack": 28,
        "defense": 12,
        "level": 25,
        "exp_reward": 500,
        "gold_reward": 500
    }
}

# Messages des NPCs
NPCS_DIALOGUE = {
    "Marchand de potions": "Bonjour! Je vends des potions de sante. Voulez-vous une potion pour 20 pieces d'or?",
    "Aubergiste": "Bienvenue a l'auberge! Reposez-vous ici. Cela vous restaure completement pour 30 or.",
    "Forgeron": "Je peux forger une meilleure arme pour vous! Ca vous coutera 100 or.",
    "Pecheur": "La peche est bonne aujourd'hui. Pourquoi ne pas vous asseoir un moment?",
    "Pretre Sage": "La sagesse vient de l'experience. Continuez votre quete!",
    "Druide": "La nature vous benit. Vous gagnez 50 points de mana.",
    "Gardien du Tresor": "NOOOOOON! CE TRESOR EST A MOI!!!"
}

# Configuration des BOSS - Créatures redoutables avec équipement
BOSSES = {
    "Warlord Noir": {
        "description": "Un guerrier légendaire couvert d'une armure d'ébène",
        "base_health": 250,
        "base_attack": 35,
        "base_defense": 15,
        "level": 15,
        "rarity_pool": "epique",
        "exp_reward": 750,
        "gold_reward": 400,
        "icon": "⚔️👹"
    },
    "Sorciere de Feu": {
        "description": "Une mage ancienne entourée de flammes éternelles",
        "base_health": 180,
        "base_attack": 40,
        "base_defense": 8,
        "level": 14,
        "rarity_pool": "epique",
        "exp_reward": 700,
        "gold_reward": 350,
        "icon": "🔥👩‍🔬"
    },
    "Archimage Ancien": {
        "description": "Un puissant wizard équipé d'artifacts anciens",
        "base_health": 200,
        "base_attack": 42,
        "base_defense": 10,
        "level": 16,
        "rarity_pool": "legendaire",
        "exp_reward": 900,
        "gold_reward": 500,
        "icon": "✨🧙"
    },
    "Dragonslayer": {
        "description": "Un chasseur de dragons armé jusqu'aux dents",
        "base_health": 280,
        "base_attack": 45,
        "base_defense": 18,
        "level": 17,
        "rarity_pool": "legendaire",
        "exp_reward": 1000,
        "gold_reward": 600,
        "icon": "🐉⚔️"
    },
    "Lich Immortel": {
        "description": "Un non-mort ancien portant d'anciens artefacts",
        "base_health": 300,
        "base_attack": 38,
        "base_defense": 20,
        "level": 18,
        "rarity_pool": "legendaire",
        "exp_reward": 1200,
        "gold_reward": 700,
        "icon": "💀🧟"
    }
}

# Configuration pour l'équipement des boss par rareté
BOSS_EQUIPMENT_CONFIG = {
    "epique": {
        "weapon_bonus": 12,
        "armor_bonus": 8,
        "health_bonus": 50,
        "items_count": 2
    },
    "legendaire": {
        "weapon_bonus": 18,
        "armor_bonus": 12,
        "health_bonus": 80,
        "items_count": 3
    }
}
