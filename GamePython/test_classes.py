#!/usr/bin/env python3
"""
Test unitaire pour verifier que les classes fonctionnent correctement
"""

from game_engine import GameEngine
from game_config import CLASSES

def test_class_stats():
    print("=" * 60)
    print("TEST DES CLASSES")
    print("=" * 60)
    
    # Test Guerrier
    print("\n1. Test classe Guerrier...")
    game = GameEngine()
    game.set_class("Guerrier")
    
    # Vérifier les stats de base
    assert game.player_class == "Guerrier", "Classe non definie"
    assert game.player_stats["health"] == 120, f"Santé incorrecte: {game.player_stats['health']} (attendu: 120)"
    assert game.player_stats["max_health"] == 120, f"Santé max incorrecte: {game.player_stats['max_health']} (attendu: 120)"
    assert game.player_stats["attack"] == 8, f"Attaque incorrecte: {game.player_stats['attack']} (attendu: 8)"
    assert game.player_stats["defense"] == 3, f"Défense incorrecte: {game.player_stats['defense']} (attendu: 3)"
    assert game.player_stats["mana"] == 30, f"Mana incorrect: {game.player_stats['mana']} (attendu: 30)"
    assert game.player_stats["max_mana"] == 30, f"Mana max incorrect: {game.player_stats['max_mana']} (attendu: 30)"
    print("   [OK] Stats de base Guerrier correctes")
    
    # Test Mage
    print("\n2. Test classe Mage...")
    game2 = GameEngine()
    game2.set_class("Mage")
    
    assert game2.player_class == "Mage", "Classe non definie"
    assert game2.player_stats["health"] == 70, f"Santé incorrecte: {game2.player_stats['health']} (attendu: 70)"
    assert game2.player_stats["max_health"] == 70, f"Santé max incorrecte: {game2.player_stats['max_health']} (attendu: 70)"
    assert game2.player_stats["attack"] == 3, f"Attaque incorrecte: {game2.player_stats['attack']} (attendu: 3)"
    assert game2.player_stats["defense"] == 0, f"Défense incorrecte: {game2.player_stats['defense']} (attendu: 0)"
    assert game2.player_stats["mana"] == 100, f"Mana incorrect: {game2.player_stats['mana']} (attendu: 100)"
    assert game2.player_stats["max_mana"] == 100, f"Mana max incorrect: {game2.player_stats['max_mana']} (attendu: 100)"
    print("   [OK] Stats de base Mage correctes")
    
    # Test Archer
    print("\n3. Test classe Archer...")
    game3 = GameEngine()
    game3.set_class("Archer")
    
    assert game3.player_class == "Archer", "Classe non definie"
    assert game3.player_stats["health"] == 90, f"Santé incorrecte: {game3.player_stats['health']} (attendu: 90)"
    assert game3.player_stats["max_health"] == 90, f"Santé max incorrecte: {game3.player_stats['max_health']} (attendu: 90)"
    assert game3.player_stats["attack"] == 6, f"Attaque incorrecte: {game3.player_stats['attack']} (attendu: 6)"
    assert game3.player_stats["defense"] == 1, f"Défense incorrecte: {game3.player_stats['defense']} (attendu: 1)"
    assert game3.player_stats["mana"] == 50, f"Mana incorrect: {game3.player_stats['mana']} (attendu: 50)"
    assert game3.player_stats["max_mana"] == 50, f"Mana max incorrect: {game3.player_stats['max_mana']} (attendu: 50)"
    print("   [OK] Stats de base Archer correctes")
    
    # Test montage de niveau Guerrier
    print("\n4. Test montage de niveau Guerrier...")
    game4 = GameEngine()
    game4.set_class("Guerrier")
    initial_health = game4.player_stats["max_health"]
    initial_attack = game4.player_stats["attack"]
    initial_defense = game4.player_stats["defense"]
    initial_mana = game4.player_stats["max_mana"]
    
    # Gagner assez d'XP pour monter de niveau
    game4.add_exp(100)  # exp_for_next_level est 100 au niveau 1
    
    # Calcul du bonus de mana : 5 + (max_mana * 0.001)
    mana_bonus = 5 + (initial_mana * 0.001)
    
    assert game4.player_stats["level"] == 2, f"Niveau incorrect: {game4.player_stats['level']} (attendu: 2)"
    assert game4.player_stats["max_health"] == initial_health + 5, f"Santé max non augmentée: {game4.player_stats['max_health']} (attendu: {initial_health + 5})"
    assert game4.player_stats["attack"] == initial_attack + 1, f"Attaque non augmentée: {game4.player_stats['attack']} (attendu: {initial_attack + 1})"
    assert game4.player_stats["defense"] == initial_defense + 2, f"Défense non augmentée: {game4.player_stats['defense']} (attendu: {initial_defense + 2})"
    assert abs(game4.player_stats["max_mana"] - (initial_mana + mana_bonus)) < 0.01, f"Mana max non augmentée: {game4.player_stats['max_mana']} (attendu: {initial_mana + mana_bonus})"
    print("   [OK] Bonus de niveau Guerrier corrects (incluant bonus mana universel)")
    
    # Test montage de niveau Mage
    print("\n5. Test montage de niveau Mage...")
    game5 = GameEngine()
    game5.set_class("Mage")
    initial_mana = game5.player_stats["max_mana"]
    initial_attack = game5.player_stats["attack"]
    
    # Calcul du bonus de mana universel + bonus de classe
    mana_bonus = 5 + (initial_mana * 0.001)
    
    game5.add_exp(100)
    
    assert game5.player_stats["level"] == 2, f"Niveau incorrect: {game5.player_stats['level']} (attendu: 2)"
    # Mage : bonus universel (5 + 0.1% de max_mana) + bonus de classe (+2)
    expected_max_mana = initial_mana + mana_bonus + 2
    assert abs(game5.player_stats["max_mana"] - expected_max_mana) < 0.01, f"Mana max non augmentée: {game5.player_stats['max_mana']} (attendu: {expected_max_mana})"
    assert abs(game5.player_stats["attack"] - (initial_attack + 0.5)) < 0.01, f"Attaque non augmentée: {game5.player_stats['attack']} (attendu: {initial_attack + 0.5})"
    print("   [OK] Bonus de niveau Mage corrects (incluant bonus mana universel)")
    
    # Test base_stats mis à jour avec la classe
    print("\n6. Test base_stats mis à jour avec la classe...")
    game6 = GameEngine()
    game6.set_class("Guerrier")
    
    assert game6.base_stats["health"] == 120, f"base_stats health incorrect: {game6.base_stats['health']} (attendu: 120)"
    assert game6.base_stats["max_health"] == 120, f"base_stats max_health incorrect: {game6.base_stats['max_health']} (attendu: 120)"
    assert game6.base_stats["attack"] == 8, f"base_stats attack incorrect: {game6.base_stats['attack']} (attendu: 8)"
    print("   [OK] base_stats mis à jour avec les stats de la classe")
    
    # Test bonus de mana universel pour toutes les classes
    print("\n7. Test bonus de mana universel (5 + 0.1% de max_mana par niveau)...")
    # Tester Guerrier (qui n'avait pas de bonus de mana avant)
    game7 = GameEngine()
    game7.set_class("Guerrier")
    initial_mana_guerrier = game7.player_stats["max_mana"]
    game7.add_exp(100)  # Monter au niveau 2
    mana_bonus_guerrier = 5 + (initial_mana_guerrier * 0.001)
    expected_mana_guerrier = initial_mana_guerrier + mana_bonus_guerrier
    assert abs(game7.player_stats["max_mana"] - expected_mana_guerrier) < 0.01, \
        f"Guerrier : Mana max = {game7.player_stats['max_mana']}, attendu {expected_mana_guerrier}"
    
    # Tester Mage
    game8 = GameEngine()
    game8.set_class("Mage")
    initial_mana_mage = game8.player_stats["max_mana"]
    game8.add_exp(100)
    mana_bonus_mage = 5 + (initial_mana_mage * 0.001)
    # Mage a aussi son bonus de classe (+2)
    expected_mana_mage = initial_mana_mage + mana_bonus_mage + 2
    assert abs(game8.player_stats["max_mana"] - expected_mana_mage) < 0.01, \
        f"Mage : Mana max = {game8.player_stats['max_mana']}, attendu {expected_mana_mage}"
    
    print("   [OK] Bonus de mana universel appliqué à toutes les classes")
    
    print("\n" + "=" * 60)
    print("[SUCCESS] TOUS LES TESTS DES CLASSES ONT REUSSI !")
    print("=" * 60)

if __name__ == "__main__":
    try:
        test_class_stats()
    except AssertionError as e:
        print(f"\n[FAIL] TEST ECHoue: {e}")
        exit(1)
    except Exception as e:
        print(f"\n[ERROR] ERREUR INATTENDUE: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
