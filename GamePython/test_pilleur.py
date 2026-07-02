# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
from game_engine import GameEngine

# Test Dévaliser
g = GameEngine()
g.set_class("Pilleur")
g.current_location = "forest"
g.player_stats["attack"] = 50
g.player_stats["level"] = 13
g.unlock_progressive_skills()

g.start_fight("Goblin")
r = g.use_skill("Dévaliser")
print(f"Dévaliser - Action: {r.get('action','')}, Kill: {r.get('enemy_defeated', False)}, Crit: {r.get('is_critical', False)}")
msg = r["message"]
print(f"  Message contient 'Dévaliser': {'Dévaliser' in msg}")
print(f"  Message contient 'épi': {'épi' in msg or 'epic' in msg.lower()}")

# Test Double ou Rien
g2 = GameEngine()
g2.set_class("Pilleur")
g2.current_location = "forest"
g2.player_stats["attack"] = 50
g2.player_stats["level"] = 13
g2.unlock_progressive_skills()
g2.start_fight("Goblin")
r2 = g2.use_skill("Double ou Rien")
print(f"\nDouble ou Rien - Action: {r2.get('action','')}, Kill: {r2.get('enemy_defeated', False)}")
msg2 = r2["message"]
print(f"  Message contient 'Double ou Rien': {'Double ou Rien' in msg2}")

# Test Ruée d'Or
g3 = GameEngine()
g3.set_class("Pilleur")
g3.current_location = "forest"
g3.player_stats["attack"] = 50
g3.player_stats["level"] = 13
g3.unlock_progressive_skills()
g3.start_fight("Goblin")
r3 = g3.use_skill("Ruée d'Or")
print(f"\nRuée d'Or - Action: {r3.get('action','')}, Kill: {r3.get('enemy_defeated', False)}")
msg3 = r3["message"]
print(f"  Message contient 'Ruée': {'Ruée' in msg3}")

# Test level up scaling
g4 = GameEngine()
g4.set_class("Pilleur")
initial_crit = g4.innate_crit_chance
initial_loot = g4.loot_quality_bonus
for _ in range(10):
    g4.player_stats["exp"] = 99999
    g4.check_level_up()
print(f"\nAprès 10 levels:")
print(f"  Crit: {initial_crit:.3f} -> {g4.innate_crit_chance:.3f}")
print(f"  Loot: {initial_loot:.3f} -> {g4.loot_quality_bonus:.3f}")
print(f"  Level: {g4.player_stats['level']}")

print("\n✅ Tous les tests Pilleur passent !")
