# --------------------------------------------------------
# RANDOM ENCOUNTER - COPY DAY 4 CODE - ENCOUNTER CREATURES
# --------------------------------------------------------
 

 
    # TODO:
    # Copy your encounter function here.
    #
    # Include:
    # - Guard
    # - Ghost
    # - Rat
    # - Different messages for each creature

 


# Define the encounter function
def encounter():

    choice = ["Guard", "Ghost", "Rat"]
    from random import choice
    creature = choice(["Guard", "Ghost", "Rat"])
    print(f"\nA {creature} appears!")
 
    # Add selection to respond to the creature
    if creature == "Guard":
        print("The guard draws their sword!")
    elif creature == "Ghost":
        print("The ghost floats towards you!")
    elif creature == "Rat":
        print("the Rat wakes up and slowly walks towards you")

 
encounter()