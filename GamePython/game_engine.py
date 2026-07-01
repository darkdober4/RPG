# Game Engine - Moteur de jeu RPG
from game_config import (
    GAME_CONFIG, LOCATIONS, ENEMIES, NPCS_DIALOGUE, ITEMS, SHOPS,
    DIFFICULTY_SETTINGS, LOOT_BY_RARITY, CLASSES, DAILY_QUESTS,
    SKILLS, BOSSES, BOSS_EQUIPMENT_CONFIG, PROGRESSIVE_SKILLS,
    ZONES, ZONE_2_ENEMIES, ZONE_2_LOOT, ZONE_2_ITEMS,
    RUNES, RUNE_RECIPES, RUNE_RARITIES, RUNE_DROP_CHANCE,
    CARDS, CARD_DROP_CHANCE, CARD_BOSS_MULTIPLIER
)
import random
from datetime import datetime


class GameEngine:
    """Moteur de jeu principal pour le RPG text-based."""
    
    def __init__(self):
        """Initialise le jeu avec tous les attributs de base."""
        self.player_stats = GAME_CONFIG["player_stats"].copy()
        self.base_stats = GAME_CONFIG["player_stats"].copy()
        self.player_class = None
        self.inventory = {}
        self.equipped = {
            "weapon": None,
            "armor": None,
            "accessory": None
        }
        self.current_location = GAME_CONFIG["starting_location"]
        self.in_combat = False
        self.current_enemy = None
        self.combat_turn = 0
        self.visited_locations = set()
        self.visited_locations.add(self.current_location)
        self.current_shop = None
        self.skills_learned = {}
        self.active_buffs = []
        self.boss_defeated = {}
        self.game_started = datetime.now()
        self.difficulty = "moyen"
        self.daily_quests_completed = []
        self.total_enemies_defeated = 0
        self.total_damage_dealt = 0
        self.total_damage_taken = 0
        self.boss_spawn_chance = 0.15
        self.game_over = False
        self.game_won = False
        self.show_options = False
        self.show_inventory = False
        self.show_quests = False
        self.show_skills = False
        self.show_map = False
        self.unlocked_skills = {}
        self.skill_notifications = []
        self.is_boss_fight = False
        self.current_boss = None
        self.daily_quests = {}
        self.quest_progress = {}
        self.completed_quests = []
        
        # Initialiser toutes les quêtes avec une progression de 0
        for quest_id in DAILY_QUESTS:
            self.quest_progress[quest_id] = 0
        
        # Système de zones
        self.current_zone = 1
        self.unlocked_zones = [1]  # Zone 1 est toujours débloquée par défaut
        self.temporary_buffs = {}
        self.enemy_health = 0
        self.enemy_max_health = 0
        self.enemy_level = 1
        self.enemy_attack = 0
        self.enemy_defense = 0

        # Système de runes
        self.rune_inventory = {}  # {"Rune de Feu|mineure": 2, ...}
        self.active_rune_buffs = []  # [{"name": ..., "effect": ..., "value": ..., "turns_left": ...}, ...]
        self.show_runes = False

        # Boost de loot (Colporteur Mystique)
        self.loot_boost_count = 0

        # Cartes permanentes
        self.card_inventory = {}  # {"Carte de Force": 2, ...}
        self.cards_used = []  # Historique des cartes utilisées pour les bonus

    def set_class(self, class_name):
        if class_name not in CLASSES:
            return False
        self.player_class = class_name
        class_data = CLASSES[class_name]
        # Mettre à jour player_stats et base_stats avec les stats de la classe
        for stat, value in class_data["base_stats"].items():
            self.player_stats[stat] = value
            self.base_stats[stat] = value
        if class_name in SKILLS:
            self.skills_learned[class_name] = {}
            for skill_name, skill_data in SKILLS[class_name].items():
                if skill_data.get("unlocked_at", 1) <= self.player_stats["level"]:
                    self.skills_learned[class_name][skill_name] = True
        
        # Débloquer les compétences progressives selon le niveau
        self.unlock_progressive_skills()
        # Vérifier les zones à débloquer
        self.check_unlocked_zones()
        return True
    
    def get_location_description(self):
        if self.current_location not in LOCATIONS:
            return "<p>Localisation inconnue</p>"
        location_data = LOCATIONS[self.current_location]
        description = f"<h2>{location_data.get('name', 'Localisation')}</h2>"
        description += f"<p>{location_data.get('description', 'Aucune description')}</p>"
        if location_data.get("enemies"):
            description += "<p><strong>Ennemis :</strong> " + ", ".join(location_data["enemies"]) + "</p>"
        if location_data.get("npcs"):
            description += "<p><strong>NPCs :</strong> " + ", ".join(location_data["npcs"]) + "</p>"
        if location_data.get("shops"):
            description += "<p><strong>Magasins :</strong> " + ", ".join(location_data["shops"]) + "</p>"
        return description
    
    def get_available_actions(self):
        actions = []
        if self.in_combat:
            actions = [
                {"type": "attack", "text": "Attaquer", "value": "attack"},
                {"type": "use_skill", "text": "Utiliser compétence", "value": "use_skill"},
                {"type": "use_item", "text": "Utiliser objet", "value": "use_item"},
                {"type": "flee", "text": "Fuir le combat", "value": "flee"}
            ]
        else:
            if self.current_location in LOCATIONS:
                location_data = LOCATIONS[self.current_location]
                if location_data.get("exits"):
                    for direction, destination in location_data["exits"].items():
                        dest_name = LOCATIONS.get(destination, {}).get("name", destination)
                        actions.append({
                            "type": "move",
                            "text": f"Aller {direction.upper()} → {dest_name}",
                            "value": destination
                        })
                if location_data.get("enemies"):
                    actions.append({
                        "type": "fight",
                        "text": "Combattre un ennemi",
                        "value": ""
                    })
                
                # Ajouter des actions pour explorer chaque zone débloquée
                for zone_id in self.unlocked_zones:
                    zone_info = self.get_zone_info(zone_id)
                    if zone_info:
                        zone_name = zone_info['name']
                        # Si c'est la zone actuelle, utiliser "Explorer" sinon "Explorer [Nom]"
                        if zone_id == self.current_zone:
                            actions.append({
                                "type": "explore",
                                "text": f"Explorer ({zone_name})",
                                "value": "explore"
                            })
                        else:
                            actions.append({
                                "type": "explore_zone",
                                "text": f"Explorer {zone_name}",
                                "value": str(zone_id)
                            })
                
                actions.extend([
                    {"type": "rest", "text": "Se reposer", "value": "rest"}
                ])
        return actions
    
    def move(self, destination):
        if self.in_combat:
            return "Vous ne pouvez pas vous déplacer pendant un combat !"
        if self.current_location not in LOCATIONS:
            return "Localisation actuelle inconnue !"
        location_data = LOCATIONS[self.current_location]
        exits = location_data.get("exits", {})
        if destination not in exits.values():
            return f"Vous ne pouvez pas aller à {destination} depuis {self.current_location}."
        self.current_location = destination
        self.visited_locations.add(destination)
        self.close_shop()
        return f"Vous vous êtes déplacé vers {destination}."
    
    def explore_location(self):
        if self.current_location not in LOCATIONS:
            return "Localisation inconnue !"
        location_data = LOCATIONS[self.current_location]
        exploration_result = f"Vous explorez {location_data.get('name', 'la zone')}...\n"
        
        # 30% de chance de trouver du loot (comme avant)
        if random.random() < 0.3:
            # Utiliser get_loot() pour avoir un loot basé sur la zone actuelle
            loot = self.get_loot(self.player_stats.get("level", 1))
            if loot:
                for item, qty in loot.items():
                    if item in self.inventory:
                        self.inventory[item] += qty
                    else:
                        self.inventory[item] = qty
                    exploration_result += f"Vous avez trouvé : {item} (x{qty})\n"
            else:
                exploration_result += "Vous n'avez rien trouvé d'intéressant.\n"
        else:
            exploration_result += "Vous n'avez rien trouvé d'intéressant.\n"
        
        # 25% de chance de déclencher un combat (comme avant)
        if random.random() < 0.25 and location_data.get("enemies"):
            exploration_result += "\nUn ennemi vous barre le chemin !"
            self.start_fight()
        return exploration_result
    
    def explore_zone(self, zone_id):
        """Change de zone et explore directement, ou explore la zone actuelle"""
        # Si zone_id est "explore", explorer la zone actuelle
        if zone_id == "explore":
            return self.explore_location()
        
        # Sinon, changer de zone et explorer
        try:
            result = self.set_zone(int(zone_id))
            if "non disponible" in result or "invalide" in result:
                return result
            # Explorer la nouvelle zone
            return self.explore_location()
        except (ValueError, TypeError):
            # Si zone_id n'est pas convertible en int, explorer la zone actuelle
            return self.explore_location()
    
    def start_fight(self, enemy=None):
        if self.current_location not in LOCATIONS:
            return "Pas d'ennemi ici !"
        location_data = LOCATIONS[self.current_location]
        available_enemies = location_data.get("enemies", [])
        
        # Ajouter les ennemis de la zone actuelle
        zone_info = self.get_zone_info()
        if self.current_zone == 2:  # Zone 2
            # Ajouter les ennemis spécifiques à la Zone 2
            zone2_enemies = list(ZONE_2_ENEMIES.keys())
            available_enemies = list(set(available_enemies + zone2_enemies))
        
        if not available_enemies and enemy is None:
            return "Pas d'ennemi disponible !"
        
        if random.random() < self.boss_spawn_chance and BOSSES:
            boss_name = random.choice(list(BOSSES.keys()))
            boss_data = BOSSES[boss_name].copy()
            self.current_enemy = {
                "name": boss_name,
                "is_boss": True,
                "health": boss_data.get("base_health", 250),
                "max_health": boss_data.get("base_health", 250),
                "attack": boss_data.get("base_attack", 35),
                "defense": boss_data.get("base_defense", 15),
                "level": boss_data.get("level", 15),
                "exp_reward": boss_data.get("exp_reward", 750),
                "gold_reward": boss_data.get("gold_reward", 400),
                "description": boss_data.get("description", ""),
                "icon": boss_data.get("icon", "👹")
            }
            self.is_boss_fight = True
            self.current_boss = boss_name
        else:
            enemy_name = enemy or random.choice(available_enemies)
            if enemy_name not in ENEMIES:
                return f"Ennemi {enemy_name} introuvable !"
            self.current_enemy = ENEMIES[enemy_name].copy()
            self.current_enemy["name"] = enemy_name
            self.current_enemy["is_boss"] = False
            self.current_enemy["max_health"] = self.current_enemy.get("health", 50)
            self.is_boss_fight = False
            self.current_boss = None
        
        self.enemy_health = self.current_enemy.get("health", 1)
        self.enemy_max_health = self.current_enemy.get("max_health", 1)
        self.enemy_level = self.current_enemy.get("level", 1)
        self.enemy_attack = self.current_enemy.get("attack", 5)
        self.enemy_defense = self.current_enemy.get("defense", 0)
        
        self.in_combat = True
        self.combat_turn = 0
        return f"Un combat a commencé contre {self.current_enemy['name']} !"
    
    def attack_enemy(self):
        if not self.in_combat or not self.current_enemy:
            return {"message": "Vous n'êtes pas en combat !", "action": "none"}

        rune_log = ""

        # Rune: regen au début du tour
        regen_val = self.get_rune_buff_value("regen")
        if regen_val > 0:
            healed = self.heal(regen_val)
            if healed > 0:
                rune_log += f"\n🌿 Régénération : +{healed} HP"

        # Rune: enemy_weaken (réduit ATK ennemi)
        weaken_val = self.get_rune_buff_value("enemy_weaken")
        enemy_atk = self.current_enemy.get("attack", 5)
        if weaken_val > 0:
            enemy_atk = max(1, enemy_atk - weaken_val)

        player_damage = self.player_stats["attack"] + random.randint(-2, 5)

        # Rune: attack_boost
        atk_boost = self.get_rune_buff_value("attack_boost")
        player_damage += atk_boost

        # Rune: berserk (+ATK -DEF)
        if self.has_rune_buff("berserk"):
            berserk_val = self.get_rune_buff_value("berserk")
            player_damage += berserk_val

        # Rune: all_boost
        all_boost_val = self.get_rune_buff_value("all_boost")
        player_damage += all_boost_val

        # Rune: bonus_damage_next (dégâts bonus à usage unique)
        bonus_dmg = self.get_rune_buff_value("bonus_damage_next")
        if bonus_dmg > 0:
            player_damage += bonus_dmg
            self.consume_rune_buff("bonus_damage_next")
            rune_log += "\n💥 Bonus de rune explosé !"

        enemy_defense = self.current_enemy.get("defense", 0)
        player_damage = max(1, player_damage - enemy_defense // 2)

        # Appliquer le multiplicateur de dégâts de l'arme équipée
        weapon_name = self.equipped.get("weapon")
        if weapon_name and weapon_name in ITEMS:
            weapon_data = ITEMS[weapon_name]
            damage_mult = weapon_data.get("damage_multiplier", 1.0)
            if damage_mult > 1.0:
                player_damage = int(player_damage * damage_mult)

        enemy_damage = enemy_atk + random.randint(-2, 3)

        # Rune: defense_boost + all_boost + berserk penalty
        player_defense = self.player_stats["defense"]
        def_boost = self.get_rune_buff_value("defense_boost") + all_boost_val
        if self.has_rune_buff("berserk"):
            berserk_penalty = RUNE_RECIPES.get("Fureur Primale", {}).get("penalty", 10)
            def_boost -= berserk_penalty
        enemy_damage = max(1, enemy_damage - (player_defense + def_boost) // 2)

        # Déterminer si c'est un coup critique
        is_critical = random.random() < 0.1
        # Rune: guaranteed_crit
        if self.has_rune_buff("guaranteed_crit"):
            is_critical = True
            crit_mult = self.get_rune_buff_value("guaranteed_crit")
            player_damage = int(player_damage * crit_mult)
            self.consume_rune_buff("guaranteed_crit")
            rune_log += "\n💀 Frappe de l'Ombre : critique garanti !"
        elif is_critical:
            player_damage = int(player_damage * 1.5)

        # Rune: multi_hit (chance de frapper plusieurs fois)
        extra_hits = 0
        if self.has_rune_buff("multi_hit") and random.random() < 0.4:
            extra_hits = self.get_rune_buff_value("multi_hit") - 1
            player_damage *= (extra_hits + 1)
            rune_log += f"\n🌀 Vortex : {extra_hits + 1} frappes !"

        self.current_enemy["health"] -= player_damage
        self.total_damage_dealt += player_damage
        self.enemy_health = self.current_enemy.get("health", 0)

        combat_log = f"Vous avez infligé {player_damage} dégâts !"
        if is_critical:
            combat_log = f"COUP CRITIQUE ! {player_damage} dégâts !"
        combat_log += rune_log

        # Tick des buffs de runes
        self.tick_rune_buffs()
        
        if self.current_enemy["health"] <= 0:
            loot = self.get_loot(self.current_enemy.get("level", 1))
            exp_gain = self.current_enemy.get("exp_reward", 50)
            gold_gain = self.current_enemy.get("gold_reward", 20)
            enemy_name = self.current_enemy["name"]
            
            self.player_stats["gold"] += gold_gain
            self.update_quest_progress(enemy_name=enemy_name)
            self.update_quest_progress(gold_gain=gold_gain)
            self.add_exp(exp_gain)
            self.total_enemies_defeated += 1
            
            if self.current_enemy.get("is_boss"):
                self.boss_defeated[self.current_enemy["name"]] = True
            
            combat_log += f"\n{self.current_enemy['name']} a été vaincu !\n"
            combat_log += f"Expérience gagnée : {exp_gain}\nOr gagné : {gold_gain}\n"
            
            if loot:
                for item, qty in loot.items():
                    self.inventory[item] = self.inventory.get(item, 0) + qty
                    combat_log += f"Butin : {item} (x{qty})\n"

            rune_drop = self.drop_rune(self.current_enemy.get("level", 1))
            if rune_drop:
                combat_log += f"Rune : {rune_drop}\n"

            card_drop = self.drop_card(self.current_enemy.get("level", 1), self.current_enemy.get("is_boss", False))
            if card_drop:
                combat_log += f"CARTE : {card_drop}\n"

            self.in_combat = False
            self.current_enemy = None
            self.enemy_health = 0
            self.enemy_max_health = 0
            return {
                "message": combat_log,
                "action": "kill",
                "enemy_defeated": True,
                "player_damage": player_damage,
                "enemy_damage": 0,
                "is_critical": is_critical
            }
        
        self.take_damage(enemy_damage)
        combat_log += f"\nL'ennemi a infligé {enemy_damage} dégâts !"
        
        # Save enemy health before potential cleanup
        current_enemy_health = self.current_enemy['health']
        
        combat_log += f"\nVie ennemie : {current_enemy_health}"
        combat_log += f"\nVotre vie : {self.player_stats['health']}"
        
        if self.player_stats['health'] <= 0:
            combat_log += "\nVous avez été vaincu !"
            self.in_combat = False
            self.current_enemy = None
            self.enemy_health = 0
            self.enemy_max_health = 0
            self.reset_health()
            return {
                "message": combat_log,
                "action": "attack",
                "player_damage": player_damage,
                "enemy_damage": enemy_damage,
                "is_critical": is_critical,
                "player_health": self.player_stats['health'],
                "enemy_health": current_enemy_health
            }
        
        self.combat_turn += 1
        return {
            "message": combat_log,
            "action": "attack",
            "player_damage": player_damage,
            "enemy_damage": enemy_damage,
            "is_critical": is_critical,
            "player_health": self.player_stats['health'],
            "enemy_health": current_enemy_health
        }
    
    def take_damage(self, amount):
        armor_bonus = self.temporary_buffs.get("defense", 0)
        damage = max(1, amount - (self.player_stats.get("armor", 0) + armor_bonus) // 2)
        self.player_stats["health"] -= damage
        self.total_damage_taken += damage
        if self.player_stats["health"] <= 0:
            self.player_stats["health"] = 0
            self.game_over = True
            self.in_combat = False
        return damage
    
    def heal(self, amount):
        healed = min(amount, self.player_stats["max_health"] - self.player_stats["health"])
        self.player_stats["health"] += healed
        return healed
    
    def add_exp(self, amount):
        self.player_stats["exp"] += amount
        # Mettre à jour la progression des quêtes d'XP
        self.update_quest_progress(exp_gain=amount)
        self.check_level_up()
    
    def check_level_up(self):
        while self.player_stats["exp"] >= self.player_stats["exp_for_next_level"]:
            self.player_stats["exp"] -= self.player_stats["exp_for_next_level"]
            self.player_stats["level"] += 1
            self.player_stats["exp_for_next_level"] = int(self.player_stats["exp_for_next_level"] * 1.1)
            
            # Vérifier les zones à débloquer
            self.check_unlocked_zones()
            
            if self.player_class in CLASSES:
                # Bonus de mana pour TOUTES les classes : 5 + 0.1% du mana max par niveau
                current_max_mana = self.player_stats.get("max_mana", 50)
                mana_bonus = 5 + (current_max_mana * 0.001)  # 0.1% = 0.001
                self.player_stats["mana"] += mana_bonus
                self.player_stats["max_mana"] += mana_bonus
                
                # Utilisation de match/case pour les bonus de classe
                match self.player_class:
                    case "Guerrier":
                        self.player_stats["defense"] += 2
                        self.player_stats["attack"] += 1
                        self.player_stats["health"] += 5
                        self.player_stats["max_health"] += 5
                    case "Mage":
                        self.player_stats["mana"] += 2
                        self.player_stats["max_mana"] += 2
                        self.player_stats["attack"] += 0.5
                        self.player_stats["health"] += 3
                        self.player_stats["max_health"] += 3
                    case "Archer":
                        self.player_stats["attack"] += 1.5
                        self.player_stats["mana"] += 1
                        self.player_stats["max_mana"] += 1
                        self.player_stats["health"] += 4
                        self.player_stats["max_health"] += 4
            
            self.unlock_progressive_skills()
    
    def get_loot(self, enemy_level):
        loot = {}
        if not LOOT_BY_RARITY:
            return loot

        # Récupérer la loot table de la zone (probabilités de base par rareté)
        zone_info = self.get_zone_info()
        if zone_info and 'loot_table' in zone_info:
            base_table = zone_info['loot_table']
        else:
            base_table = {
                "commun": 0.50,
                "rare": 0.30,
                "epique": 0.15,
                "legendaire": 0.05
            }

        # Scaling : 1.5% base + 2% de la proba de base par niveau du monstre
        # Ex: ennemi niv 1, commun (base 0.55) → 0.015 + 0.02 * 0.55 * 1 = 0.026 (2.6%)
        # Ex: ennemi niv 1 total ≈ 8% | niv 10 total ≈ 26% | niv 30 total ≈ 66%
        # Boost Colporteur : +0.5% global par achat (0.005 par boost)
        loot_boost_bonus = self.loot_boost_count * 0.005

        for rarity, base_prob in base_table.items():
            if rarity not in LOOT_BY_RARITY:
                continue
            drop_chance = 0.015 + (0.02 * base_prob * enemy_level) + loot_boost_bonus
            if random.random() < drop_chance:
                item = random.choice(LOOT_BY_RARITY[rarity])
                loot[item] = loot.get(item, 0) + 1

            # Zone 2 : même formule, pool d'items supplémentaire
            if self.current_zone == 2 and rarity in ZONE_2_LOOT:
                if random.random() < drop_chance:
                    zone2_item = random.choice(ZONE_2_LOOT[rarity])
                    loot[zone2_item] = loot.get(zone2_item, 0) + 1

        return loot
    
    def equip_item(self, item_name, item_type):
        if item_type not in self.equipped:
            return f"Type d'équipement {item_type} invalide !"
        if item_name not in ITEMS:
            return f"Objet {item_name} introuvable !"
        if item_name not in self.inventory or self.inventory[item_name] <= 0:
            return f"Vous n'avez pas {item_name} dans votre inventaire !"

        item_data = ITEMS[item_name]
        if item_data.get("type") != item_type:
            return f"{item_name} n'est pas un {item_type} !"

        required_level = item_data.get("required_level", 1)
        if self.player_stats["level"] < required_level:
            return f"Niveau insuffisant pour équiper {item_name} ! (Requis: niv {required_level}, Vous: niv {self.player_stats['level']})"
        
        if self.equipped[item_type]:
            old_item = self.equipped[item_type]
            self.inventory[old_item] = self.inventory.get(old_item, 0) + 1
            if old_item in ITEMS:
                old_data = ITEMS[old_item]
                for stat_key in ["attack_bonus", "defense_bonus", "health_bonus", "mana_bonus"]:
                    if stat_key in old_data:
                        match stat_key:
                            case "attack_bonus":
                                self.player_stats["attack"] = max(0, self.player_stats.get("attack", 0) - old_data[stat_key])
                            case "defense_bonus":
                                self.player_stats["defense"] = max(0, self.player_stats.get("defense", 0) - old_data[stat_key])
                            case "health_bonus":
                                self.player_stats["max_health"] = max(1, self.player_stats.get("max_health", 100) - old_data[stat_key])
                                self.player_stats["health"] = min(self.player_stats["health"], self.player_stats["max_health"])
                            case "mana_bonus":
                                self.player_stats["max_mana"] = max(0, self.player_stats.get("max_mana", 50) - old_data[stat_key])
                                self.player_stats["mana"] = min(self.player_stats["mana"], self.player_stats["max_mana"])
        
        self.equipped[item_type] = item_name
        self.inventory[item_name] -= 1
        
        for stat_key in ["attack_bonus", "defense_bonus", "health_bonus", "mana_bonus"]:
            if stat_key in item_data:
                match stat_key:
                    case "attack_bonus":
                        self.player_stats["attack"] = self.player_stats.get("attack", 0) + item_data[stat_key]
                    case "defense_bonus":
                        self.player_stats["defense"] = self.player_stats.get("defense", 0) + item_data[stat_key]
                    case "health_bonus":
                        self.player_stats["max_health"] = self.player_stats.get("max_health", 100) + item_data[stat_key]
                        self.player_stats["health"] = self.player_stats["max_health"]
                    case "mana_bonus":
                        self.player_stats["max_mana"] = self.player_stats.get("max_mana", 50) + item_data[stat_key]
                        self.player_stats["mana"] = self.player_stats["max_mana"]
        
        return f"Vous avez équipé {item_name} !"
    
    def unequip_item(self, item_type):
        if item_type not in self.equipped:
            return f"Type d'équipement {item_type} invalide !"
        if not self.equipped[item_type]:
            return f"Vous n'avez rien d'équipé en {item_type} !"
        
        item_name = self.equipped[item_type]
        item_data = ITEMS.get(item_name, {})
        
        for stat_key in ["attack_bonus", "defense_bonus", "health_bonus", "mana_bonus"]:
            if stat_key in item_data:
                match stat_key:
                    case "attack_bonus":
                        self.player_stats["attack"] = max(0, self.player_stats.get("attack", 0) - item_data[stat_key])
                    case "defense_bonus":
                        self.player_stats["defense"] = max(0, self.player_stats.get("defense", 0) - item_data[stat_key])
                    case "health_bonus":
                        self.player_stats["max_health"] = max(1, self.player_stats.get("max_health", 100) - item_data[stat_key])
                        self.player_stats["health"] = min(self.player_stats["health"], self.player_stats["max_health"])
                    case "mana_bonus":
                        self.player_stats["max_mana"] = max(0, self.player_stats.get("max_mana", 50) - item_data[stat_key])
                        self.player_stats["mana"] = min(self.player_stats["mana"], self.player_stats["max_mana"])
        
        self.equipped[item_type] = None
        self.inventory[item_name] = self.inventory.get(item_name, 0) + 1
        return f"Vous avez déséquipé {item_name} !"
    
    def use_item(self, item_name):
        if item_name not in self.inventory or self.inventory[item_name] <= 0:
            return f"Vous n'avez pas {item_name} !"
        if item_name not in ITEMS:
            return f"Objet {item_name} introuvable !"
        
        item_data = ITEMS[item_name]
        if item_data.get("type") != "consumable":
            return f"{item_name} n'est pas consommable !"
        
        effect_message = f"Vous avez utilisé {item_name} !\n"
        
        if item_data.get("heal"):
            healed = self.heal(item_data["heal"])
            effect_message += f"Santé restaurée : {healed} HP\n"
        
        if item_data.get("mana"):
            mana_restored = min(item_data["mana"], 
                              self.player_stats["max_mana"] - self.player_stats["mana"])
            self.player_stats["mana"] += mana_restored
            effect_message += f"Mana restauré : {mana_restored} MP\n"
        
        if item_data.get("exp_boost"):
            effect_message += f"Bonus d'expérience : {item_data['exp_boost']}%\n"
        
        if item_data.get("attack_boost"):
            boost = item_data["attack_boost"]
            duration = item_data.get("duration", 3)
            self.temporary_buffs["attack"] = boost
            effect_message += f"Attaque augmentée de +{boost} pendant {duration} tours !\n"
        
        if item_data.get("defense_boost"):
            boost = item_data["defense_boost"]
            duration = item_data.get("duration", 3)
            self.temporary_buffs["defense"] = boost
            effect_message += f"Défense augmentée de +{boost} pendant {duration} tours !\n"
        
        self.inventory[item_name] -= 1
        if self.inventory[item_name] <= 0:
            del self.inventory[item_name]
        
        return effect_message
    
    def visit_shop(self, shop_name):
        if shop_name not in SHOPS:
            return f"Magasin {shop_name} introuvable !"
        self.current_shop = shop_name
        shop_data = SHOPS[shop_name]
        return f"Bienvenue chez {shop_name} ! {shop_data.get('description', '')}"
    
    def buy_item(self, item_name):
        if not self.current_shop or self.current_shop not in SHOPS:
            return "Vous n'êtes pas dans un magasin !"
        shop_data = SHOPS[self.current_shop]
        shop_items = shop_data.get("items", [])
        if item_name not in shop_items:
            return f"{item_name} n'est pas vendu ici !"
        item_data = ITEMS.get(item_name, {})
        price = item_data.get("price", 0)
        if self.player_stats["gold"] < price:
            return f"Vous n'avez pas assez d'or ! (Prix: {price}, Or: {self.player_stats['gold']})"
        self.player_stats["gold"] -= price
        self.inventory[item_name] = self.inventory.get(item_name, 0) + 1
        return f"Vous avez acheté {item_name} pour {price} or !"
    
    def sell_item(self, item_name):
        if item_name not in self.inventory or self.inventory[item_name] <= 0:
            return f"Vous n'avez pas {item_name} !"
        if item_name not in ITEMS:
            return f"Objet {item_name} introuvable !"
        for slot, equipped_item in self.equipped.items():
            if equipped_item == item_name:
                return f"Vous devez d'abord déséquiper {item_name} !"
        item_data = ITEMS[item_name]
        price = item_data.get("sell_price", item_data.get("price", 10) // 2)
        self.player_stats["gold"] += price
        # Mettre à jour la progression des quêtes d'or
        self.update_quest_progress(gold_gain=price)
        self.inventory[item_name] -= 1
        if self.inventory[item_name] <= 0:
            del self.inventory[item_name]
        return f"Vous avez vendu {item_name} pour {price} or !"
    
    def get_current_shop_items(self):
        if not self.current_shop or self.current_shop not in SHOPS:
            return []
        shop_data = SHOPS[self.current_shop]
        shop_items = []
        for item_name in shop_data.get("items", []):
            item_data = ITEMS.get(item_name, {})
            shop_items.append({
                "name": item_name,
                "price": item_data.get("price", 0),
                "required_level": item_data.get("required_level", 1)
            })
        return shop_items
    
    def get_available_skills_for_level(self):
        available_skills = {}
        if self.player_class not in SKILLS:
            return available_skills
        
        # Ajouter les compétences de base (SKILLS)
        class_skills = SKILLS[self.player_class]
        current_level = self.player_stats["level"]
        for skill_name, skill_data in class_skills.items():
            unlock_level = skill_data.get("unlocked_at", 1)
            if current_level >= unlock_level:
                available_skills[skill_name] = skill_data
        
        # Ajouter les compétences progressives déjà apprises
        if self.player_class in self.skills_learned:
            for skill_name in self.skills_learned[self.player_class]:
                # Trouver les données de la compétence dans PROGRESSIVE_SKILLS
                if self.player_class in PROGRESSIVE_SKILLS:
                    for skill in PROGRESSIVE_SKILLS[self.player_class]:
                        if skill.get("name") == skill_name:
                            available_skills[skill_name] = skill
                            break
        
        return available_skills
    
    def get_upcoming_skills(self):
        upcoming = []
        if self.player_class not in PROGRESSIVE_SKILLS:
            return upcoming
        class_skills = PROGRESSIVE_SKILLS[self.player_class]
        current_level = self.player_stats["level"]
        for skill_data in class_skills:
            unlock_level = skill_data.get("level", 1)
            if current_level < unlock_level:
                upcoming.append({
                    "name": skill_data.get("name", ""),
                    "level": unlock_level,
                    "description": skill_data.get("description", ""),
                    "mana_cost": skill_data.get("mana_cost", 0),
                    "icon": skill_data.get("icon", "✨")
                })
        return upcoming
    
    def unlock_progressive_skills(self):
        if self.player_class not in PROGRESSIVE_SKILLS:
            return
        progressive = PROGRESSIVE_SKILLS[self.player_class]
        current_level = self.player_stats["level"]
        if self.player_class not in self.skills_learned:
            self.skills_learned[self.player_class] = {}
        for skill_data in progressive:
            skill_name = skill_data.get("name", "")
            unlock_level = skill_data.get("level", 1)
            if current_level >= unlock_level and skill_name:
                # Ne pas dupliquer si déjà débloquée
                if skill_name not in self.skills_learned[self.player_class]:
                    self.skills_learned[self.player_class][skill_name] = True
                    # Synchroniser avec unlocked_skills pour compatibilité
                    self.unlocked_skills[skill_name] = skill_data
    
    def get_navigation_map(self):
        if self.current_location not in LOCATIONS:
            return {
                "current": self.current_location,
                "current_name": "Localisation inconnue",
                "available_exits": []
            }
        location_data = LOCATIONS[self.current_location]
        exits = []
        if location_data.get("exits"):
            for direction, destination in location_data["exits"].items():
                if destination in LOCATIONS:
                    dest_data = LOCATIONS[destination]
                    exits.append({
                        "direction": direction.upper(),
                        "location_id": destination,
                        "location_name": dest_data.get("name", destination),
                        "description": dest_data.get("short_description", "")
                    })
        return {
            "current": self.current_location,
            "current_name": location_data.get("name", "Unknown"),
            "available_exits": exits
        }
    
    def get_world_map(self):
        locations_map = []
        for location_id in LOCATIONS.keys():
            location_data = LOCATIONS[location_id]
            x = location_data.get("x", 50)
            y = location_data.get("y", 50)
            locations_map.append({
                "id": location_id,
                "name": location_data.get("name", location_id),
                "visited": location_id in self.visited_locations,
                "is_current": location_id == self.current_location,
                "x": x,
                "y": y
            })
        return {
            "locations": locations_map,
            "visited_count": len(self.visited_locations),
            "total_count": len(LOCATIONS)
        }
    
    def reset_game(self):
        self.__init__()
        return "Le jeu a été réinitialisé !"
    
    def reset_health(self):
        self.player_stats["health"] = self.player_stats["max_health"]
        self.current_location = GAME_CONFIG["starting_location"]
    
    def get_player_stats(self):
        stats = {
            "level": self.player_stats["level"],
            "exp": self.player_stats["exp"],
            "exp_for_next_level": self.player_stats["exp_for_next_level"],
            "health": self.player_stats["health"],
            "max_health": self.player_stats["max_health"],
            "mana": self.player_stats["mana"],
            "max_mana": self.player_stats["max_mana"],
            "attack": self.player_stats["attack"],
            "defense": self.player_stats["defense"],
            "gold": self.player_stats["gold"],
            "weapon": self.equipped.get("weapon", "Mains nues"),
            "armor": self.equipped.get("armor", "Aucune"),
            "accessory": self.equipped.get("accessory", "Aucun")
        }
        return stats
    
    def get_player_stats_display(self):
        stats = self.get_player_stats()
        display = ""
        display += f"<strong>Niveau {stats['level']}</strong><br>"
        display += f"Santé: {stats['health']}/{stats['max_health']}<br>"
        display += f"Mana: {stats['mana']}/{stats['max_mana']}<br>"
        display += f"Attaque: {stats['attack']}<br>"
        display += f"Défense: {stats['defense']}<br>"
        display += f"Or: {stats['gold']}<br>"
        display += f"EXP: {stats['exp']}/{stats['exp_for_next_level']}"
        return display
    
    def get_inventory_info(self):
        inventory_info = {
            "items": self.inventory.copy(),
            "equipped": self.equipped.copy(),
            "inventory_count": sum(self.inventory.values())
        }
        return inventory_info
    
    def get_quests_display(self):
        quests_list = []
        if not DAILY_QUESTS:
            return quests_list
        for quest_id, quest_data in DAILY_QUESTS.items():
            target_count = quest_data.get('target_count', quest_data.get('target_gold', quest_data.get('target_exp', 1)))
            quest_info = {
                'id': quest_id,
                'name': quest_id,
                'icon': quest_data.get('icon', '📜'),
                'description': quest_data.get('description', 'Pas de description'),
                'reward_exp': quest_data.get('reward_exp', 0),
                'reward_gold': quest_data.get('reward_gold', 0),
                'reward_item': quest_data.get('reward_item', ''),
                'progress': self.quest_progress.get(quest_id, 0),
                'target': target_count,
                'completed': quest_id in self.completed_quests
            }
            quests_list.append(quest_info)
        return quests_list
    
    def close_shop(self):
        self.current_shop = None
        return "Magasin fermé."
    
    def talk_to_npc(self, npc_name):
        if npc_name not in NPCS_DIALOGUE:
            return f"NPC {npc_name} non trouvé."
        dialogue_text = NPCS_DIALOGUE[npc_name]
        return f"<p><strong>{npc_name}:</strong> {dialogue_text}</p>"

    def buy_loot_boost(self):
        """Achète un boost de chance de loot (+0.5% cumulable)."""
        cost = 1000 + (self.loot_boost_count * 500)
        if self.player_stats["gold"] < cost:
            return f"Or insuffisant ! (Prix: {cost} or, Vous: {self.player_stats['gold']} or)"
        self.player_stats["gold"] -= cost
        self.loot_boost_count += 1
        total_bonus = self.loot_boost_count * 0.5
        next_cost = 1000 + (self.loot_boost_count * 500)
        return f"🍀 Chance de loot améliorée ! +0.5% (Total: +{total_bonus}%) — Prochain boost: {next_cost} or"

    def get_loot_boost_info(self):
        """Retourne les infos du boost de loot pour l'affichage."""
        total_bonus = self.loot_boost_count * 0.5
        next_cost = 1000 + (self.loot_boost_count * 500)
        return {
            "count": self.loot_boost_count,
            "total_bonus": total_bonus,
            "next_cost": next_cost,
            "bonus_per_level": 0.5
        }

    def rest(self):
        if self.in_combat:
            return "Vous ne pouvez pas vous reposer pendant un combat !"
        heal_amount = int(self.player_stats["max_health"] * 0.3)
        mana_amount = int(self.player_stats["max_mana"] * 0.2)
        healed = self.heal(heal_amount)
        mana_restored = min(mana_amount, self.player_stats["max_mana"] - self.player_stats["mana"])
        self.player_stats["mana"] += mana_restored
        return f"Vous vous reposez... Santé restaurée : {healed} HP, Mana restauré : {mana_restored} MP."
    
    def use_skill(self, skill_name):
        if not self.player_class:
            return {"message": "Vous n'avez pas de classe!", "action": "none"}
        
        # Vérifier d'abord dans les compétences de base (SKILLS)
        class_skills = SKILLS.get(self.player_class, {})
        if skill_name in class_skills:
            skill_data = class_skills[skill_name]
        # Sinon vérifier dans les compétences progressives déjà apprises
        elif self.player_class in self.skills_learned and skill_name in self.skills_learned[self.player_class]:
            # Trouver la définition de la compétence dans PROGRESSIVE_SKILLS
            progressive_skills = PROGRESSIVE_SKILLS.get(self.player_class, [])
            skill_data = None
            for skill in progressive_skills:
                if skill.get("name") == skill_name:
                    skill_data = skill
                    break
            if skill_data is None:
                return {"message": f"Compétence {skill_name} non trouvée!", "action": "none"}
        else:
            return {"message": f"Compétence {skill_name} non trouvée ou non débloquée!", "action": "none"}
        
        # Extraire les données de la compétence
        mana_cost = skill_data.get("mana_cost", 0)
        if self.player_stats["mana"] < mana_cost:
            return {
                "message": f"Pas assez de mana! (Besoin: {mana_cost}, Mana: {self.player_stats['mana']})",
                "action": "none",
                "skill_type": "fail"
            }
        self.player_stats["mana"] -= mana_cost
        
        # Déterminer le type d'animation selon la compétence avec match/case
        match skill_name:
            case "Éclair" | "Boule de Feu" | "Météorite" | "Tir de Précision" | "Charge Furieuse" | "Coup Mortel" | "Coup Puissant":
                skill_type = "magic"
            case "Soin" | "Défense Renforcée" | "Esquive" | "Glaciation" | "Téléportation":
                skill_type = "heal"
            case "Tir Rapide" | "Pluie de Flèches" | "Volée Explosive":
                skill_type = "rapid"
            case _:
                skill_type = "skill"
        
        # Gestion soin
        if skill_data.get("heal"):
            healed = self.heal(skill_data["heal"])
            return {
                "message": f"Vous avez utilisé {skill_name}! Santé restaurée: {healed} HP",
                "action": "heal",
                "skill_type": skill_type,
                "heal_amount": healed
            }
        
        # Gestion défense boost
        if skill_data.get("defense_boost"):
            boost = skill_data["defense_boost"]
            duration = skill_data.get("duration", 3)
            self.temporary_buffs["defense"] = boost
            return {
                "message": f"Vous avez utilisé {skill_name}! Défense augmentée de +{boost} pendant {duration} tours!",
                "action": "defense_boost",
                "skill_type": skill_type,
                "boost_amount": boost
            }
        
        # Gestion attaque boost
        if skill_data.get("attack_multiplier"):
            boost_mult = skill_data["attack_multiplier"]
            duration = skill_data.get("duration", 2)
            bonus = int(self.player_stats["attack"] * (boost_mult - 1))
            self.temporary_buffs["attack"] = bonus
            return {
                "message": f"Vous avez utilisé {skill_name}! Attaque augmentée de +{bonus} pendant {duration} tours!",
                "action": "attack_boost",
                "skill_type": skill_type,
                "boost_amount": bonus
            }
        
        # Gestion damage reduction
        if skill_data.get("damage_reduction"):
            reduction = skill_data.get("damage_reduction", 0.5)
            duration = skill_data.get("duration", 2)
            self.temporary_buffs["defense"] = int(self.player_stats.get("defense", 0) * reduction)
            return {
                "message": f"Vous avez utilisé {skill_name}! Dégâts réduits de {int(reduction * 100)}% pendant {duration} tours!",
                "action": "damage_reduction",
                "skill_type": skill_type
            }
        
        damage_multiplier = skill_data.get("damage_multiplier", 1.0)
        hits = skill_data.get("hits", 1)
        total_damage = 0
        
        if self.in_combat and self.current_enemy:
            result = f"Vous avez utilisé {skill_name}!\n"
            for i in range(hits):
                if not self.current_enemy or self.current_enemy["health"] <= 0:
                    break
                hit_damage = int(self.player_stats["attack"] * damage_multiplier)
                hit_damage = max(1, hit_damage - self.current_enemy.get("defense", 0) // 2)
                # Appliquer le multiplicateur de dégâts de l'arme équipée
                weapon_name = self.equipped.get("weapon")
                if weapon_name and weapon_name in ITEMS:
                    weapon_mult = ITEMS[weapon_name].get("damage_multiplier", 1.0)
                    if weapon_mult > 1.0:
                        hit_damage = int(hit_damage * weapon_mult)
                # Rune: skill_double
                if self.has_rune_buff("skill_double"):
                    skill_mult = self.get_rune_buff_value("skill_double")
                    hit_damage = int(hit_damage * skill_mult)
                self.current_enemy["health"] -= hit_damage
                total_damage += hit_damage
                result += f"Hit {i+1}: {hit_damage} dégâts\n"

            # Tick des buffs de runes
            self.tick_rune_buffs()
            self.enemy_health = self.current_enemy.get("health", 0)
            result += f"Dégâts totaux: {total_damage}\n"
            
            # Déterminer si c'est un coup critique pour les compétences
            is_critical = random.random() < 0.15
            
            if self.current_enemy["health"] <= 0:
                loot = self.get_loot(self.current_enemy.get("level", 1))
                exp_gain = self.current_enemy.get("exp_reward", 50)
                gold_gain = self.current_enemy.get("gold_reward", 20)
                enemy_name = self.current_enemy["name"]
                
                self.player_stats["gold"] += gold_gain
                self.update_quest_progress(enemy_name=enemy_name)
                self.update_quest_progress(gold_gain=gold_gain)
                self.add_exp(exp_gain)
                self.total_enemies_defeated += 1
                
                if self.current_enemy.get("is_boss"):
                    self.boss_defeated[self.current_enemy["name"]] = True
                
                result += f"\n{self.current_enemy['name']} a été vaincu!\n"
                result += f"Expérience gagnée: {exp_gain}, Or gagné: {gold_gain}\n"
                
                if loot:
                    for item, qty in loot.items():
                        self.inventory[item] = self.inventory.get(item, 0) + qty
                        result += f"Butin: {item} (x{qty})\n"

                rune_drop = self.drop_rune(self.current_enemy.get("level", 1))
                if rune_drop:
                    result += f"Rune : {rune_drop}\n"

                card_drop = self.drop_card(self.current_enemy.get("level", 1), self.current_enemy.get("is_boss", False))
                if card_drop:
                    result += f"CARTE : {card_drop}\n"

                self.in_combat = False
                self.current_enemy = None
                self.enemy_health = 0
                self.enemy_max_health = 0
                return {
                    "message": result,
                    "action": "kill",
                    "skill_type": skill_type,
                    "total_damage": total_damage,
                    "is_critical": is_critical,
                    "enemy_defeated": True
                }
            # L'ennemi riposte si encore en vie
            enemy_atk = self.current_enemy.get("attack", 5)
            weaken_val = self.get_rune_buff_value("enemy_weaken")
            if weaken_val > 0:
                enemy_atk = max(1, enemy_atk - weaken_val)

            enemy_damage = enemy_atk + random.randint(-2, 3)
            player_defense = self.player_stats["defense"]
            def_boost = self.get_rune_buff_value("defense_boost") + self.get_rune_buff_value("all_boost")
            if self.has_rune_buff("berserk"):
                berserk_penalty = RUNE_RECIPES.get("Fureur Primale", {}).get("penalty", 10)
                def_boost -= berserk_penalty
            enemy_damage = max(1, enemy_damage - (player_defense + def_boost) // 2)

            self.take_damage(enemy_damage)
            result += f"\n{self.current_enemy['name']} riposte et inflige {enemy_damage} dégâts !"

            if self.player_stats['health'] <= 0:
                result += "\nVous avez été vaincu !"
                self.in_combat = False
                self.current_enemy = None
                self.enemy_health = 0
                self.enemy_max_health = 0
                self.reset_health()
                return {
                    "message": result,
                    "action": "skill_attack",
                    "skill_type": skill_type,
                    "total_damage": total_damage,
                    "enemy_damage": enemy_damage,
                    "is_critical": is_critical,
                    "hits": hits,
                    "player_health": self.player_stats['health'],
                    "enemy_health": self.enemy_health
                }

            self.combat_turn += 1
            return {
                "message": result,
                "action": "skill_attack",
                "skill_type": skill_type,
                "total_damage": total_damage,
                "enemy_damage": enemy_damage,
                "is_critical": is_critical,
                "hits": hits,
                "player_health": self.player_stats['health'],
                "enemy_health": self.current_enemy.get("health", 0)
            }
        return {
            "message": f"Vous avez utilisé {skill_name}! (Hors combat)",
            "action": "none",
            "skill_type": skill_type
        }
    
    def flee_combat(self):
        if not self.in_combat or not self.current_enemy:
            return "Vous n'êtes pas en combat!"
        if random.random() < 0.5:
            self.in_combat = False
            self.current_enemy = None
            self.enemy_health = 0
            self.enemy_max_health = 0
            return "Vous avez réussi à fuir!"
        enemy_damage = self.current_enemy.get("attack", 5) + random.randint(-2, 3)
        self.take_damage(enemy_damage)
        return f"Vous n'avez pas pu fuir! L'ennemi vous a infligé {enemy_damage} dégâts."
    
    def drop_item(self, item_name):
        if item_name not in self.inventory or self.inventory[item_name] <= 0:
            return False
        self.inventory[item_name] -= 1
        if self.inventory[item_name] <= 0:
            del self.inventory[item_name]
        return True
    
    def unlock_zone(self, zone_id):
        """Débloque une zone"""
        if zone_id not in self.unlocked_zones and zone_id in ZONES:
            zone = ZONES[zone_id]
            if self.player_stats['level'] >= zone.get('required_level', 999):
                self.unlocked_zones.append(zone_id)
                return f"Zone {zone_id} débloquée !"
        return f"Impossible de débloquer la zone {zone_id}"

    def check_unlocked_zones(self):
        """Vérifie et débloque toutes les zones disponibles selon le niveau"""
        for zone_id, zone_data in ZONES.items():
            if zone_id not in self.unlocked_zones:
                required_level = zone_data.get('required_level', 999)
                if self.player_stats['level'] >= required_level:
                    self.unlock_zone(zone_id)

    def set_zone(self, zone_id):
        """Change de zone"""
        if zone_id in self.unlocked_zones and zone_id in ZONES:
            self.current_zone = zone_id
            return f"Zone changée vers {ZONES[zone_id]['name']}"
        return f"Zone {zone_id} non disponible"

    def change_zone(self, zone_id):
        """Change de zone avec vérifications"""
        try:
            zone_id = int(zone_id)
        except:
            return f"Zone invalide: {zone_id}"
        return self.set_zone(zone_id)

    def get_zone_info(self, zone_id=None):
        """Retourne les infos d'une zone ou de la zone actuelle"""
        zone_id = zone_id or self.current_zone
        if zone_id in ZONES:
            return ZONES[zone_id]
        return None

    def set_difficulty(self, difficulty):
        if difficulty not in DIFFICULTY_SETTINGS:
            return "Difficulté invalide!"
        self.difficulty = difficulty
        
        # Utilisation de match/case pour les paramètres de difficulté
        match difficulty:
            case "facile":
                self.boss_spawn_chance = 0.05
            case "moyen":
                self.boss_spawn_chance = 0.15
            case "difficile":
                self.boss_spawn_chance = 0.30
        
        return f"Difficulté définie à {difficulty}!"
        

    def update_quest_progress(self, enemy_name=None, exp_gain=0, gold_gain=0):
        """Met à jour la progression de toutes les quêtes actives"""
        if not DAILY_QUESTS:
            return
        
        # Protection contre les valeurs invalides
        if exp_gain < 0:
            exp_gain = 0
        if gold_gain < 0:
            gold_gain = 0
        
        for quest_id, quest_data in DAILY_QUESTS.items():
            # Skip already completed quests
            if quest_id in self.completed_quests:
                continue
            
            # Initialize progress if not exists
            if quest_id not in self.quest_progress:
                self.quest_progress[quest_id] = 0
            
            # Utilisation de match/case pour les types de quêtes
            if 'target_enemy' in quest_data:
                target_enemy = quest_data['target_enemy']
                if enemy_name == target_enemy:
                    self.quest_progress[quest_id] += 1
                    if self.quest_progress[quest_id] >= quest_data.get('target_count', 1):
                        self.complete_quest(quest_id)
            else:
                match quest_data.get('type'):
                    case 'gold':
                        target_gold = quest_data.get('target_gold', 0)
                        current_gold = self.quest_progress.get(quest_id, 0)
                        new_gold = current_gold + gold_gain
                        self.quest_progress[quest_id] = new_gold
                        if new_gold >= target_gold:
                            self.complete_quest(quest_id)
                    case 'exp':
                        target_exp = quest_data.get('target_exp', 0)
                        current_exp = self.quest_progress.get(quest_id, 0)
                        new_exp = current_exp + exp_gain
                        self.quest_progress[quest_id] = new_exp
                        if new_exp >= target_exp:
                            self.complete_quest(quest_id)
    
    def complete_quest(self, quest_id):
        if quest_id not in DAILY_QUESTS:
            return False
        if quest_id in self.completed_quests:
            return False
        
        quest_data = DAILY_QUESTS[quest_id]
        
        # Vérifier que la quête est effectivement accomplie avec match/case
        quest_completed = False
        if 'target_enemy' in quest_data:
            # Quête de type "tuer X ennemis"
            target_count = quest_data.get('target_count', 1)
            if self.quest_progress.get(quest_id, 0) >= target_count:
                quest_completed = True
        else:
            match quest_data.get('type'):
                case 'gold':
                    # Quête de type "amasser X or"
                    target_gold = quest_data.get('target_gold', 0)
                    if self.quest_progress.get(quest_id, 0) >= target_gold:
                        quest_completed = True
                case 'exp':
                    # Quête de type "gagner X XP"
                    target_exp = quest_data.get('target_exp', 0)
                    if self.quest_progress.get(quest_id, 0) >= target_exp:
                        quest_completed = True
                case _:
                    # Quête sans type spécifique, on la considère comme accomplie
                    quest_completed = True
        
        if not quest_completed:
            return False
        
        # Marquer la quête comme complétée AVANT de donner les récompenses
        # pour éviter la récursion infinie
        self.completed_quests.append(quest_id)
        
        exp_reward = quest_data.get("reward_exp", 0)
        gold_reward = quest_data.get("reward_gold", 0)
        self.add_exp(exp_reward)  # add_exp met à jour les quêtes d'XP
        self.player_stats["gold"] += gold_reward
        # NOTE: On ne met PAS à jour les quêtes avec les récompenses pour éviter:
        # 1. La récursion infinie (récompense or → quête or → nouvelle récompense → ...)
        # 2. L'exploitation (compléter une quête → recevoir or → compléter quête or → recevoir plus or)
        if quest_data.get("reward_item"):
            reward_item = quest_data["reward_item"]
            self.inventory[reward_item] = self.inventory.get(reward_item, 0) + 1
        return True
    
    def check_win(self):
        if self.player_stats["level"] >= 50:
            self.game_won = True
        if len(self.boss_defeated) >= len(BOSSES):
            self.game_won = True
        return self.game_won

    # ==================== SYSTÈME DE RUNES ====================

    def toggle_runes(self):
        self.show_runes = not self.show_runes
        return self.show_runes

    def drop_rune(self, enemy_level):
        """Tente de faire tomber une rune après un combat."""
        if random.random() > RUNE_DROP_CHANCE:
            return None
        rune_name = random.choice(list(RUNES.keys()))
        # Rareté basée sur le niveau de l'ennemi
        weights = []
        for rarity_data in RUNE_RARITIES.values():
            weights.append(rarity_data["drop_weight"])
        # Ennemis de haut niveau = plus de chance de runes majeures/anciennes
        if enemy_level >= 15:
            weights = [40, 35, 25]
        elif enemy_level >= 8:
            weights = [50, 35, 15]
        rarity = random.choices(list(RUNE_RARITIES.keys()), weights=weights, k=1)[0]
        rune_key = f"{rune_name}|{rarity}"
        self.rune_inventory[rune_key] = self.rune_inventory.get(rune_key, 0) + 1
        rune_data = RUNES[rune_name]
        rarity_data = RUNE_RARITIES[rarity]
        return f"{rarity_data['icon']} {rune_data['icon']} {rune_name} ({rarity})"

    def craft_rune(self, recipe_name):
        """Combine 2 runes pour créer un buff temporaire."""
        if recipe_name not in RUNE_RECIPES:
            return "Recette inconnue !"
        recipe = RUNE_RECIPES[recipe_name]
        needed_runes = recipe["runes"]
        # Vérifier que le joueur possède les runes requises (toute rareté)
        found_runes = []
        used_keys = []
        for needed in needed_runes:
            best_key = None
            best_mult = 0
            for key, qty in self.rune_inventory.items():
                rune_name = key.split("|")[0]
                rune_rarity = key.split("|")[1]
                if rune_name == needed and qty > 0:
                    mult = RUNE_RARITIES[rune_rarity]["multiplier"]
                    if mult > best_mult:
                        best_mult = mult
                        best_key = key
            if best_key:
                found_runes.append(best_key)
                used_keys.append(best_key)
            else:
                return f"Rune manquante : {needed}"
        if len(found_runes) < len(needed_runes):
            return "Runes insuffisantes pour cette recette."
        # Consommer les runes
        best_multiplier = 1.0
        for key in used_keys:
            rune_rarity = key.split("|")[1]
            best_multiplier = max(best_multiplier, RUNE_RARITIES[rune_rarity]["multiplier"])
            self.rune_inventory[key] -= 1
            if self.rune_inventory[key] <= 0:
                del self.rune_inventory[key]
        # Créer le buff
        buff = {
            "name": recipe_name,
            "icon": recipe["icon"],
            "effect": recipe["effect"],
            "value": int(recipe["value"] * best_multiplier),
            "duration": recipe["duration"],
            "turns_left": recipe["duration"],
            "combat_text": recipe["combat_text"]
        }
        # Remplacer ou ajouter le buff
        self.active_rune_buffs = [b for b in self.active_rune_buffs if b["name"] != recipe_name]
        self.active_rune_buffs.append(buff)
        mult_text = f" (x{best_multiplier})" if best_multiplier > 1.0 else ""
        return f"{recipe['icon']} {recipe_name} activé pour {recipe['duration']} tours{mult_text} !"

    def get_rune_buff_summary(self):
        """Retourne un résumé des buffs de runes actifs."""
        return [{"name": b["name"], "icon": b["icon"], "turns_left": b["turns_left"]}
                for b in self.active_rune_buffs]

    def tick_rune_buffs(self):
        """Réduit la durée des buffs de runes d'un tour."""
        for buff in self.active_rune_buffs:
            buff["turns_left"] -= 1
        self.active_rune_buffs = [b for b in self.active_rune_buffs if b["turns_left"] > 0]

    def get_rune_buff_value(self, effect_type):
        """Retourne la valeur cumulée d'un type d'effet de rune."""
        total = 0
        for buff in self.active_rune_buffs:
            if buff["effect"] == effect_type:
                total += buff["value"]
        return total

    def has_rune_buff(self, effect_type):
        """Vérifie si un type de buff de rune est actif."""
        return any(b["effect"] == effect_type for b in self.active_rune_buffs)

    def consume_rune_buff(self, effect_type):
        """Consomme un buff de rune à usage unique."""
        self.active_rune_buffs = [b for b in self.active_rune_buffs if b["effect"] != effect_type]

    def get_runes_display(self):
        """Retourne les données de runes pour l'affichage."""
        inventory = []
        for key, qty in self.rune_inventory.items():
            parts = key.split("|")
            rune_name = parts[0]
            rune_rarity = parts[1] if len(parts) > 1 else "mineure"
            rune_data = RUNES.get(rune_name, {})
            rarity_data = RUNE_RARITIES.get(rune_rarity, {})
            inventory.append({
                "key": key,
                "name": rune_name,
                "icon": rune_data.get("icon", "?"),
                "rarity": rune_rarity,
                "rarity_icon": rarity_data.get("icon", ""),
                "description": rune_data.get("description", ""),
                "quantity": qty
            })
        recipes = []
        for name, data in RUNE_RECIPES.items():
            can_craft = True
            for needed in data["runes"]:
                has_it = any(k.split("|")[0] == needed and v > 0 for k, v in self.rune_inventory.items())
                if not has_it:
                    can_craft = False
                    break
            recipes.append({
                "name": name,
                "icon": data["icon"],
                "description": data["description"],
                "runes": [RUNES.get(r, {}).get("icon", "?") + " " + r.replace("Rune de ", "") for r in data["runes"]],
                "effect": data["effect"],
                "value": data["value"],
                "duration": data["duration"],
                "can_craft": can_craft
            })
        return {
            "inventory": inventory,
            "recipes": recipes,
            "active_buffs": self.active_rune_buffs
        }

    # ==================== SYSTÈME DE CARTES ====================

    def drop_card(self, enemy_level, is_boss=False):
        """Tente de faire tomber une carte après un combat."""
        # Chance de base + loot boost du Colporteur + bonus légendaire
        base_chance = CARD_DROP_CHANCE
        loot_boost_bonus = self.loot_boost_count * 0.005
        # Bonus légendaire : somme des probabilités légendaires de la loot table
        legendary_bonus = 0
        zone_info = self.get_zone_info()
        if zone_info and 'loot_table' in zone_info:
            legendary_prob = zone_info['loot_table'].get('legendaire', 0)
        else:
            legendary_prob = 0.05
        legendary_bonus = 0.01 * legendary_prob * enemy_level

        drop_chance = base_chance + loot_boost_bonus + legendary_bonus
        if is_boss:
            drop_chance *= CARD_BOSS_MULTIPLIER

        if random.random() >= drop_chance:
            return None

        # Sélectionner une carte selon la rareté
        # Plus l'ennemi est fort, plus les cartes épiques/légendaires sont probables
        if enemy_level >= 20 or (is_boss and random.random() < 0.3):
            possible = [name for name, data in CARDS.items() if data['rarity'] in ('epique', 'legendaire')]
        elif enemy_level >= 10 or is_boss:
            possible = [name for name, data in CARDS.items() if data['rarity'] in ('rare', 'epique')]
        else:
            possible = [name for name, data in CARDS.items() if data['rarity'] == 'rare']

        if not possible:
            return None

        card_name = random.choice(possible)
        self.card_inventory[card_name] = self.card_inventory.get(card_name, 0) + 1
        card_data = CARDS[card_name]
        return f"{card_data['icon']} {card_name}"

    def use_card(self, card_name):
        """Utilise une carte pour appliquer son bonus permanent."""
        if card_name not in CARDS:
            return "Carte inconnue !"
        if card_name not in self.card_inventory or self.card_inventory[card_name] <= 0:
            return f"Vous n'avez pas de {card_name} !"

        card_data = CARDS[card_name]
        stat = card_data["stat"]
        value = card_data["value"]

        # Consommer la carte
        self.card_inventory[card_name] -= 1
        if self.card_inventory[card_name] <= 0:
            del self.card_inventory[card_name]

        # Appliquer le bonus permanent
        if stat == "loot_boost":
            self.loot_boost_count += int(value / 0.5) if value >= 0.5 else 1
            self.cards_used.append(card_name)
            return f"{card_data['icon']} {card_name} utilisée ! Chance de loot +{value}% permanente !"
        elif stat == "max_health":
            self.player_stats["max_health"] += value
            self.player_stats["health"] += value
        elif stat == "max_mana":
            self.player_stats["max_mana"] += value
            self.player_stats["mana"] += value
        elif stat == "attack":
            self.player_stats["attack"] += value
        elif stat == "defense":
            self.player_stats["defense"] += value

        self.cards_used.append(card_name)
        stat_names = {"attack": "Attaque", "defense": "Défense", "max_health": "PV max", "max_mana": "Mana max"}
        return f"{card_data['icon']} {card_name} utilisée ! {stat_names.get(stat, stat)} +{value} permanent !"

    def get_cards_display(self):
        """Retourne les cartes pour l'affichage."""
        cards = []
        for name, qty in self.card_inventory.items():
            data = CARDS.get(name, {})
            cards.append({
                "name": name,
                "icon": data.get("icon", "🃏"),
                "rarity": data.get("rarity", "rare"),
                "description": data.get("description", ""),
                "lore": data.get("lore", ""),
                "quantity": qty,
                "stat": data.get("stat", ""),
                "value": data.get("value", 0)
            })
        return cards

    # ==================== SYSTÈME DE SCORE ====================

    def get_score_details(self):
        """Calcule le détail du score par catégorie."""
        details = {}

        details["Niveau"] = {
            "value": self.player_stats["level"],
            "points": self.player_stats["level"] * 100,
            "icon": "⭐"
        }

        details["Ennemis vaincus"] = {
            "value": self.total_enemies_defeated,
            "points": self.total_enemies_defeated * 10,
            "icon": "⚔️"
        }

        details["Boss vaincus"] = {
            "value": len(self.boss_defeated),
            "points": len(self.boss_defeated) * 500,
            "icon": "👹"
        }

        details["Quêtes complétées"] = {
            "value": len(self.completed_quests),
            "points": len(self.completed_quests) * 200,
            "icon": "📜"
        }

        details["Or accumulé"] = {
            "value": self.player_stats["gold"],
            "points": self.player_stats["gold"] // 5,
            "icon": "💰"
        }

        details["Dégâts infligés"] = {
            "value": self.total_damage_dealt,
            "points": int(self.total_damage_dealt * 0.5),
            "icon": "💥"
        }

        legendary_count = sum(
            1 for item, qty in self.inventory.items()
            if item in ITEMS and ITEMS[item].get("rarity") == "legendaire"
            for _ in range(qty)
        )
        for slot, equipped_item in self.equipped.items():
            if equipped_item and equipped_item in ITEMS and ITEMS[equipped_item].get("rarity") == "legendaire":
                legendary_count += 1

        details["Items légendaires"] = {
            "value": legendary_count,
            "points": legendary_count * 300,
            "icon": "🏆"
        }

        details["Cartes utilisées"] = {
            "value": len(self.cards_used),
            "points": len(self.cards_used) * 150,
            "icon": "🃏"
        }

        details["Zones explorées"] = {
            "value": len(self.unlocked_zones),
            "points": len(self.unlocked_zones) * 100,
            "icon": "🗺️"
        }

        runes_count = sum(self.rune_inventory.values())
        details["Runes collectées"] = {
            "value": runes_count,
            "points": runes_count * 20,
            "icon": "🔮"
        }

        return details

    def get_score(self):
        """Retourne le score total du joueur."""
        details = self.get_score_details()
        total = sum(d["points"] for d in details.values())

        if total < 500:
            rank = "Novice"
            rank_icon = "🥉"
        elif total < 2000:
            rank = "Apprenti"
            rank_icon = "🥉"
        elif total < 5000:
            rank = "Aventurier"
            rank_icon = "🥈"
        elif total < 10000:
            rank = "Héros"
            rank_icon = "🥈"
        elif total < 20000:
            rank = "Champion"
            rank_icon = "🥇"
        elif total < 40000:
            rank = "Légende"
            rank_icon = "🥇"
        else:
            rank = "Dieu"
            rank_icon = "👑"

        return {
            "total": total,
            "rank": rank,
            "rank_icon": rank_icon,
            "details": details
        }

    def toggle_options(self):
        self.show_options = not self.show_options
        return self.show_options
    
    def toggle_inventory(self):
        self.show_inventory = not self.show_inventory
        return self.show_inventory
    
    def toggle_quests(self):
        self.show_quests = not self.show_quests
        return self.show_quests
    
    def toggle_skills(self):
        self.show_skills = not self.show_skills
        return self.show_skills
