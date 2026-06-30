
# Read the original file
with open('/mnt/agents/upload/game_engine.py', 'r', encoding='utf-8') as f:
    original = f.read()

# Fix 1: attack_enemy - use local reference and add guards
old_attack_enemy = '''    def attack_enemy(self):
        if not self.in_combat or not self.current_enemy:
            return {"message": "Vous n'êtes pas en combat !", "action": "none"}
        
        player_damage = self.player_stats["attack"] + random.randint(-2, 5)
        enemy_defense = self.current_enemy.get("defense", 0)
        player_damage = max(1, player_damage - enemy_defense // 2)
        
        enemy_damage = self.current_enemy.get("attack", 5) + random.randint(-2, 3)
        player_defense = self.player_stats["defense"]
        enemy_damage = max(1, enemy_damage - player_defense // 2)
        
        # Déterminer si c'est un coup critique (10% de chance)
        is_critical = random.random() < 0.1
        if is_critical:
            player_damage = int(player_damage * 1.5)
        
        self.current_enemy["health"] -= player_damage
        self.total_damage_dealt += player_damage
        self.enemy_health = self.current_enemy.get("health", 0)
        
        combat_log = f"Vous avez infligé {player_damage} dégâts !"
        if is_critical:
            combat_log = f"COUP CRITIQUE ! {player_damage} dégâts !"
        
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
            
            combat_log += f"\\n{self.current_enemy['name']} a été vaincu !\\n"
            combat_log += f"Expérience gagnée : {exp_gain}\\nOr gagné : {gold_gain}\\n"
            
            if loot:
                for item, qty in loot.items():
                    self.inventory[item] = self.inventory.get(item, 0) + qty
                    combat_log += f"Butin : {item} (x{qty})\\n"
            
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
        combat_log += f"\\nL'ennemi a infligé {enemy_damage} dégâts !"
        
        # Save enemy health before potential cleanup
        current_enemy_health = self.current_enemy['health']
        
        combat_log += f"\\nVie ennemie : {current_enemy_health}"
        combat_log += f"\\nVotre vie : {self.player_stats['health']}"
        
        if self.player_stats['health'] <= 0:
            combat_log += "\\nVous avez été vaincu !"
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
        }'''

new_attack_enemy = '''    def attack_enemy(self):
        if not self.in_combat or not self.current_enemy:
            return {"message": "Vous n'êtes pas en combat !", "action": "none"}
        
        # Garder une référence locale pour éviter les problèmes de concurrence
        enemy = self.current_enemy
        
        player_damage = self.player_stats["attack"] + random.randint(-2, 5)
        enemy_defense = enemy.get("defense", 0)
        player_damage = max(1, player_damage - enemy_defense // 2)
        
        enemy_damage = enemy.get("attack", 5) + random.randint(-2, 3)
        player_defense = self.player_stats["defense"]
        enemy_damage = max(1, enemy_damage - player_defense // 2)
        
        # Déterminer si c'est un coup critique (10% de chance)
        is_critical = random.random() < 0.1
        if is_critical:
            player_damage = int(player_damage * 1.5)
        
        enemy["health"] -= player_damage
        self.total_damage_dealt += player_damage
        self.enemy_health = enemy.get("health", 0)
        
        combat_log = f"Vous avez infligé {player_damage} dégâts !"
        if is_critical:
            combat_log = f"COUP CRITIQUE ! {player_damage} dégâts !"
        
        if enemy["health"] <= 0:
            loot = self.get_loot(enemy.get("level", 1))
            exp_gain = enemy.get("exp_reward", 50)
            gold_gain = enemy.get("gold_reward", 20)
            enemy_name = enemy["name"]
            
            self.player_stats["gold"] += gold_gain
            self.update_quest_progress(enemy_name=enemy_name)
            self.update_quest_progress(gold_gain=gold_gain)
            self.add_exp(exp_gain)
            self.total_enemies_defeated += 1
            
            if enemy.get("is_boss"):
                self.boss_defeated[enemy["name"]] = True
            
            combat_log += f"\\n{enemy['name']} a été vaincu !\\n"
            combat_log += f"Expérience gagnée : {exp_gain}\\nOr gagné : {gold_gain}\\n"
            
            if loot:
                for item, qty in loot.items():
                    self.inventory[item] = self.inventory.get(item, 0) + qty
                    combat_log += f"Butin : {item} (x{qty})\\n"
            
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
        combat_log += f"\\nL'ennemi a infligé {enemy_damage} dégâts !"
        
        # Vérifier si le combat est toujours valide après les dégâts
        if not self.in_combat or not self.current_enemy:
            return {
                "message": combat_log,
                "action": "attack",
                "player_damage": player_damage,
                "enemy_damage": enemy_damage,
                "is_critical": is_critical,
                "player_health": self.player_stats['health'],
                "enemy_health": 0
            }
        
        # Save enemy health before potential cleanup
        current_enemy_health = self.current_enemy.get('health', 0)
        
        combat_log += f"\\nVie ennemie : {current_enemy_health}"
        combat_log += f"\\nVotre vie : {self.player_stats['health']}"
        
        if self.player_stats['health'] <= 0:
            combat_log += "\\nVous avez été vaincu !"
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
        }'''

fixed = original.replace(old_attack_enemy, new_attack_enemy)

# Fix 2: use_skill - break multi-hit loop if enemy dies
old_use_skill_loop = '''            if self.in_combat and self.current_enemy:
            result = f"Vous avez utilisé {skill_name}!\\n"
            for i in range(hits):
                hit_damage = int(self.player_stats["attack"] * damage_multiplier)
                hit_damage = max(1, hit_damage - self.current_enemy.get("defense", 0) // 2)
                self.current_enemy["health"] -= hit_damage
                total_damage += hit_damage
                result += f"Hit {i+1}: {hit_damage} dégâts\\n"'''

new_use_skill_loop = '''            if self.in_combat and self.current_enemy:
            result = f"Vous avez utilisé {skill_name}!\\n"
            for i in range(hits):
                if not self.current_enemy or self.current_enemy["health"] <= 0:
                    break
                hit_damage = int(self.player_stats["attack"] * damage_multiplier)
                hit_damage = max(1, hit_damage - self.current_enemy.get("defense", 0) // 2)
                self.current_enemy["health"] -= hit_damage
                total_damage += hit_damage
                result += f"Hit {i+1}: {hit_damage} dégâts\\n"'''

fixed = fixed.replace(old_use_skill_loop, new_use_skill_loop)

# Verify changes were applied
if old_attack_enemy in fixed:
    print("ERROR: attack_enemy fix not applied!")
elif old_use_skill_loop in fixed:
    print("ERROR: use_skill fix not applied!")
else:
    print("Both fixes applied successfully.")
    
# Write to output
with open('/mnt/agents/output/game_engine_fixed.py', 'w', encoding='utf-8') as f:
    f.write(fixed)

print("File saved to /mnt/agents/output/game_engine_fixed.py")
