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
        "description": "Vaincre 5 Goblins",
        "target_enemy": "Goblin",
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
        # Armes
        "Épée de Fer",
        "Arc Longue Portée",
        "Bâton de Mana",
        "Dague Rouillée",
        "Massue en Bois",
        "Lance de Chasse",
        "Fouet de Cuir",
        "Couteau de Lancer",
        "Épée Acérée",
        "Arc de Précision",
        # Armures
        "Armure Cuir",
        "Tunique de Voyageur",
        "Plastron en Bronze",
        "Bouclier en Bois",
        "Armure Légère",
        # Accessoires
        "Anneau de Santé",
        "Anneau de Force",
        "Anneau de Protection",
        "Pendentif en Cuivre",
        "Bracelet de Force",
        "Amulette de Vitalité",
        "Bague en Fer",
        # Consommables
        "Potion Santé",
        "Potion Mana",
        "Herbe Médicinale",
        "Baie Énergétique",
        "Pain de Voyage"
    ],
    "rare": [
        # Armes
        "Hache de Bataille",
        "Arc de Chasse",
        "Bâton Flamboyant",
        "Épée d'Acier Trempé",
        "Hache Jumelle",
        "Arc Renforcé",
        "Bâton Runique",
        "Faux de Guerre",
        "Masse d'Armes",
        "Arbalète Légère",
        "Épée de Lumière",
        "Bâton Glacial",
        "Sceptre Arcaniste",
        "Arc Sylvain",
        "Arc Flamboyant",
        # Armures
        "Armure de Fer",
        "Cotte de Mailles",
        "Bouclier de Fer",
        "Cape de Protection",
        "Casque de Guerre",
        "Armure Acier",
        "Armure du Mage",
        # Accessoires
        "Amulette de Mana",
        "Anneau du Guerrier",
        "Anneau du Mage",
        "Amulette du Chasseur",
        "Collier de Griffes",
        "Talisman de Mana",
        "Boucle d'Oreille d'Agilité",
        # Consommables
        "Potion Santé Majeure",
        "Potion Mana Majeure",
        "Potion Force",
        "Potion Protection",
        "Potion Poison",
        "Potion d'Acier",
        "Potion de Rage",
        "Potion de Rempart",
        "Elixir Mineur"
    ],
    "epique": [
        # Armes
        "Marteau de Guerre",
        "Arc Élémental",
        "Bâton du Sage",
        "Épée Vampirique",
        "Trident des Abysses",
        "Katana Céleste",
        "Bâton de Liche",
        "Arc SPECTRAL",
        "Double Hache Chaos",
        "Lame Sombre",
        "Glaive du Guerrier",
        "Orbe de Puissance",
        "Bâton Infernal",
        "Arc du Chasseur Légendaire",
        "Arc Glacé",
        # Armures
        "Armure Dragon",
        "Armure en Obsidienne",
        "Robe d'Archimage",
        "Bouclier du Paladin",
        "Armure Mithril",
        "Armure de Brume",
        "Armure Abyssale",
        # Accessoires
        "Couronne de Pouvoir",
        "Anneau de l'Archimage",
        "Bague de Régénération",
        "Pendentif du Dragon",
        "Bracelet d'Éther",
        "Ceinture de Titan",
        # Consommables
        "Élixir de Vie",
        "Élixir de Mana Cosmique",
        "Potion Berserker",
        "Potion d'Invulnérabilité",
        "Élixir Phénix"
    ],
    "legendaire": [
        # Armes
        "Lame Primordiale",
        "Épée de Feu",
        "Éclair Éternel",
        "Excalibur",
        "Gungnir, Lance d'Odin",
        "Arc d'Artémis",
        "Bâton de Merlin",
        "Lame du Néant",
        "Mjolnir",
        # Armures
        "Armure Céleste",
        "Armure d'Achille",
        "Égide d'Athéna",
        "Manteau des Ombres",
        "Armure Sacrée",
        # Accessoires
        "Anneau Infini",
        "Couronne du Roi Démon",
        "Oeil de Ra",
        "Anneau Unique",
        "Amulette de l'Immortel",
        # Consommables
        "Ambroisie Divine",
        "Potion de Résurrection"
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
       "required_level": 3,
        "price": 80,
        "description": "Épée standard pour guerrier"
    },
    "Hache de Bataille": {
        "type": "weapon",
        "attack_bonus": 10,
        "class": "Guerrier",
        "rarity": "rare",
       "required_level": 6,
        "price": 150,
        "description": "Hache puissante pour combat rapproché"
    },
    "Marteau de Guerre": {
        "type": "weapon",
        "attack_bonus": 12,
        "class": "Guerrier",
        "rarity": "epique",
       "required_level": 12,
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
       "required_level": 3,
        "price": 80,
        "description": "Amplifie la magie"
    },
    "Bâton Flamboyant": {
        "type": "weapon",
        "attack_bonus": 8,
        "mana_bonus": 40,
        "class": "Mage",
        "rarity": "rare",
       "required_level": 7,
        "price": 150,
        "description": "Lance des feux puissants"
    },
    "Bâton du Sage": {
        "type": "weapon",
        "attack_bonus": 12,
        "mana_bonus": 60,
        "class": "Mage",
        "rarity": "epique",
       "required_level": 14,
        "price": 250,
        "description": "Ancien bâton de grand pouvoir"
    },
    
    # ARMES ARCHER
    "Arc Longue Portée": {
        "type": "weapon",
        "attack_bonus": 6,
        "class": "Archer",
        "rarity": "commun",
       "required_level": 2,
        "price": 80,
        "description": "Arc de chasseur"
    },
    "Arc de Chasse": {
        "type": "weapon",
        "attack_bonus": 9,
        "class": "Archer",
        "rarity": "rare",
       "required_level": 6,
        "price": 150,
        "description": "Arc parfaitement équilibré"
    },
    "Arc Élémental": {
        "type": "weapon",
        "attack_bonus": 13,
        "class": "Archer",
        "rarity": "epique",
       "required_level": 12,
        "price": 250,
        "description": "Flèches en feu et glaçon"
    },
    
    # ARMURES
    "Armure Cuir": {
        "type": "armor",
        "defense_bonus": 2,
        "price": 40,
       "required_level": 1,
        "description": "Armure légère en cuir"
    },
    "Armure de Fer": {
        "type": "armor",
        "defense_bonus": 5,
        "rarity": "commun",
       "required_level": 2,
        "price": 100,
        "description": "Armure solide en fer"
    },
    "Armure Dragon": {
        "type": "armor",
        "defense_bonus": 10,
        "rarity": "epique",
       "required_level": 12,
        "price": 300,
        "description": "Armure faite de peau de dragon"
    },
    "Armure Céleste": {
        "type": "armor",
        "defense_bonus": 15,
        "rarity": "legendaire",
       "required_level": 20,
        "price": 500,
        "description": "Armure des anges"
    },
    
    # CONSOMMABLES
    "Potion Santé": {
        "type": "consumable",
        "heal": 50,
        "rarity": "commun",
       "required_level": 1,
        "price": 20,
        "description": "Restaure 50 points de santé"
    },
    "Potion Santé Majeure": {
        "type": "consumable",
        "heal": 150,
        "rarity": "rare",
       "required_level": 3,
        "price": 50,
        "description": "Restaure 150 points de santé"
    },
    "Potion Mana": {
        "type": "consumable",
        "mana": 30,
        "rarity": "commun",
       "required_level": 1,
        "price": 25,
        "description": "Restaure 30 points de mana"
    },
    "Potion Mana Majeure": {
        "type": "consumable",
        "mana": 100,
        "rarity": "rare",
       "required_level": 3,
        "price": 60,
        "description": "Restaure 100 points de mana"
    },
    "Potion Force": {
        "type": "consumable",
        "attack_boost": 10,
        "duration": 3,
        "rarity": "epique",
       "required_level": 10,
        "price": 80,
        "description": "+10 Attack pendant 3 tours"
    },
    "Potion Protection": {
        "type": "consumable",
        "defense_boost": 10,
        "duration": 3,
        "rarity": "epique",
       "required_level": 10,
        "price": 80,
        "description": "+10 Defense pendant 3 tours"
    },
    
    # LÉGENDAIRES
    "Épée de Feu": {
        "type": "weapon",
        "attack_bonus": 50,
        "rarity": "legendaire",
       "required_level": 24,
        "class": "Guerrier",
        "price": 0,
        "description": "Épée légendaire enflammée"
    },
    "Éclair Éternel": {
        "type": "weapon",
        "attack_bonus": 40,
        "mana_bonus": 80,
        "rarity": "legendaire",
       "required_level": 24,
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
       "required_level": 3,
       "price": 100,
       "description": "Épée bien affûtée"
    },
    "Épée de Lumière": {
       "type": "weapon",
       "attack_bonus": 11,
       "defense_bonus": 2,
       "class": "Guerrier",
       "rarity": "rare",
       "required_level": 7,
       "price": 180,
       "description": "Épée sacrée brillante"
    },
    "Lame Sombre": {
       "type": "weapon",
       "attack_bonus": 14,
       "health_bonus": 20,
       "class": "Guerrier",
       "rarity": "epique",
       "required_level": 13,
       "price": 280,
       "description": "Lame maudite qui renforce le porteur"
    },
    "Glaive du Guerrier": {
       "type": "weapon",
       "attack_bonus": 15,
       "defense_bonus": 1,
       "class": "Guerrier",
       "rarity": "epique",
       "required_level": 13,
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
       "required_level": 7,
       "price": 160,
       "description": "Bâton de glace éternelle"
    },
    "Sceptre Arcaniste": {
       "type": "weapon",
       "attack_bonus": 10,
       "mana_bonus": 50,
       "class": "Mage",
       "rarity": "rare",
       "required_level": 8,
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
       "required_level": 15,
       "price": 320,
       "description": "Orbe cosmique d'une puissance infinie"
    },
    "Bâton Infernal": {
       "type": "weapon",
       "attack_bonus": 14,
       "mana_bonus": 65,
       "class": "Mage",
       "rarity": "epique",
       "required_level": 15,
       "price": 310,
       "description": "Bâton craché par le feu infernal"
    },
    
    # ARMES ARCHER SUPPLÉMENTAIRES
    "Arc de Précision": {
       "type": "weapon",
       "attack_bonus": 8,
       "class": "Archer",
       "rarity": "commun",
       "required_level": 3,
       "price": 110,
       "description": "Arc très précis"
    },
    "Arc Sylvain": {
       "type": "weapon",
       "attack_bonus": 10,
       "defense_bonus": 1,
       "class": "Archer",
       "rarity": "rare",
       "required_level": 6,
       "price": 160,
       "description": "Arc de la forêt ancienne"
    },
    "Arc Flamboyant": {
       "type": "weapon",
       "attack_bonus": 11,
       "health_bonus": 15,
       "class": "Archer",
       "rarity": "rare",
       "required_level": 7,
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
       "required_level": 14,
       "price": 350,
       "description": "Arc du grand chasseur d'antan"
    },
    "Arc Glacé": {
       "type": "weapon",
       "attack_bonus": 14,
       "mana_bonus": 40,
       "class": "Archer",
       "rarity": "epique",
       "required_level": 14,
       "price": 330,
       "description": "Arc qui tire des flèches glaciales"
    },
    
    # ARMURES SUPPLÉMENTAIRES
    "Armure Légère": {
       "type": "armor",
       "defense_bonus": 3,
       "rarity": "commun",
       "required_level": 1,
       "price": 60,
       "description": "Armure légère et flexible"
    },
    "Armure Acier": {
       "type": "armor",
       "defense_bonus": 7,
       "rarity": "rare",
       "required_level": 5,
       "price": 120,
       "description": "Armure d'acier renforcé"
    },
    "Armure Mithril": {
       "type": "armor",
       "defense_bonus": 12,
       "health_bonus": 40,
       "rarity": "epique",
       "required_level": 13,
       "price": 350,
       "description": "Armure légendaire de mithril"
    },
    "Armure du Mage": {
       "type": "armor",
       "defense_bonus": 3,
       "mana_bonus": 50,
       "rarity": "rare",
       "required_level": 7,
       "price": 140,
       "description": "Tunique magique pour mage"
    },
    "Armure de Brume": {
       "type": "armor",
       "defense_bonus": 8,
       "mana_bonus": 30,
       "rarity": "epique",
       "required_level": 12,
       "price": 320,
       "description": "Armure spectrale de brume magique"
    },
    "Armure Abyssale": {
       "type": "armor",
       "defense_bonus": 11,
       "health_bonus": 50,
       "rarity": "epique",
       "required_level": 14,
       "price": 340,
       "description": "Armure noire des abysses"
    },
    "Armure Sacrée": {
       "type": "armor",
       "defense_bonus": 14,
       "health_bonus": 60,
       "rarity": "legendaire",
       "required_level": 20,
       "price": 600,
       "description": "Armure benedite par les dieux"
    },
    
    # ACCESSOIRES (Anneaux, Amulettes, etc.)
    "Anneau de Santé": {
       "type": "accessory",
       "health_bonus": 30,
       "rarity": "commun",
       "required_level": 2,
       "price": 50,
       "description": "Anneau qui augmente la vitalité"
    },
    "Anneau de Force": {
       "type": "accessory",
       "attack_bonus": 3,
       "rarity": "commun",
       "required_level": 1,
       "price": 60,
       "description": "Anneau qui augmente l'attaque"
    },
    "Anneau de Protection": {
       "type": "accessory",
       "defense_bonus": 3,
       "rarity": "commun",
       "required_level": 1,
       "price": 60,
       "description": "Anneau qui augmente la défense"
    },
    "Amulette de Mana": {
       "type": "accessory",
       "mana_bonus": 40,
       "rarity": "rare",
       "required_level": 5,
       "price": 120,
       "description": "Amulette qui restaure le mana"
    },
    "Anneau du Guerrier": {
       "type": "accessory",
       "attack_bonus": 5,
       "health_bonus": 25,
       "rarity": "rare",
       "required_level": 6,
       "price": 140,
       "description": "Anneau ancestral des guerriers"
    },
    "Anneau du Mage": {
       "type": "accessory",
       "mana_bonus": 60,
       "attack_bonus": 2,
       "rarity": "rare",
       "required_level": 7,
       "price": 150,
       "description": "Anneau qui amplifie la magie"
    },
    "Amulette du Chasseur": {
       "type": "accessory",
       "attack_bonus": 4,
       "defense_bonus": 2,
       "rarity": "rare",
       "required_level": 5,
       "price": 130,
       "description": "Amulette du chasseur de renom"
    },
    "Couronne de Pouvoir": {
       "type": "accessory",
       "attack_bonus": 8,
       "health_bonus": 50,
       "defense_bonus": 5,
       "rarity": "epique",
       "required_level": 14,
       "price": 400,
       "description": "Couronne qui confère puissance et prestige"
    },
    "Anneau de l'Archimage": {
       "type": "accessory",
       "mana_bonus": 100,
       "attack_bonus": 5,
       "rarity": "epique",
       "required_level": 14,
       "price": 420,
       "description": "Anneau du grand archimage"
    },
    "Bague de Régénération": {
       "type": "accessory",
       "health_bonus": 80,
       "rarity": "epique",
       "required_level": 13,
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
       "required_level": 22,
       "price": 800,
       "description": "Anneau qui balance tous les attributs parfaitement"
    },
    
    # CONSOMMABLES SUPPLÉMENTAIRES
    "Élixir de Vie": {
       "type": "consumable",
       "heal": 200,
       "rarity": "epique",
       "required_level": 10,
       "price": 120,
       "description": "Restaure 200 points de santé d'un coup"
    },
    "Élixir de Mana Cosmique": {
       "type": "consumable",
       "mana": 150,
       "rarity": "epique",
       "required_level": 10,
       "price": 130,
       "description": "Restaure 150 points de mana d'un coup"
    },
    "Potion Poison": {
       "type": "consumable",
       "attack_boost": 15,
       "duration": 2,
       "rarity": "rare",
       "required_level": 3,
       "price": 70,
       "description": "+15 Attack pendant 2 tours (toxine)"
    },
    "Potion d'Acier": {
       "type": "consumable",
       "defense_boost": 15,
       "duration": 2,
       "rarity": "rare",
       "required_level": 3,
       "price": 70,
       "description": "+15 Defense pendant 2 tours"
    },
    # ===== NOUVEAUX ITEMS DE LOOT =====

    # --- ARMES COMMUNES ---
    "Dague Rouillée": {
       "type": "weapon",
       "attack_bonus": 3,
       "rarity": "commun",
       "required_level": 1,
       "price": 30,
       "description": "Une vieille dague encore tranchante"
    },
    "Massue en Bois": {
       "type": "weapon",
       "attack_bonus": 5,
       "rarity": "commun",
       "required_level": 2,
       "price": 45,
       "description": "Un gros bâton solide pour cogner"
    },
    "Lance de Chasse": {
       "type": "weapon",
       "attack_bonus": 6,
       "rarity": "commun",
       "required_level": 2,
       "price": 60,
       "description": "Lance utilisée par les chasseurs"
    },
    "Fouet de Cuir": {
       "type": "weapon",
       "attack_bonus": 4,
       "defense_bonus": 1,
       "rarity": "commun",
       "required_level": 2,
       "price": 50,
       "description": "Un fouet flexible et rapide"
    },
    "Couteau de Lancer": {
       "type": "weapon",
       "attack_bonus": 5,
       "rarity": "commun",
       "required_level": 2,
       "price": 55,
       "description": "Petit couteau équilibré pour le lancer"
    },

    # --- ARMURES COMMUNES ---
    "Tunique de Voyageur": {
       "type": "armor",
       "defense_bonus": 1,
       "rarity": "commun",
       "required_level": 1,
       "price": 25,
       "description": "Vêtement épais offrant une protection minime"
    },
    "Plastron en Bronze": {
       "type": "armor",
       "defense_bonus": 3,
       "rarity": "commun",
       "required_level": 1,
       "price": 55,
       "description": "Plastron bon marché en bronze"
    },
    "Bouclier en Bois": {
       "type": "armor",
       "defense_bonus": 2,
       "health_bonus": 10,
       "rarity": "commun",
       "required_level": 2,
       "price": 45,
       "description": "Bouclier simple mais efficace"
    },

    # --- ACCESSOIRES COMMUNS ---
    "Pendentif en Cuivre": {
       "type": "accessory",
       "health_bonus": 15,
       "rarity": "commun",
       "required_level": 1,
       "price": 35,
       "description": "Un modeste pendentif porte-bonheur"
    },
    "Bracelet de Force": {
       "type": "accessory",
       "attack_bonus": 2,
       "rarity": "commun",
       "required_level": 1,
       "price": 40,
       "description": "Bracelet en cuir renforcé"
    },
    "Amulette de Vitalité": {
       "type": "accessory",
       "health_bonus": 20,
       "rarity": "commun",
       "required_level": 2,
       "price": 45,
       "description": "Petite amulette qui renforce le corps"
    },
    "Bague en Fer": {
       "type": "accessory",
       "defense_bonus": 2,
       "rarity": "commun",
       "required_level": 1,
       "price": 40,
       "description": "Bague solide en fer forgé"
    },

    # --- CONSOMMABLES COMMUNS ---
    "Herbe Médicinale": {
       "type": "consumable",
       "heal": 30,
       "rarity": "commun",
       "required_level": 1,
       "price": 10,
       "description": "Plante sauvage aux vertus curatives"
    },
    "Baie Énergétique": {
       "type": "consumable",
       "mana": 20,
       "rarity": "commun",
       "required_level": 1,
       "price": 15,
       "description": "Petite baie qui restaure un peu de mana"
    },
    "Pain de Voyage": {
       "type": "consumable",
       "heal": 20,
       "rarity": "commun",
       "required_level": 1,
       "price": 8,
       "description": "Nourriture simple qui redonne des forces"
    },

    # --- ARMES RARES ---
    "Épée d'Acier Trempé": {
       "type": "weapon",
       "attack_bonus": 9,
       "rarity": "rare",
       "required_level": 6,
       "price": 130,
       "description": "Lame forgée dans un acier de qualité"
    },
    "Hache Jumelle": {
       "type": "weapon",
       "attack_bonus": 8,
       "defense_bonus": 1,
       "class": "Guerrier",
       "rarity": "rare",
       "required_level": 6,
       "price": 140,
       "description": "Deux petites haches maniées en duo"
    },
    "Arc Renforcé": {
       "type": "weapon",
       "attack_bonus": 8,
       "class": "Archer",
       "rarity": "rare",
       "required_level": 5,
       "price": 120,
       "description": "Arc aux branches renforcées de métal"
    },
    "Bâton Runique": {
       "type": "weapon",
       "attack_bonus": 6,
       "mana_bonus": 25,
       "class": "Mage",
       "rarity": "rare",
       "required_level": 6,
       "price": 130,
       "description": "Bâton gravé de runes anciennes"
    },
    "Faux de Guerre": {
       "type": "weapon",
       "attack_bonus": 10,
       "rarity": "rare",
       "required_level": 6,
       "price": 145,
       "description": "Une faux transformée en arme redoutable"
    },
    "Masse d'Armes": {
       "type": "weapon",
       "attack_bonus": 9,
       "defense_bonus": 2,
       "class": "Guerrier",
       "rarity": "rare",
       "required_level": 6,
       "price": 135,
       "description": "Masse lourde qui écrase les armures"
    },
    "Arbalète Légère": {
       "type": "weapon",
       "attack_bonus": 9,
       "class": "Archer",
       "rarity": "rare",
       "required_level": 6,
       "price": 140,
       "description": "Arbalète compacte et rapide à recharger"
    },

    # --- ARMURES RARES ---
    "Cotte de Mailles": {
       "type": "armor",
       "defense_bonus": 5,
       "rarity": "rare",
       "required_level": 5,
       "price": 110,
       "description": "Armure en anneaux métalliques entrelacés"
    },
    "Bouclier de Fer": {
       "type": "armor",
       "defense_bonus": 6,
       "health_bonus": 15,
       "rarity": "rare",
       "required_level": 6,
       "price": 125,
       "description": "Grand bouclier rond en fer"
    },
    "Cape de Protection": {
       "type": "armor",
       "defense_bonus": 3,
       "mana_bonus": 15,
       "rarity": "rare",
       "required_level": 5,
       "price": 100,
       "description": "Cape enchantée qui dévie les sorts"
    },
    "Casque de Guerre": {
       "type": "armor",
       "defense_bonus": 4,
       "health_bonus": 20,
       "rarity": "rare",
       "required_level": 5,
       "price": 115,
       "description": "Casque en acier protégeant la tête"
    },

    # --- ACCESSOIRES RARES ---
    "Collier de Griffes": {
       "type": "accessory",
       "attack_bonus": 4,
       "rarity": "rare",
       "required_level": 5,
       "price": 110,
       "description": "Collier fait de griffes de monstres"
    },
    "Talisman de Mana": {
       "type": "accessory",
       "mana_bonus": 45,
       "rarity": "rare",
       "required_level": 6,
       "price": 120,
       "description": "Talisman pulsant d'énergie magique"
    },
    "Boucle d'Oreille d'Agilité": {
       "type": "accessory",
       "attack_bonus": 2,
       "defense_bonus": 2,
       "rarity": "rare",
       "required_level": 5,
       "price": 100,
       "description": "Boucle d'oreille qui améliore les réflexes"
    },

    # --- CONSOMMABLES RARES ---
    "Potion de Rage": {
       "type": "consumable",
       "attack_boost": 12,
       "duration": 3,
       "rarity": "rare",
       "required_level": 3,
       "price": 65,
       "description": "+12 Attack pendant 3 tours"
    },
    "Potion de Rempart": {
       "type": "consumable",
       "defense_boost": 12,
       "duration": 3,
       "rarity": "rare",
       "required_level": 3,
       "price": 65,
       "description": "+12 Defense pendant 3 tours"
    },
    "Elixir Mineur": {
       "type": "consumable",
       "heal": 100,
       "mana": 50,
       "rarity": "rare",
       "required_level": 3,
       "price": 80,
       "description": "Restaure 100 HP et 50 MP"
    },

    # --- ARMES ÉPIQUES ---
    "Épée Vampirique": {
       "type": "weapon",
       "attack_bonus": 13,
       "health_bonus": 25,
       "class": "Guerrier",
       "rarity": "epique",
       "required_level": 13,
       "price": 280,
       "description": "Lame sombre qui draine la vie"
    },
    "Trident des Abysses": {
       "type": "weapon",
       "attack_bonus": 14,
       "mana_bonus": 20,
       "rarity": "epique",
       "required_level": 13,
       "price": 290,
       "description": "Trident maudit des profondeurs"
    },
    "Katana Céleste": {
       "type": "weapon",
       "attack_bonus": 13,
       "defense_bonus": 3,
       "rarity": "epique",
       "required_level": 13,
       "price": 275,
       "description": "Lame fine forgée sous les étoiles"
    },
    "Bâton de Liche": {
       "type": "weapon",
       "attack_bonus": 12,
       "mana_bonus": 55,
       "class": "Mage",
       "rarity": "epique",
       "required_level": 14,
       "price": 300,
       "description": "Bâton imprégné de nécromancie"
    },
    "Arc SPECTRAL": {
       "type": "weapon",
       "attack_bonus": 13,
       "mana_bonus": 20,
       "class": "Archer",
       "rarity": "epique",
       "required_level": 13,
       "price": 285,
       "description": "Arc dont les flèches traversent les murs"
    },
    "Double Hache Chaos": {
       "type": "weapon",
       "attack_bonus": 15,
       "class": "Guerrier",
       "rarity": "epique",
       "required_level": 12,
       "price": 310,
       "description": "Deux haches tourbillonnantes de chaos"
    },

    # --- ARMURES ÉPIQUES ---
    "Armure en Obsidienne": {
       "type": "armor",
       "defense_bonus": 10,
       "attack_bonus": 3,
       "rarity": "epique",
       "required_level": 12,
       "price": 330,
       "description": "Armure noire tranchante comme du verre"
    },
    "Robe d'Archimage": {
       "type": "armor",
       "defense_bonus": 5,
       "mana_bonus": 60,
       "health_bonus": 20,
       "rarity": "epique",
       "required_level": 14,
       "price": 340,
       "description": "Robe tissée de fils magiques"
    },
    "Bouclier du Paladin": {
       "type": "armor",
       "defense_bonus": 13,
       "health_bonus": 35,
       "rarity": "epique",
       "required_level": 13,
       "price": 350,
       "description": "Bouclier sacré des chevaliers de lumière"
    },

    # --- ACCESSOIRES ÉPIQUES ---
    "Pendentif du Dragon": {
       "type": "accessory",
       "attack_bonus": 6,
       "health_bonus": 35,
       "rarity": "epique",
       "required_level": 12,
       "price": 380,
       "description": "Écaille de dragon montée en pendentif"
    },
    "Bracelet d'Éther": {
       "type": "accessory",
       "mana_bonus": 70,
       "defense_bonus": 3,
       "rarity": "epique",
       "required_level": 13,
       "price": 390,
       "description": "Bracelet tissé d'énergie pure"
    },
    "Ceinture de Titan": {
       "type": "accessory",
       "health_bonus": 60,
       "defense_bonus": 5,
       "rarity": "epique",
       "required_level": 13,
       "price": 370,
       "description": "Ceinture portée par les géants anciens"
    },

    # --- CONSOMMABLES ÉPIQUES ---
    "Potion Berserker": {
       "type": "consumable",
       "attack_boost": 20,
       "duration": 3,
       "rarity": "epique",
       "required_level": 10,
       "price": 110,
       "description": "+20 Attack pendant 3 tours"
    },
    "Potion d'Invulnérabilité": {
       "type": "consumable",
       "defense_boost": 20,
       "duration": 3,
       "rarity": "epique",
       "required_level": 10,
       "price": 110,
       "description": "+20 Defense pendant 3 tours"
    },
    "Élixir Phénix": {
       "type": "consumable",
       "heal": 9999,
       "rarity": "epique",
       "required_level": 10,
       "price": 200,
       "description": "Restaure toute la santé d'un coup"
    },

    # --- ARMES LÉGENDAIRES ---
    "Lame Primordiale": {
       "type": "weapon",
       "attack_bonus": 8,
       "damage_multiplier": 2.0,
       "rarity": "legendaire",
       "required_level": 1,
       "price": 0,
       "description": "Une lame ancienne qui double les dégâts infligés"
    },
    "Excalibur": {
       "type": "weapon",
       "attack_bonus": 45,
       "defense_bonus": 10,
       "health_bonus": 50,
       "class": "Guerrier",
       "rarity": "legendaire",
       "required_level": 25,
       "price": 0,
       "description": "L'épée du roi légendaire"
    },
    "Gungnir, Lance d'Odin": {
       "type": "weapon",
       "attack_bonus": 50,
       "rarity": "legendaire",
       "required_level": 24,
       "price": 0,
       "description": "Lance divine qui ne manque jamais sa cible"
    },
    "Arc d'Artémis": {
       "type": "weapon",
       "attack_bonus": 42,
       "defense_bonus": 5,
       "mana_bonus": 30,
       "class": "Archer",
       "rarity": "legendaire",
       "required_level": 24,
       "price": 0,
       "description": "Arc de la déesse de la chasse"
    },
    "Bâton de Merlin": {
       "type": "weapon",
       "attack_bonus": 35,
       "mana_bonus": 100,
       "health_bonus": 40,
       "class": "Mage",
       "rarity": "legendaire",
       "required_level": 25,
       "price": 0,
       "description": "Le bâton du plus grand enchanteur"
    },
    "Lame du Néant": {
       "type": "weapon",
       "attack_bonus": 55,
       "rarity": "legendaire",
       "required_level": 24,
       "price": 0,
       "description": "Une lame qui tranche la réalité elle-même"
    },
    "Mjolnir": {
       "type": "weapon",
       "attack_bonus": 48,
       "defense_bonus": 8,
       "class": "Guerrier",
       "rarity": "legendaire",
       "required_level": 24,
       "price": 0,
       "description": "Le marteau du dieu du tonnerre"
    },

    # --- ARMURES LÉGENDAIRES ---
    "Armure d'Achille": {
       "type": "armor",
       "defense_bonus": 18,
       "health_bonus": 80,
       "rarity": "legendaire",
       "required_level": 22,
       "price": 0,
       "description": "Armure quasi invulnérable du héros grec"
    },
    "Égide d'Athéna": {
       "type": "armor",
       "defense_bonus": 20,
       "health_bonus": 50,
       "mana_bonus": 30,
       "rarity": "legendaire",
       "required_level": 22,
       "price": 0,
       "description": "Le bouclier divin de la sagesse"
    },
    "Manteau des Ombres": {
       "type": "armor",
       "defense_bonus": 12,
       "attack_bonus": 8,
       "mana_bonus": 40,
       "rarity": "legendaire",
       "required_level": 20,
       "price": 0,
       "description": "Cape vivante qui absorbe la lumière"
    },

    # --- ACCESSOIRES LÉGENDAIRES ---
    "Couronne du Roi Démon": {
       "type": "accessory",
       "attack_bonus": 12,
       "health_bonus": 70,
       "defense_bonus": 8,
       "mana_bonus": 40,
       "rarity": "legendaire",
       "required_level": 22,
       "price": 0,
       "description": "Couronne maudite d'un roi déchu"
    },
    "Oeil de Ra": {
       "type": "accessory",
       "attack_bonus": 10,
       "mana_bonus": 80,
       "rarity": "legendaire",
       "required_level": 20,
       "price": 0,
       "description": "L'oeil du dieu solaire égyptien"
    },
    "Anneau Unique": {
       "type": "accessory",
       "attack_bonus": 15,
       "defense_bonus": 10,
       "health_bonus": 80,
       "mana_bonus": 60,
       "rarity": "legendaire",
       "required_level": 24,
       "price": 0,
       "description": "Un anneau pour les gouverner tous"
    },

    # --- CONSOMMABLES LÉGENDAIRES ---
    "Ambroisie Divine": {
       "type": "consumable",
       "heal": 9999,
       "mana": 9999,
       "rarity": "legendaire",
       "required_level": 18,
       "price": 0,
       "description": "Nectar des dieux, restaure tout"
    },
    "Potion de Résurrection": {
       "type": "consumable",
       "heal": 9999,
       "attack_boost": 25,
       "defense_boost": 25,
       "duration": 5,
       "rarity": "legendaire",
       "required_level": 18,
       "price": 0,
       "description": "Potion mythique qui ramène de la mort"
    },

    # ===== Items Zone 2 (nouveaux objets) =====
    "Bâton des Abysses": {
       "type": "weapon",
       "attack_bonus": 15,
       "mana_bonus": 50,
       "class": "Mage",
       "rarity": "epique",
       "required_level": 14,
       "price": 0,
       "description": "Bâton imprimé de magie noire des abysses"
    },
    "Épée du Dragon": {
       "type": "weapon",
       "attack_bonus": 20,
       "class": "Guerrier",
       "rarity": "legendaire",
       "required_level": 20,
       "price": 0,
       "description": "Épée forgée dans les flammes d'un dragon"
    },
    "Arc des Ombres": {
       "type": "weapon",
       "attack_bonus": 18,
       "class": "Archer",
       "rarity": "epique",
       "required_level": 13,
       "price": 0,
       "description": "Arc maudit qui tire des flèches spectrales"
    },
    "Armure du Gardien": {
       "type": "armor",
       "defense_bonus": 12,
       "health_bonus": 30,
       "rarity": "epique",
       "required_level": 13,
       "price": 0,
       "description": "Armure portée par les gardiens des donjons"
    },
    "Amulette de l'Immortel": {
       "type": "accessory",
       "health_bonus": 50,
       "defense_bonus": 5,
       "rarity": "legendaire",
       "required_level": 20,
       "price": 0,
       "description": "Amulette qui confère une partie de l'immortalité"
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
            "ouest": "river",
            "nord-ouest": "mountain",
            "sud-est": "valley",
            "sud-ouest": "volcano"
        },
        "x": 50,
        "y": 70
    },
    "village": {
        "name": "Village Paisible",
        "description": "Un petit village avec quelques maisons en bois. Les habitants vous regardent avec curiosité.",
        "enemies": [],
        "npcs": ["Aubergiste", "Forgeron", "Colporteur Mystique"],
        "exits": {
            "sud": "forest",
            "est": "temple",
            "ouest": "castle"
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
            "est": "summit",
            "sud-est": "tower"
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
            "sud": "underworld"
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
    # ===== Ennemis Zone 1 (de base) =====
    "Goblin": {
        "health": 25,
        "attack": 10,
        "defense": 2,
        "level": 1,
        "exp_reward": 50,
        "gold_reward": 10
    },
    "Loup": {
        "health": 35,
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
        "health": 20,
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
    },
    # ===== Ennemis Zone 2 (nouveaux monstres) =====
    "Dragon des Abysses": {
        "health": 350,
        "attack": 45,
        "defense": 15,
        "level": 25,
        "exp_reward": 800,
        "gold_reward": 250
    },
    "Démon des Flammes": {
        "health": 280,
        "attack": 40,
        "defense": 12,
        "level": 22,
        "exp_reward": 700,
        "gold_reward": 200
    },
    "Golem de Pierre": {
        "health": 400,
        "attack": 30,
        "defense": 25,
        "level": 20,
        "exp_reward": 600,
        "gold_reward": 150
    },
    "Spectre Supérieur": {
        "health": 220,
        "attack": 35,
        "defense": 8,
        "level": 18,
        "exp_reward": 550,
        "gold_reward": 120
    },
    "Troll des Montagnes": {
        "health": 300,
        "attack": 38,
        "defense": 10,
        "level": 15,
        "exp_reward": 450,
        "gold_reward": 100
    },
    "Loup Blanc": {
        "health": 120,
        "attack": 25,
        "defense": 8,
        "level": 8,
        "exp_reward": 180,
        "gold_reward": 60
    },
    "Géant des Glaces": {
        "health": 250,
        "attack": 35,
        "defense": 18,
        "level": 12,
        "exp_reward": 350,
        "gold_reward": 150
    },
    "Dragon Blanc": {
        "health": 400,
        "attack": 50,
        "defense": 20,
        "level": 25,
        "exp_reward": 800,
        "gold_reward": 350
    },
    "Chevalier des Cieux": {
        "health": 200,
        "attack": 30,
        "defense": 15,
        "level": 14,
        "exp_reward": 400,
        "gold_reward": 120
    },
    "Élémental d'Air": {
        "health": 180,
        "attack": 28,
        "defense": 10,
        "level": 13,
        "exp_reward": 350,
        "gold_reward": 100
    },
    "Phénix": {
        "health": 300,
        "attack": 40,
        "defense": 12,
        "level": 20,
        "exp_reward": 600,
        "gold_reward": 250
    },
    "Spectre": {
        "health": 150,
        "attack": 25,
        "defense": 5,
        "level": 10,
        "exp_reward": 250,
        "gold_reward": 80
    },
    "Golem de Cristal": {
        "health": 280,
        "attack": 30,
        "defense": 22,
        "level": 15,
        "exp_reward": 400,
        "gold_reward": 180
    },
    "Squelette Guerrier": {
        "health": 100,
        "attack": 20,
        "defense": 8,
        "level": 7,
        "exp_reward": 150,
        "gold_reward": 50
    },
    "Zombie": {
        "health": 130,
        "attack": 18,
        "defense": 3,
        "level": 6,
        "exp_reward": 120,
        "gold_reward": 40
    },
    "Liche": {
        "health": 350,
        "attack": 45,
        "defense": 15,
        "level": 22,
        "exp_reward": 700,
        "gold_reward": 300
    },
    "Golem de Lave": {
        "health": 350,
        "attack": 38,
        "defense": 25,
        "level": 20,
        "exp_reward": 600,
        "gold_reward": 200
    },
    "Dragon de Feu": {
        "health": 500,
        "attack": 55,
        "defense": 22,
        "level": 30,
        "exp_reward": 1000,
        "gold_reward": 500
    },
    "Chevalier Noir": {
        "health": 280,
        "attack": 40,
        "defense": 20,
        "level": 18,
        "exp_reward": 550,
        "gold_reward": 200
    },
    "Garde du Château": {
        "health": 160,
        "attack": 25,
        "defense": 12,
        "level": 10,
        "exp_reward": 200,
        "gold_reward": 70
    },
    "Assassin": {
        "health": 120,
        "attack": 35,
        "defense": 5,
        "level": 12,
        "exp_reward": 300,
        "gold_reward": 100
    },
    "Roi des Ombres": {
        "health": 450,
        "attack": 48,
        "defense": 20,
        "level": 28,
        "exp_reward": 900,
        "gold_reward": 400
    },
    "Mage Noir": {
        "health": 200,
        "attack": 35,
        "defense": 8,
        "level": 15,
        "exp_reward": 400,
        "gold_reward": 150
    },
    "Golem Volant": {
        "health": 220,
        "attack": 28,
        "defense": 15,
        "level": 13,
        "exp_reward": 350,
        "gold_reward": 120
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
    "Gardien du Tresor": "NOOOOOON! CE TRESOR EST A MOI!!!",
    "Colporteur Mystique": "Psst... J'ai un secret pour trouver de meilleurs trésors. Contre quelques pièces d'or, je peux améliorer votre chance de loot. Chaque achat augmente votre chance de 0.5%, et c'est cumulable à l'infini !"
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

# ==================== SYSTÈME DE ZONES ====================

# Configuration des zones
ZONES = {
    1: {
        "name": "Zone 1",
        "description": "Zone de base - Forêts, villages et donjons classiques",
        "unlocked_by_default": True,
        "required_level": 1,
        "enemies": ["Goblin", "Loup", "Goblin Guerrier", "Chauve-souris", "Nymphe Enragee"],
        "loot_table": {
            "commun": 0.55,
            "rare": 0.30,
            "epique": 0.10,
            "legendaire": 0.05
        }
    },
    2: {
        "name": "Zone 2",
        "description": "Zone avancée - Monstres puissants et trésors rares",
        "unlocked_by_default": False,
        "required_level": 10,
        "enemies": ["Dragon Jeune", "Golem", "Pretre Noir", "Gardien du Tresor", "Liche"],
        "loot_table": {
            "commun": 0.20,
            "rare": 0.35,
            "epique": 0.30,
            "legendaire": 0.15
        }
    }
}

# Ennemis spécifiques à la Zone 2 (en plus des ennemis de base)
ZONE_2_ENEMIES = {
    "Dragon des Abysses": {
        "health": 350,
        "attack": 45,
        "defense": 15,
        "level": 25,
        "exp_reward": 800,
        "gold_reward": 250
    },
    "Démon des Flammes": {
        "health": 280,
        "attack": 40,
        "defense": 12,
        "level": 22,
        "exp_reward": 700,
        "gold_reward": 200
    },
    "Golem de Pierre": {
        "health": 400,
        "attack": 30,
        "defense": 25,
        "level": 20,
        "exp_reward": 600,
        "gold_reward": 150
    },
    "Spectre Supérieur": {
        "health": 220,
        "attack": 35,
        "defense": 8,
        "level": 18,
        "exp_reward": 550,
        "gold_reward": 120
    },
    "Troll des Montagnes": {
        "health": 300,
        "attack": 38,
        "defense": 10,
        "level": 15,
        "exp_reward": 450,
        "gold_reward": 100
    }
}

# Loot spécifique à la Zone 2 (en plus du loot de base)
ZONE_2_LOOT = {
    "commun": [
        "Épée Acérée",
        "Armure de Fer",
        "Potion Santé Majeure",
        "Potion Mana Majeure"
    ],
    "rare": [
        "Épée de Lumière",
        "Lame Sombre",
        "Armure Acier",
        "Armure de Brume",
        "Potion Force",
        "Potion Protection"
    ],
    "epique": [
        "Glaive du Guerrier",
        "Marteau de Guerre",
        "Armure Dragon",
        "Armure Mithril",
        "Anneau du Guerrier",
        "Couronne de Pouvoir"
    ],
    "legendaire": [
        "Épée de Feu",
        "Éclair Éternel",
        "Armure Céleste",
        "Armure Sacrée",
        "Anneau Infini"
    ]
}

# Items spécifiques à la Zone 2
ZONE_2_ITEMS = {
    "Bâton des Abysses": {
        "type": "weapon",
        "attack_bonus": 15,
        "mana_bonus": 50,
        "class": "Mage",
        "rarity": "epique",
        "price": 0,
        "description": "Bâton imprimé de magie noire des abysses"
    },
    "Épée du Dragon": {
        "type": "weapon",
        "attack_bonus": 20,
        "class": "Guerrier",
        "rarity": "legendaire",
        "price": 0,
        "description": "Épée forgée dans les flammes d'un dragon"
    },
    "Arc des Ombres": {
        "type": "weapon",
        "attack_bonus": 18,
        "class": "Archer",
        "rarity": "epique",
        "price": 0,
        "description": "Arc maudit qui tire des flèches spectrales"
    },
    "Armure du Gardien": {
        "type": "armor",
        "defense_bonus": 12,
        "health_bonus": 30,
        "rarity": "epique",
        "price": 0,
        "description": "Armure portée par les gardiens des donjons"
    },
    "Amulette de l'Immortel": {
        "type": "accessory",
        "health_bonus": 50,
        "defense_bonus": 5,
        "rarity": "legendaire",
        "price": 0,
        "description": "Amulette qui confère une partie de l'immortalité"
    }
}

# ==================== SYSTÈME DE RUNES ====================

# Définition des runes
RUNES = {
    "Rune de Feu": {
        "icon": "🔥",
        "element": "feu",
        "description": "Imprégnée de flammes éternelles"
    },
    "Rune de Glace": {
        "icon": "❄️",
        "element": "glace",
        "description": "Gèle l'air autour d'elle"
    },
    "Rune de Foudre": {
        "icon": "⚡",
        "element": "foudre",
        "description": "Crépite d'énergie électrique"
    },
    "Rune de Nature": {
        "icon": "🌿",
        "element": "nature",
        "description": "Pulse de vie végétale"
    },
    "Rune d'Ombre": {
        "icon": "💀",
        "element": "ombre",
        "description": "Absorbe la lumière ambiante"
    },
    "Rune de Lumière": {
        "icon": "✨",
        "element": "lumiere",
        "description": "Rayonne d'une clarté divine"
    },
    "Rune du Chaos": {
        "icon": "🌀",
        "element": "chaos",
        "description": "Tourbillonne d'énergie instable"
    }
}

# Raretés des runes (affecte la puissance du buff)
RUNE_RARITIES = {
    "mineure": {"icon": "◇", "multiplier": 1.0, "drop_weight": 60},
    "majeure": {"icon": "◆", "multiplier": 1.5, "drop_weight": 30},
    "ancienne": {"icon": "◈", "multiplier": 2.0, "drop_weight": 10}
}

# Recettes de craft de runes (combiner 2 runes)
RUNE_RECIPES = {
    "Bouclier de Flammes": {
        "runes": ["Rune de Feu", "Rune de Lumière"],
        "icon": "🔥🛡️",
        "description": "Enveloppe le porteur de flammes protectrices",
        "effect": "defense_boost",
        "value": 15,
        "duration": 4,
        "combat_text": "Un bouclier de flammes vous entoure !"
    },
    "Explosion Glacée": {
        "runes": ["Rune de Glace", "Rune de Foudre"],
        "icon": "❄️⚡",
        "description": "Gèle puis électrocute l'ennemi",
        "effect": "bonus_damage_next",
        "value": 40,
        "duration": 1,
        "combat_text": "Une explosion glacée frappe votre ennemi !"
    },
    "Régénération Sauvage": {
        "runes": ["Rune de Nature", "Rune de Lumière"],
        "icon": "🌿✨",
        "description": "Restaure la santé à chaque tour",
        "effect": "regen",
        "value": 25,
        "duration": 5,
        "combat_text": "La nature vous soigne à chaque instant !"
    },
    "Frappe de l'Ombre": {
        "runes": ["Rune d'Ombre", "Rune de Feu"],
        "icon": "💀🔥",
        "description": "Attaque critique garantie au prochain coup",
        "effect": "guaranteed_crit",
        "value": 2.5,
        "duration": 1,
        "combat_text": "Les ombres guident votre lame pour un coup dévastateur !"
    },
    "Courroux Céleste": {
        "runes": ["Rune de Lumière", "Rune de Foudre"],
        "icon": "✨⚡",
        "description": "Augmente massivement l'attaque",
        "effect": "attack_boost",
        "value": 20,
        "duration": 4,
        "combat_text": "La fureur divine augmente votre puissance !"
    },
    "Vortex du Chaos": {
        "runes": ["Rune du Chaos", "Rune d'Ombre"],
        "icon": "🌀💀",
        "description": "Chaque attaque a une chance de frapper 3 fois",
        "effect": "multi_hit",
        "value": 3,
        "duration": 3,
        "combat_text": "Le chaos démultiplie vos frappes !"
    },
    "Armure de Givre": {
        "runes": ["Rune de Glace", "Rune de Nature"],
        "icon": "❄️🌿",
        "description": "Armure de glace qui ralentit l'ennemi",
        "effect": "defense_boost",
        "value": 20,
        "duration": 5,
        "combat_text": "Une armure de givre vivant vous protège !"
    },
    "Tempête Électrique": {
        "runes": ["Rune de Foudre", "Rune de Feu"],
        "icon": "⚡🔥",
        "description": "Inflige des dégâts bonus massifs",
        "effect": "attack_boost",
        "value": 25,
        "duration": 3,
        "combat_text": "Une tempête de feu et de foudre vous habite !"
    },
    "Éclipse": {
        "runes": ["Rune d'Ombre", "Rune de Lumière"],
        "icon": "💀✨",
        "description": "Équilibre parfait, tous les bonus augmentés",
        "effect": "all_boost",
        "value": 12,
        "duration": 4,
        "combat_text": "L'éclipse confère un pouvoir équilibré !"
    },
    "Fureur Primale": {
        "runes": ["Rune de Nature", "Rune du Chaos"],
        "icon": "🌿🌀",
        "description": "Berserk: +30 ATK mais -10 DEF",
        "effect": "berserk",
        "value": 30,
        "penalty": 10,
        "duration": 4,
        "combat_text": "Une fureur primitive s'empare de vous !"
    },
    "Nova Glaciale": {
        "runes": ["Rune de Glace", "Rune d'Ombre"],
        "icon": "❄️💀",
        "description": "Réduit l'attaque de l'ennemi",
        "effect": "enemy_weaken",
        "value": 15,
        "duration": 4,
        "combat_text": "Le froid et les ténèbres affaiblissent votre ennemi !"
    },
    "Déchaînement Arcanique": {
        "runes": ["Rune du Chaos", "Rune de Foudre"],
        "icon": "🌀⚡",
        "description": "Double les dégâts des compétences",
        "effect": "skill_double",
        "value": 2.0,
        "duration": 3,
        "combat_text": "L'énergie arcanique démultiplie vos sorts !"
    }
}

# Chances de drop de runes par ennemi (ajoutées au loot normal)
RUNE_DROP_CHANCE = 0.40  # 40% de chance de drop une rune par combat

# ==================== SYSTÈME DE CARTES ====================

# Cartes : objets ultra-rares qui donnent des bonus permanents
CARDS = {
    "Carte de Force": {
        "icon": "🃏💪",
        "rarity": "rare",
        "description": "Augmente l'attaque de +2 de façon permanente",
        "stat": "attack",
        "value": 2,
        "lore": "Forgée dans le sang d'un guerrier ancien tombé au champ d'honneur, cette carte pulse d'une rage oubliée. Celui qui la brise sent ses muscles se tendre comme des cordes d'arc, et ses coups portent le poids de mille batailles."
    },
    "Carte de Vitalité": {
        "icon": "🃏❤️",
        "rarity": "rare",
        "description": "Augmente les PV max de +10 de façon permanente",
        "stat": "max_health",
        "value": 10,
        "lore": "On dit qu'elle fut créée par une guérisseuse du village de Brume-Claire, qui y enferma l'essence d'un cœur de dragon mourant. La carte bat encore faiblement entre vos doigts, comme si elle se souvenait de son dernier souffle."
    },
    "Carte de Fer": {
        "icon": "🃏🛡️",
        "rarity": "rare",
        "description": "Augmente la défense de +2 de façon permanente",
        "stat": "defense",
        "value": 2,
        "lore": "Trouvée dans les ruines de la forteresse d'Acier-Noir, cette carte porte l'empreinte d'un bouclier légendaire. Les forgerons nains qui la créèrent y insufflèrent la résistance de la montagne elle-même."
    },
    "Carte de Sagesse": {
        "icon": "🃏📘",
        "rarity": "rare",
        "description": "Augmente le mana max de +10 de façon permanente",
        "stat": "max_mana",
        "value": 10,
        "lore": "Arrachée au grimoire d'un archimage disparu il y a trois siècles, cette page vivante murmure des formules que seul votre esprit peut entendre. Les runes qui la parcourent se réarrangent à chaque lune."
    },
    "Carte du Titan": {
        "icon": "🃏⚔️",
        "rarity": "epique",
        "description": "Augmente l'attaque de +5 de façon permanente",
        "stat": "attack",
        "value": 5,
        "lore": "Les Titans de l'ère primordiale gravaient leur force dans des tablettes de cristal. Celle-ci est le dernier fragment connu — elle contient la fureur d'un être qui pouvait briser des montagnes à mains nues. Son poids semble impossible pour un simple morceau de parchemin."
    },
    "Carte du Colosse": {
        "icon": "🃏🏔️",
        "rarity": "epique",
        "description": "Augmente les PV max de +25 de façon permanente",
        "stat": "max_health",
        "value": 25,
        "lore": "Le Colosse de Valdris était une créature de pierre haute de cent coudées, invulnérable aux armes des mortels. Quand il s'effondra enfin, son corps se changea en milliers de ces cartes — chacune contenant une parcelle de son indestructibilité."
    },
    "Carte de l'Archimage": {
        "icon": "🃏✨",
        "rarity": "epique",
        "description": "Augmente le mana max de +25 de façon permanente",
        "stat": "max_mana",
        "value": 25,
        "lore": "Mérilinde l'Éternelle, dernière des Archimages, dispersa son savoir dans sept cartes avant de disparaître dans le Voile. Celle que vous tenez contient un océan de mana compressé — les étoiles qui la parcourent bougent encore."
    },
    "Carte du Destin": {
        "icon": "🃏🍀",
        "rarity": "legendaire",
        "description": "Augmente la chance de loot de +0.5% de façon permanente",
        "stat": "loot_boost",
        "value": 0.5,
        "lore": "Nul ne sait qui créa la Carte du Destin. Certains prétendent qu'elle existait avant le monde lui-même, tissée dans la trame du hasard par une entité au-delà de la compréhension. La posséder, c'est tordre subtilement les probabilités — les trésors viennent à vous comme attirés par une force invisible. On raconte qu'il en existe seulement sept dans toutes les réalités."
    }
}

# Probabilité de base de drop une carte (1%)
CARD_DROP_CHANCE = 0.01

# Bonus pour les boss (3x plus de chance)
CARD_BOSS_MULTIPLIER = 3.0
