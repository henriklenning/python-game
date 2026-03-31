from flask import Flask, render_template, request, redirect, url_for #to start a flask app, render html templates, handle requests, and redirect users
import random

app = Flask(__name__)
app.secret_key = 'dungeonmaster' # Set a secret key for session management

STARTING_ITEMS = [
    { "id": 1, "name": "Copper Shortsword", "type": "Weapon", "stat": {"attack": 5}, "description": "A basic shortsword made of copper. It has a dull blade and is not very effective in combat." },
    { "id": 2, "name": "Wooden Shield", "type": "Secondary", "stat": {"defense": 3}, "description": "A simple wooden shield. It provides minimal protection and is easily damaged." },
    { "id": 3, "name": "Leather Armor", "type": "Armor", "stat": {"defense": 4}, "description": "Basic leather armor. It offers some protection but is not very durable." }
    ]

ITEM_POOL = [] 

def initialize_game():
    session['floor'] = 0
    session['inventory'] = list(STARTING_ITEMS) # Start with a copy of the starting items
    session['health'] = 100
    session['log'] = ["You stand before the entrance of a dark, assumed to be, long abandoned dungeon. The air is thick with the scent of damp stone and decay. You can feel a chill run down your spine as you step inside, the darkness swallowing you whole. There ought to be riches and treasures hidden within, but also dangers lurking in the shadows. You must be cautious as you explore the depths of this ancient place."]

@app.route('/')
def index():
    if 'floor' not in session:
        # If the user is new (no 'floor' in session), start the game
        initialize_game()
    
    # Send the current game state to the template for rendering
    return render_template('index.html',
                            floor=session['floor'], 
                            inventory=session['inventory'], 
                            health=session['health'], 
                            log=session['log'])