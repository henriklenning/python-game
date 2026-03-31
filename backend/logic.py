# backend/logic.py
import random
from data import ITEM_POOL # The dot means "look in the current folder"

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