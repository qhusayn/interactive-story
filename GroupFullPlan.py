# ==========================================
# ESCAPE THE CASTLE - COMPLETE GAME
# ==========================================
 
import random
 
# SHARED GAME INFORMATION
inventory = []
 
 
# ==========================================
# INTRODUCTION - COPY DAY 2 CODE
# ==========================================
 
def introduction():
 
    # TODO:
    # Copy your character creation code here.
    #
    # Include:
    # - Welcome message
    # - Player name
    # - Character class
    # - Starting health and gold
    #
    # Remember to indent your code!
 
 
# ==========================================
# CELL - COPY DAY 3/4 CODE
# ==========================================
 
def cell():
 
    # TODO:
    # Copy your Cell scene here.
    #
    # Include:
    # - Door, window and bed choices
    # - While loop
    # - Finding the Iron Key
    # - Adding the key to inventory
    #
    # Remove any separate inventory = []
    # from your original scene.
 
 
# ==========================================
# RANDOM ENCOUNTER - COPY DAY 4 CODE
# ==========================================
 
def encounter(creature):
 
    # TODO:
    # Copy your encounter function here.
    #
    # Include:
    # - Guard
    # - Ghost
    # - Rat
    # - Different messages for each creature
 
 
# ==========================================
# CORRIDOR - COPY DAY 3/4 CODE
# ==========================================
 
def corridor():
 
    # TODO:
    # Copy your Corridor scene here.
    #
    # Include:
    # - Cabinet choice
    # - Finding the Rusty Dagger
    # - Adding the dagger to inventory
    #
    # Then add:
    # - List of possible creatures
    # - random.choice()
    # - Call encounter() with the chosen creature
 
 
# ==========================================
# LIBRARY - NEW SCENE
# ==========================================
 
def library():
 
    # TODO:
    # Create a Library scene.
    #
    # The player discovers a clue to the
    # password needed to escape the castle.
    #
    # Use:
    # - print()
    # - input()
    # - if/elif/else
    # - A while loop
 
 
# ==========================================
# CASTLE GATE - NEW SCENE
# ==========================================
 
def castle_gate():
 
    # TODO:
    # Create the final escape challenge.
    #
    # The player must enter the correct
    # password to unlock the gate.
    #
    # Use a while loop to allow retries.
    #
    # Display a victory message when
    # the player escapes.
 
 
# ==========================================
# MAIN GAME
# ==========================================
 
def play_game():
 
    introduction()
    cell()
    corridor()
    library()
    castle_gate()
 
 
# Start the game
play_game()
 
 