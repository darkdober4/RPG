#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Serveur Flask pour le RPG Text-Based GamePython
Lance le jeu d'aventure en ligne
"""

from flask import Flask, render_template, request, session, redirect, url_for
from game_engine import GameEngine
from game_config import ITEMS, CLASSES, SKILLS, DAILY_QUESTS
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
            
            # CORRECTION : Charger l'inventaire et l'équipement avec les bons types
            saved_inventory = saved_stats.get('inventory', {})
            if isinstance(saved_inventory, dict):
                game_sessions[game_id].inventory = saved_inventory.copy()
            elif isinstance(saved_inventory, list):
                game_sessions[game_id].inventory = {}
                for item in saved_inventory:
                    game_sessions[game_id].inventory[item] = game_sessions[game_id].inventory.get(item, 0) + 1
            
            saved_equipped = saved_stats.get('equipped', {})
            if isinstance(saved_equipped, dict):
                for slot in game_sessions[game_id].equipped:
                    game_sessions[game_id].equipped[slot] = saved_equipped.get(slot, None)
    
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
        'unlocked_skills': game.unlocked_skills
    }
    
    if 'last_message' in session:
        del session['last_message']
    
    return render_template('game.html', game_state=game_state)


@app.route('/action', methods=['POST'])
def action():
    """Gere les actions du joueur"""
    game = get_game_session()
    
    action_type = request.form.get('action_type')
    action_value = request.form.get('action_value')
    
    message = ""
    
    if action_type == 'move':
        message = game.move(action_value)
        game.close_shop()
    elif action_type == 'fight':
        message = game.start_fight(action_value)
        game.close_shop()
    elif action_type == 'talk':
        message = game.talk_to_npc(action_value)
    elif action_type == 'attack':
        message = game.attack_enemy()
    elif action_type == 'use_skill':
        message = game.use_skill(action_value)
    elif action_type == 'flee':
        message = game.flee_combat()
    elif action_type == 'buy':
        message = game.buy_item(action_value)
    elif action_type == 'equip':
        parts = action_value.split('|')
        item_name = parts[0]
        item_type = parts[1] if len(parts) > 1 else 'weapon'
        if game.equip_item(item_name, item_type):
            message = f"{item_name} équipé(e)!"
        else:
            message = "Impossible d'équiper cet objet."
    elif action_type == 'unequip':
        if game.unequip_item(action_value):
            message = f"Objet dés-équipé!"
        else:
            message = "Aucun objet à dés-équiper."
    elif action_type == 'use_item':
        message = game.use_item(action_value)
    elif action_type == 'drop_item':
        if game.drop_item(action_value):
            message = f"{action_value} jeté(e)!"
        else:
            message = "Objet non trouvé."
    elif action_type == 'close_shop':
        message = game.close_shop()
    elif action_type == 'set_difficulty':
        message = game.set_difficulty(action_value)
    elif action_type == 'toggle_options':
        game.toggle_options()
        if game.show_options:
            message = "Options ouvertes."
        else:
            message = "Options fermees."
    elif action_type == 'toggle_inventory':
        game.toggle_inventory()
        if game.show_inventory:
            message = "Inventaire ouvert."
        else:
            message = "Inventaire fermé."
    elif action_type == 'toggle_quests':
        game.toggle_quests()
        if game.show_quests:
            message = "Quêtes ouvertes."
        else:
            message = "Quêtes fermées."
    elif action_type == 'toggle_skills':
        game.toggle_skills()
        if game.show_skills:
            message = "Compétences ouvertes."
        else:
            message = "Compétences fermées."
    elif action_type == 'complete_quest':
        if game.complete_quest(action_value):
            quest_data = DAILY_QUESTS.get(action_value, {})
            message = f"Quête complétée! +{quest_data.get('reward_exp', 0)} XP, +{quest_data.get('reward_gold', 0)} or"
            if quest_data.get('reward_item'):
                message += f", +{quest_data.get('reward_item')}"
        else:
            message = "Cette quête est déjà complétée ou non accomplie."
    
    game.check_win()
    
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
            'defense': game.player_stats['defense']
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
        'defense': game.player_stats['defense']
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
