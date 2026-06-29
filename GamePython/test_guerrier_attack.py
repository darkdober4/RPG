#!/usr/bin/env python3
"""
Test spécifique pour vérifier que l'attaque du Guerrier reste à 9 après la mort
"""

from game_engine import GameEngine
from game_config import CLASSES

def test_guerrier_attack_after_death():
    print("=" * 60)
    print("TEST : ATTAQUE GUERRIER APRES LA MORT")
    print("=" * 60)
    
    # Créer un Guerrier et monter au niveau 2
    print("\n1. Création d'un Guerrier niveau 2...")
    game = GameEngine()
    game.set_class("Guerrier")
    
    # Stats initiales
    print(f"   Niveau 1: Attaque={game.player_stats['attack']} (attendu: 8)")
    assert game.player_stats['attack'] == 8, f"Attaque initiale incorrecte: {game.player_stats['attack']}"
    
    # Monter au niveau 2
    game.add_exp(100)
    
    print(f"   Niveau 2: Attaque={game.player_stats['attack']} (attendu: 9)")
    assert game.player_stats['attack'] == 9, f"Attaque après level up incorrecte: {game.player_stats['attack']}"
    print("   [OK] Guerrier niveau 2 a 9 en attaque")
    
    # Simuler une mort
    print("\n2. Simulation de la mort...")
    game.take_damage(9999)
    assert game.game_over == True, "Le joueur devrait être mort"
    print("   [OK] Joueur mort")
    
    # Vérifier que l'attaque est toujours à 9 après la mort (en mémoire)
    print("\n3. Vérification de l'attaque après la mort (en mémoire)...")
    print(f"   Après la mort: Attaque={game.player_stats['attack']} (attendu: 9)")
    assert game.player_stats['attack'] == 9, f"Attaque perdue après la mort: {game.player_stats['attack']} (attendu: 9)"
    print("   [OK] Attaque conservée en mémoire")
    
    # Simuler ce que fait rpg_server.py : sauvegarder et recréer
    print("\n4. Simulation du processus de sauvegarde/rechargement...")
    
    # Sauvegarder les stats (comme le fait action() quand on meurt)
    saved_stats = {
        'exp': game.player_stats['exp'],
        'level': game.player_stats['level'],
        'gold': game.player_stats['gold'],
        'exp_for_next_level': game.player_stats['exp_for_next_level'],
        'inventory': game.inventory.copy(),
        'equipped': game.equipped.copy(),
        'health': game.player_stats['health'],
        'max_health': game.player_stats['max_health'],
        'mana': game.player_stats['mana'],
        'max_mana': game.player_stats['max_mana'],
        'attack': game.player_stats['attack'],  # ← C'est la clé !
        'defense': game.player_stats['defense']
    }
    
    # Simuler la suppression de la session (comme le fait action())
    game_id = "test_game_id"
    game_sessions = {"test_game_id": game}
    del game_sessions[game_id]
    
    # Simuler get_game_session() : créer nouveau GameEngine et charger les stats
    game2 = GameEngine()
    game2.player_class = "Guerrier"
    game2.set_class("Guerrier")  # Cela met attack à 8
    
    # Charger les saved_stats (comme le fait get_game_session())
    game2.player_stats['exp'] = saved_stats['exp']
    game2.player_stats['level'] = saved_stats['level']
    game2.player_stats['gold'] = saved_stats['gold']
    game2.player_stats['exp_for_next_level'] = saved_stats['exp_for_next_level']
    game2.inventory = saved_stats['inventory'].copy()
    game2.equipped = saved_stats['equipped'].copy()
    
    # Charger les stats supplémentaires
    if 'health' in saved_stats:
        game2.player_stats['health'] = saved_stats['health']
    if 'max_health' in saved_stats:
        game2.player_stats['max_health'] = saved_stats['max_health']
    if 'mana' in saved_stats:
        game2.player_stats['mana'] = saved_stats['mana']
    if 'max_mana' in saved_stats:
        game2.player_stats['max_mana'] = saved_stats['max_mana']
    if 'attack' in saved_stats:
        game2.player_stats['attack'] = saved_stats['attack']  # ← Restaure à 9
    if 'defense' in saved_stats:
        game2.player_stats['defense'] = saved_stats['defense']
    
    print(f"   Après rechargement: Attaque={game2.player_stats['attack']} (attendu: 9)")
    assert game2.player_stats['attack'] == 9, f"Attaque non restaurée: {game2.player_stats['attack']} (attendu: 9)"
    print("   [OK] Attaque restaurée à 9 après rechargement")
    
    print("\n" + "=" * 60)
    print("[SUCCESS] L'ATTAQUE DU GUERRIER RESTE A 9 APRES LA MORT !")
    print("=" * 60)

if __name__ == "__main__":
    try:
        test_guerrier_attack_after_death()
    except AssertionError as e:
        print(f"\n[FAIL] TEST ECHoue: {e}")
        exit(1)
    except Exception as e:
        print(f"\n[ERROR] ERREUR INATTENDUE: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
