#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Serveur Flask pour le RPG Text-Based GamePython
Lance le jeu d'aventure en ligne
"""

from flask import Flask, render_template, request, session, redirect, url_for
from game_engine import GameEngine
from game_config import ITEMS, CLASSES, SKILLS, DAILY_QUESTS, LOCATIONS, SHOPS
import webbrowser
import threading
import os

app = Flask(__name__, template_folder='templates')
app.secret_key = 'gamepython_secret_rpg_key_2024'

# Dictionnaire des sessions de jeu
game_sessions = {}


def get_game_session():
    """Obtient ou crée une session de jeu pour l'utilisateur"""
    if 'game_id' not in session:
        session['game_id'] = os.urandom(16).hex()
    
    game_id = session['game_id']
    
    if game_id not in game_sessions:
        game_sessions[game_id] = GameEngine()
        
        # Charger la classe si sauvegardée
        if 'player_class' in session:
            game_sessions[game_id].set_class(session['player_class'])
        
        # Charger les stats sauvegardees si elles existent
        if 'saved_stats' in session:
            saved_stats = session['saved_stats']
            game_sessions[game_id].player_stats['exp'] = saved_stats.get('exp', 0)
            game_sessions[game_id].player_stats['level'] = saved_stats.get('level', 1)
            game_sessions[game_id].player_stats['gold'] = saved_stats.get('gold', 0)
            game_sessions[game_id].player_stats['exp_for_next_level'] = saved_stats.get('exp_for_next_level', 100)
            
            # Charger TOUTES les stats principales pour éviter la perte lors de la mort
            if 'health' in saved_stats:
                game_sessions[game_id].player_stats['health'] = saved_stats['health']
            if 'max_health' in saved_stats:
                game_sessions[game_id].player_stats['max_health'] = saved_stats['max_health']
            if 'mana' in saved_stats:
                game_sessions[game_id].player_stats['mana'] = saved_stats['mana']
            if 'max_mana' in saved_stats:
                game_sessions[game_id].player_stats['max_mana'] = saved_stats['max_mana']
            if 'attack' in saved_stats:
                game_sessions[game_id].player_stats['attack'] = saved_stats['attack']
            if 'defense' in saved_stats:
                game_sessions[game_id].player_stats['defense'] = saved_stats['defense']
            
            # Charger les infos de zone
            if 'current_zone' in saved_stats:
                game_sessions[game_id].current_zone = saved_stats['current_zone']
            if 'unlocked_zones' in saved_stats:
                game_sessions[game_id].unlocked_zones = saved_stats['unlocked_zones']
            
            # CORRECTION : Charger l'inventaire et l'équipement avec les bons types
            saved_inventory = saved_stats.get('inventory', {})
            match saved_inventory:
                case dict():
                    game_sessions[game_id].inventory = saved_inventory.copy()
                case list():
                    game_sessions[game_id].inventory = {}
                    for item in saved_inventory:
                        game_sessions[game_id].inventory[item] = game_sessions[game_id].inventory.get(item, 0) + 1
                case _:
                    game_sessions[game_id].inventory = {}
            
            saved_equipped = saved_stats.get('equipped', {})
            if isinstance(saved_equipped, dict):
                for slot in game_sessions[game_id].equipped:
                    game_sessions[game_id].equipped[slot] = saved_equipped.get(slot, None)
            
            # Charger la progression des quêtes
            saved_quest_progress = saved_stats.get('quest_progress', {})
            if isinstance(saved_quest_progress, dict):
                game_sessions[game_id].quest_progress = saved_quest_progress.copy()
            
            saved_completed_quests = saved_stats.get('completed_quests', [])
            if isinstance(saved_completed_quests, list):
                game_sessions[game_id].completed_quests = saved_completed_quests.copy()
            
            # Charger les compétences progressives
            saved_skills_learned = saved_stats.get('skills_learned', {})
            if isinstance(saved_skills_learned, dict):
                game_sessions[game_id].skills_learned = {k: v.copy() if isinstance(v, dict) else v for k, v in saved_skills_learned.items()}
            
            saved_unlocked_skills = saved_stats.get('unlocked_skills', {})
            if isinstance(saved_unlocked_skills, dict):
                game_sessions[game_id].unlocked_skills = saved_unlocked_skills.copy()

            saved_runes = saved_stats.get('rune_inventory', {})
            if isinstance(saved_runes, dict):
                game_sessions[game_id].rune_inventory = saved_runes.copy()
    
    return game_sessions[game_id]


@app.route('/choose-class/<class_name>')
def choose_class(class_name):
    """Permet au joueur de choisir sa classe"""
    session['player_class'] = class_name
    session.modified = True
    return redirect(url_for('index'))


@app.route('/')
def index():
    """Page d'accueil du jeu"""
    game = get_game_session()
    
    game_state = {
        'player_stats': game.get_player_stats(),
        'player_class': game.player_class,
        'location_description': game.get_location_description(),
        'available_actions': game.get_available_actions(),
        'navigation_map': game.get_navigation_map(),
        'world_map': game.get_world_map(),
        'in_combat': game.in_combat,
        'current_enemy': game.current_enemy,
        'enemy_health': getattr(game, 'enemy_health', 0),
        'enemy_max_health': getattr(game, 'enemy_max_health', 0),
        'enemy_level': getattr(game, 'enemy_level', 1),
        'enemy_attack': getattr(game, 'enemy_attack', 0),
        'enemy_defense': getattr(game, 'enemy_defense', 0),
        'is_boss_fight': getattr(game, 'is_boss_fight', False),
        'current_boss': getattr(game, 'current_boss', None),
        'game_over': game.game_over,
        'game_won': game.game_won,
        'last_message': session.get('last_message', 'Bienvenue dans GamePython RPG Adventure!'),
        'inventory': game.inventory,
        'gold': game.player_stats['gold'],
        'current_shop': game.current_shop,
        'shop_items': game.get_current_shop_items(),
        'difficulty': game.difficulty,
        'show_options': game.show_options,
        'show_inventory': game.show_inventory,
        'equipped': game.equipped,
        'all_items': ITEMS,
        'classes': CLASSES,
        'player_class_chosen': 'player_class' in session,
        'temporary_buffs': game.temporary_buffs,
        'show_quests': game.show_quests,
        'show_skills': game.show_skills,
        'quests': game.get_quests_display(),
        'completed_quests_count': len(game.completed_quests),
        'player_skills': game.get_available_skills_for_level(),
        'upcoming_skills': game.get_upcoming_skills(),
        'unlocked_skills': game.unlocked_skills,
        'combat_animation': session.get('combat_animation'),
        'current_location_npcs': LOCATIONS.get(game.current_location, {}).get('npcs', []),
        'current_location_shops': LOCATIONS.get(game.current_location, {}).get('shops', []),
        'all_shops': SHOPS,
        'runes_data': game.get_runes_display(),
        'show_runes': game.show_runes,
        'rune_buffs': game.get_rune_buff_summary()
    }
    
    if 'last_message' in session:
        del session['last_message']
    
    return render_template('game.html', game_state=game_state)


@app.route('/action', methods=['POST'])
def action():
    """Gere les actions du joueur"""
    game = get_game_session()
    
    action_type = request.form.get('action_type') or ""
    action_value = request.form.get('action_value') or ""
    message = ""
    
    # Utilisation de match/case pour une meilleure lisibilité (Python 3.10+)
    match action_type:
        # Actions de déplacement et exploration
        case 'move':
            message = game.move(action_value)
            game.close_shop()
        case 'fight':
            message = game.start_fight(action_value)
            game.close_shop()
        case 'explore':
            message = game.explore_location()
            game.close_shop()
        case 'change_zone':
            message = game.change_zone(action_value)
            game.close_shop()
        case 'explore_zone':
            message = game.explore_zone(action_value)
            game.close_shop()
        case 'rest':
            message = game.rest()
            game.close_shop()
        
        # Actions sociales
        case 'talk':
            message = game.talk_to_npc(action_value)
        case 'visit_shop':
            message = game.visit_shop(action_value)
        
        # Actions de combat
        case 'attack':
            result = game.attack_enemy()
            if isinstance(result, dict):
                message = result.get("message", "")
                if result.get("action") in ["attack", "kill"]:
                    session['combat_animation'] = {
                        "type": "attack",
                        "player_damage": result.get("player_damage", 0),
                        "enemy_damage": result.get("enemy_damage", 0),
                        "is_critical": result.get("is_critical", False)
                    }
            else:
                message = result
        
        case 'use_skill':
            result = game.use_skill(action_value)
            if isinstance(result, dict):
                message = result.get("message", "")
                # Utilisation de match/case pour les actions de compétence
                match result.get("action"):
                    case "skill_attack" | "heal" | "defense_boost" | "attack_boost" | "damage_reduction":
                        session['combat_animation'] = {
                            "type": result.get("skill_type", "skill"),
                            "action": result.get("action", "skill"),
                            "total_damage": result.get("total_damage", 0),
                            "heal_amount": result.get("heal_amount", 0),
                            "boost_amount": result.get("boost_amount", 0),
                            "is_critical": result.get("is_critical", False),
                            "hits": result.get("hits", 1),
                            "skill_name": action_value
                        }
                    case "kill":
                        session['combat_animation'] = {
                            "type": result.get("skill_type", "magic"),
                            "action": "kill",
                            "total_damage": result.get("total_damage", 0),
                            "enemy_defeated": True
                        }
                    case _:
                        pass  # Aucune animation spéciale
            else:
                message = result if isinstance(result, str) else str(result)
        
        case 'flee':
            message = game.flee_combat()
        
        # Actions d'inventaire
        case 'equip':
            parts = action_value.split('|')
            item_name = parts[0]
            item_type = parts[1] if len(parts) > 1 else 'weapon'
            if game.equip_item(item_name, item_type):
                message = f"{item_name} équipé(e)!"
            else:
                message = "Impossible d'équiper cet objet."
        
        case 'unequip':
            if game.unequip_item(action_value):
                message = "Objet dés-équipé!"
            else:
                message = "Aucun objet à dés-équiper."
        
        case 'use_item':
            message = game.use_item(action_value)
        
        case 'drop_item':
            if game.drop_item(action_value):
                message = f"{action_value} jeté(e)!"
            else:
                message = "Objet non trouvé."
        
        case 'buy':
            message = game.buy_item(action_value)
        
        case 'close_shop':
            message = game.close_shop()
        
        # Actions d'interface
        case 'set_difficulty':
            message = game.set_difficulty(action_value)
        
        case 'toggle_options':
            game.toggle_options()
            message = "Options ouvertes." if game.show_options else "Options fermees."
        
        case 'toggle_inventory':
            game.toggle_inventory()
            message = "Inventaire ouvert." if game.show_inventory else "Inventaire fermé."
        
        case 'toggle_quests':
            game.toggle_quests()
            message = "Quêtes ouvertes." if game.show_quests else "Quêtes fermées."
        
        case 'toggle_skills':
            game.toggle_skills()
            message = "Compétences ouvertes." if game.show_skills else "Compétences fermées."

        case 'toggle_runes':
            game.toggle_runes()
            message = "Runes ouvertes." if game.show_runes else "Runes fermées."

        case 'craft_rune':
            message = game.craft_rune(action_value)
        
        case 'complete_quest':
            if game.complete_quest(action_value):
                quest_data = DAILY_QUESTS.get(action_value, {})
                message = f"Quête complétée! +{quest_data.get('reward_exp', 0)} XP, +{quest_data.get('reward_gold', 0)} or"
                if quest_data.get('reward_item'):
                    message += f", +{quest_data.get('reward_item')}"
            else:
                message = "Cette quête est déjà complétée ou non accomplie."
        
        # Cas par défaut
        case _:
            message = "Action inconnue."
    
    game.check_win()
    
    # Stocker le message dans la session pour affichage
    session['last_message'] = message
    
    # Sauvegarder automatiquement les stats si le joueur est mort
    if game.game_over:
        session['saved_stats'] = {
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
            'attack': game.player_stats['attack'],
            'defense': game.player_stats['defense'],
            'quest_progress': game.quest_progress.copy(),
            'completed_quests': game.completed_quests.copy(),
            'skills_learned': {k: v.copy() if isinstance(v, dict) else v for k, v in game.skills_learned.items()},
            'unlocked_skills': game.unlocked_skills.copy(),
            'rune_inventory': game.rune_inventory.copy()
        }
        session.modified = True
        # Supprimer la session de jeu actuelle pour forcer un rechargement
        # avec les stats sauvegardées au prochain accès
        game_id = session.get('game_id')
        if game_id and game_id in game_sessions:
            del game_sessions[game_id]
        # Réinitialiser game_over pour permettre de continuer
        game.game_over = False
    
    session['last_message'] = message
    session.modified = True
    
    return redirect(url_for('index'))


@app.route('/restart', methods=['POST'])
def restart():
    """Recommence le jeu en gardant l'XP, les objets et toutes les stats"""
    game = get_game_session()
    
    # Sauvegarder TOUTES les stats actuelles dans la session
    session['saved_stats'] = {
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
        'attack': game.player_stats['attack'],
        'defense': game.player_stats['defense'],
        'current_zone': game.current_zone,
        'unlocked_zones': game.unlocked_zones.copy(),
        'quest_progress': game.quest_progress.copy(),
        'completed_quests': game.completed_quests.copy(),
        'skills_learned': {k: v.copy() if isinstance(v, dict) else v for k, v in game.skills_learned.items()},
        'unlocked_skills': game.unlocked_skills.copy(),
        'rune_inventory': game.rune_inventory.copy()
    }

    game_id = session.get('game_id')
    if game_id and game_id in game_sessions:
        del game_sessions[game_id]

    if 'last_message' in session:
        del session['last_message']

    session['game_id'] = os.urandom(16).hex()
    session.modified = True
    
    return redirect(url_for('index'))


@app.route('/health')
def health():
    """Route de sante du serveur"""
    return {'status': 'ok', 'message': 'Serveur RPG actif'}, 200


@app.route('/clear_animation', methods=['POST'])
def clear_animation():
    """Nettoie l'animation de combat après affichage"""
    if 'combat_animation' in session:
        del session['combat_animation']
        session.modified = True
    return '', 200


def open_browser():
    """Ouvre le navigateur"""
    url = "http://127.0.0.1:5000"
    webbrowser.open(url)
    print(f"Navigateur ouvert a: {url}")


if __name__ == '__main__':
    print("Serveur RPG GamePython demarrage!")
    print("Acces a: http://127.0.0.1:5000")
    print("Pour arreter: Ctrl+C")
    print()
    
    browser_thread = threading.Thread(target=open_browser, daemon=True)
    browser_thread.start()
    
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True,
        use_reloader=False
    )
