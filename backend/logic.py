# This file contains the logic for the game, including the random events that can occur when entering a floor. It uses the item pool from data.py to generate loot events.
import random
from data import ITEM_POOL # Import the item pool to use for generating loot events

def get_random_event(floor):
    """Decides what happens when you enter a floor."""
    roll = random.randint(1, 3)
    
    if floor == 10:
        return {"type": "boss", "text": "The Final Dragon awakes!"}
    
    if roll == 1:
        return {"type": "combat", "text": "A foul goblin jumps from the shadows!"}
    elif roll == 2:
        item = random.choice(ITEM_POOL)
        return {"type": "loot", "text": f"You found a {item['name']}!", "item": item}
    else:
        return {"type": "empty", "text": "The hallway is eerily quiet."}