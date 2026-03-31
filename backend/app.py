import os
from flask import Flask, render_template, request, redirect, url_for, session #to start a flask app, render html templates, handle requests, redirect users, and manage sessions
from logic import get_random_event # Import the function to get random events when entering a floor
from data import STARTING_ITEMS # Import the starting items for the player's inventory

import random


#Get the directory of the current file to use for loading assets (app.py) and templates (index.html)
base_dir = os.path.dirname(os.path.abspath(__file__))

templates_dir = os.path.join(base_dir, '..', 'frontend', 'templates')
static_dir = os.path.join(base_dir, '..', 'frontend', 'static')

app = Flask(__name__, template_folder=templates_dir, static_folder=static_dir) # Create a Flask application instance, specifying the directories for templates and static files.
app.secret_key = 'dungeonmaster' # Set a secret key for session management

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

if __name__ == '__main__':
    app.run(debug=True)