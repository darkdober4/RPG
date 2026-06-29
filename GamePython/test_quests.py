#!/usr/bin/env python3
"""
Test unitaire pour vérifier que le système de quêtes fonctionne correctement
"""

from game_engine import GameEngine
from game_config import DAILY_QUESTS

def test_quest_system():
    print("=" * 60)
    print("TEST DU SYSTEME DE QUETES")
    print("=" * 60)
    
    # Créer une nouvelle instance du jeu
    game = GameEngine()
    game.set_class("Guerrier")
    
    # Vérifier que toutes les quêtes sont initialisées
    print("\n1. Verification de l'initialisation des quetes...")
    for quest_id in DAILY_QUESTS:
        assert quest_id in game.quest_progress, f"Quete {quest_id} non initialisee"
        assert game.quest_progress[quest_id] == 0, f"Quete {quest_id} a une progression non nulle"
        assert quest_id not in game.completed_quests, f"Quete {quest_id} deja marquee comme completee"
    print("   [OK] Toutes les quetes sont correctement initialisees a 0")
    
    # Tester une quête de type "tuer X ennemis"
    print("\n2. Test de la quete 'Tueur de Gobelins' (tuer 5 Gobelins)...")
    for i in range(5):
        # Simuler la mort d'un Gobelin
        game.update_quest_progress(enemy_name="Gobelin", exp_gain=50, gold_gain=10)
    
    # Vérifier que la quête est complétée
    assert "Tueur de Gobelins" in game.completed_quests, "Quete non completee apres 5 Gobelins"
    print("   [OK] Quete 'Tueur de Gobelins' completee apres 5 kills")
    
    # Tester une quête de type "gold"
    print("\n3. Test de la quete 'Collectionneur de Pieces' (500 or)...")
    game2 = GameEngine()
    game2.set_class("Mage")
    
    # Gagner 500 or
    game2.update_quest_progress(gold_gain=500)
    
    # Vérifier que la quête est complétée
    assert "Collectionneur de Pièces" in game2.completed_quests, "Quete d'or non completee"
    print("   [OK] Quete 'Collectionneur de Pieces' completee apres 500 or")
    
    # Tester une quête de type "exp"
    print("\n4. Test de la quete 'Aventurier Experimente' (1000 XP)...")
    game3 = GameEngine()
    game3.set_class("Archer")
    
    # Gagner 1000 XP
    game3.update_quest_progress(exp_gain=1000)
    
    # Vérifier que la quête est complétée
    assert "Aventurier Expérimenté" in game3.completed_quests, "Quete d'XP non completee"
    print("   [OK] Quete 'Aventurier Experimente' completee apres 1000 XP")
    
    # Tester la complétion manuelle
    print("\n5. Test de la completion manuelle (bouton 'Completer la quete')...")
    game4 = GameEngine()
    game4.set_class("Guerrier")
    
    # Gagner 1000 XP pour accomplir la quête
    game4.update_quest_progress(exp_gain=1000)
    
    # Essayer de compléter manuellement une quête non accomplie
    result = game4.complete_quest("Chasseur de Loups")  # Nécessite 3 Loups
    assert result == False, "Quete non accomplie completee avec succes (erreur !)"
    print("   [OK] Impossible de completer manuellement une quete non accomplie")
    
    # Accomplir la quête en tuant 3 loups
    for i in range(3):
        game4.update_quest_progress(enemy_name="Loup", exp_gain=75, gold_gain=20)
    
    # La quête devrait être automatiquement complétée après le 3ème loup
    assert "Chasseur de Loups" in game4.completed_quests, "Quete non auto-completee apres 3 loups"
    print("   [OK] Quete automatiquement completee apres 3 loups")
    
    # Tester qu'une quête déjà complétée ne peut pas être complétée à nouveau
    print("\n6. Test de la double completion...")
    result = game4.complete_quest("Chasseur de Loups")
    assert result == False, "Quete deja completee completee a nouveau (erreur !)"
    print("   [OK] Impossible de completer une quete deja accomplie")
    
    # Tester le gain d'or via la vente d'items
    print("\n7. Test du gain d'or via la vente d'items...")
    game5 = GameEngine()
    game5.set_class("Guerrier")
    game5.inventory["Épée de Fer"] = 1
    
    # Vendre un item (doit déclencher update_quest_progress)
    # Note: sell_item appelle update_quest_progress, donc cela devrait fonctionner
    game5.sell_item("Épée de Fer")
    
    # Vérifier que l'or a été ajouté
    assert game5.player_stats["gold"] > 0, "Or non ajoute apres vente"
    print(f"   [OK] Or ajoute apres vente: {game5.player_stats['gold']} or")
    
    # Tester que les quêtes d'or sont mises à jour
    print("\n8. Test des quetes d'or avec gain progressif...")
    game6 = GameEngine()
    game6.set_class("Mage")
    
    # Gagner de l'or petit à petit
    for i in range(5):
        game6.update_quest_progress(gold_gain=100)  # 500 or au total
    
    assert "Collectionneur de Pièces" in game6.completed_quests
    print("   [OK] Quete d'or completee avec gain progressif")
    
    print("\n" + "=" * 60)
    print("[SUCCESS] TOUS LES TESTS ONT REUSSI !")
    print("=" * 60)
    print("\nLe systeme de quetes fonctionne correctement !")
    print("- Les quetes de type 'tuer X ennemis' sont suivies")
    print("- Les quetes de type 'amasser X or' sont suivies")
    print("- Les quetes de type 'gagner X XP' sont suivies")
    print("- La completion manuelle verifie les conditions")
    print("- Impossible de completer une quete non accomplie ou deja completee")

if __name__ == "__main__":
    try:
        test_quest_system()
    except AssertionError as e:
        print(f"\n❌ TEST ÉCHOUÉ: {e}")
        exit(1)
    except Exception as e:
        print(f"\n❌ ERREUR INATTENDUE: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
