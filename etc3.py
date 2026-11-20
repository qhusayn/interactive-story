import os
import streamlit as st
import random
from dotenv import load_dotenv
from google import genai
 
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
 
client = genai.Client(api_key=api_key) if api_key else None
 
MODEL_NAME = "gemini-3.5-flash-lite"

# ================================================================
# 1. PAGE SETUP — SAME APPROACH AS THE FINAL APP
# ================================================================
# page_icon uses the Unicode castle character, not an image file.
# Keep this before other Streamlit display calls.
st.set_page_config(page_title="Escape the Castle", page_icon="🏰", layout="centered")
st.title("🏰 Escape the Castle")

# ================================================================
# 2. GAME SETUP — INITIALISE VALUES ONCE & STRUCTURED
# ================================================================
# Session state remembers values when Streamlit reruns the script.
if "game_started" not in st.session_state:
    st.session_state.game_started = False
 
def start_game(name):
    """Set the same starting values and seven-room route as the final app."""
    st.session_state.game_started = True
    st.session_state.player_name = name
    st.session_state.health = 5
    st.session_state.max_health = 5
    st.session_state.inventory = ["Torch"]
    st.session_state.rooms = [ 
        "cell", "corridor", "crypt", "library",
        "guard_room", "dungeon", "castle_gate"
    ]
    st.session_state.room_number = 0
    st.session_state.result_type = ""
    st.session_state.result_message = ""
    st.session_state.result_value = ""
    st.session_state.action_complete = False

 
def restart_game():
    """Clear saved game values and return to the start screen"""
    st.session_state.clear()
    st.rerun()

 
def get_current_room():
    """Use the room number to find the name of the current room."""
    return st.session_state.rooms[st.session_state.room_number]


def continue_game():
    """Clear the last action and move to the next room."""
    st.session_state.result_type = ""
    st.session_state.result_message = ""
    st.session_state.result_value = ""
    st.session_state.action_complete = False
    st.session_state.room_number += 1
    st.rerun()

def add_item(item):
    if item not in st.session_state.inventory:
                    st.session_state.inventory.append(item)
 
def has_item(item):
     return item in st.session_state.inventory
 
def remove_item(item):
     if item in st.session_state.inventory:
                         st.session_state.inventory.remove(item)
 
def take_damage(amount):
    st.session_state.health = st.session_state.health - amount
    if st.session_state.health < 0:
        st.session_state.health = 0
 
def heal_player(amount):
    old_health = st.session_state.health
    st.session_state.health = min(st.session_state.max_health, st.session_state.health + amount)
    return st.session_state.health - old_health

def generate_story(room, action, outcome, fallback_message):
    if client is None:
        return fallback_message

    inventory_text = ", ".join(st.session_state.inventory)

    prompt = f"""
You are the storyteller for a dark fantasy
adventure game called Escape the Castle.

Player: {st.session_state.player_name}
Room: {room}
Health: {st.session_state.health}/{st.session_state.max_health}
Inventory: {inventory_text}
 
Action:
{action}
 
Outcome:
{outcome}
 
Describe what happens in 30-50 words.
 
Use second person, but other times in the first person.
Use atmospheric dark fantasy language, but as if your're taking to a 7 year old child.
Do not hange the outcome.
Do not change health or inventory.
Do not introduce new choices.
"""
    try:
        interaction = client.interactions.create(
            model="gemini-3.5-flash-lite",
            input=prompt,
            generation_config={"thinking_level": "minimal"}
        )
        if interaction.output_text:
            return interaction.output_text
        return fallback_message
    except Exception as error:
        st.error(f"Gemini error: {error}")
        return fallback_message

def roll_dice():
    return random.randint(1, 6)
 
def chance_encounter(button_text, room, action, success_number, success_outcome, success_fallback, failure_outcome, failure_fallback, damage, bonus_item=""):
    if st.button(button_text):
        roll = roll_dice()
        if bonus_item != "" and has_item(bonus_item):
            roll = roll + 2
        if roll >= success_number:
            story = generate_story(room, action, success_outcome, success_fallback)
            set_result("success", story)
        else:
            take_damage(damage)
            story = generate_story(room, action, failure_outcome, failure_fallback)
            set_result("damage", story, damage)
        st.rerun


# ================================================================
# 3. REUSABLE DISPLAY FUNCTIONS — KEEP EVERY ROOM CONSISTENT
# ================================================================
def show_room(title, description):
    """Display a room heading and its description."""
    st.header(title)
    st.write(description)


def show_player_info():
    """Show the player information in the main page for today's lesson."""
    st.subheader(f"🧑 {st.session_state.player_name} ")
    left, right = st.columns(2)
    with left:
        st.write(f"❤️ Health: {st.session_state.health} / {st.session_state.max_health}")
    with right:
        st.write(f"🎒 Inventory: {', '.join(st.session_state.inventory)}")  
    st.caption(
        f"Room {st.session_state.room_number + 1}"
        f"of {len(st.session_state.rooms)}"
    )
    st.divider()


def set_result(result_type, message, value="Apple"):
    """Save the outcome so it remains visible after a rerun."""
    st.session_state.result_type = result_type
    st.session_state.result_message = message
    st.session_state.result_value = value
    st.session_state.action_complete = True
    st.rerun()

 
def show_result():
    kind = st.session_state.result_type
    value = st.session_state.result_value
 
    if kind == "item":
        st.success(f"🎒 NEW ITEM: {value}")
    elif kind == "damage":
        st.error(f"💔 DAMAGE: You lose {value} health.")
    elif kind == "heal":
        st.success(f"💚 HEALED: You recover {value} health.")
    elif kind == "success":
        st.success("✅ Success!")
    else:
        st.info("The journey continues...")
 
    st.write(st.session_state.result_message)
 
 
def show_continue_button(text = "Continue"):
    """Only offer Continue after the room action is finished."""
    if st.button(text):
        continue_game()

# ========================================================
# 4. START SCREEN — NAME INPUT FROM DAY 1
# =========================================================
room = None

if not st.session_state.game_started:
    st.write("You wake beneath an ancient castle. Your goal is to escape.")
    name = st.text_input("What is your name?")
    if st.button("Enter the Castle"):
        if name.strip():
            start_game(name)
            st.rerun()
        else:
            st.warning("Enter your name first before starting ")

else:
    # Show the same player information on every room.
    show_player_info()
    room = get_current_room()

    if st.session_state.health <= 0:
        show_room("💀 Game Over", "Your strength gives out. The castle has claimed another victim.")
        st.error("You did not escape the castle")
        if st.button("🔄 Try Again"):
            restart_game()
            st.stop()

# ============================================================
# ROOM 1 — CELL (MODEL SIMPLE CONTINUE NAVIGATION)
# ============================================================

if room == "cell":
    show_room("🔒 The Cell", " You wake on a cold stone floor. The iron door creaks open.")
    if not st.session_state.action_complete:
        left, right = st.columns(2)
        with left:
            if st.button("🔎 Search the cell"):
                outcome = "The player searches the cell, finds nothing useful, and notices the iron door is open."
                story = generate_story(
                    "The Cell",
                    "searching the cold stone cell",
                    outcome,
                    "You search the cold stone cell but find nothing useful. The iron door hangs open."
                )
                set_result("story", story)
        with right:
            if st.button("🚪 Leave the cell"):
                outcome = "The player leaves the cell through the open iron door and heads toward the corridor."
                story = generate_story(
                    "The Cell",
                    "leaving through the open iron door",
                    outcome,
                    "You step through the open iron door and head toward the corridor."
                )
                set_result("story", story)
    else:
        show_result()
        show_continue_button()

# ============================================================
# ROOM 2 — CORRIDOR (MODEL RESULT -> CONTINUE)
# ============================================================

elif room == "corridor":
    show_room("🕯️ The Corridor", "A wooden cabinet stands beside the staircase.")
    if not st.session_state.action_complete:
        left, right = st.columns(2)
        with left:
            if st.button("🔎 Search the cabinet"):
                add_item("Rusty Dagger")
                outcome = "The player searches the cabinet and finds a Rusty Dagger."
                story = generate_story(
                    "The Corridor",
                    "searching the wooden cabinet beside the staircase",
                    outcome,
                    "You search the cabinet and find a Rusty Dagger tucked inside."
                )
                set_result("item", story, "Rusty Dagger")
                st.rerun()
        with right:
            if st.button("➡️ Ignore it"):
                outcome = "The player ignores the cabinet and continues down the corridor."
                story = generate_story(
                    "The Corridor",
                    "ignoring the wooden cabinet and continuing onward",
                    outcome,
                    "You leave the cabinet untouched and continue down the dim corridor."
                )
                set_result("story", story)
    else:
        show_result()
        show_continue_button()


# ============================================================
# ROOM 3 — CRYPT (LEARNERS REPEAT THE PATTERN)
# ============================================================

elif room == "crypt":
    show_room("⚰️ The Crypt", "A metal object glints beside a stone coffin.")
    if not st.session_state.action_complete:
        left, right = st.columns(2)
        with left:
            if st.button("🔎 Investigate"):
                roll = roll_dice()
                if roll >= 3:
                    add_item("Iron Key")
                    outcome = "The player safely finds an Iron Key beside the coffin."
                    story = generate_story(
                    "The Crypt",
                    "investigating the glinting object beside the stone coffin",
                    outcome,
                    "You brush dust from an Iron Key and take it from beside the coffin."
                    )
                    set_result("item", story, "Iron Key")
                else:
                    take_damage(1)
                    story = generate_story(
                    "The Crypt", "investigate the object beside a coffin", "A skeletal hand attacks the player, who loses 1 health.", "A skeletal hand bursts from the coffin and claws your arm!"
                    )
                set_result("damage", story, 1)
            st.rerun()

        with right:
            if st.button("🚪 Leave the crypt"):
                outcome = "The player leaves the crypt without disturbing anything."
                story = generate_story(
                    "The Crypt",
                    "leaving the crypt undisturbed",
                    outcome,
                    "You back away from the coffin and leave the silent crypt."
                )
                set_result("story", story)
                st.rerun()
    else:
        show_result()
        show_continue_button()
 
# ============================================================
# ROOM 4 — LIBRARY (REPEAT THE PATTERN)
# ============================================================
elif room == "library":
    show_room("📚 The Forgotten Library", "A strange green light shines from an old book.")
    if not st.session_state.action_complete:
        left, right = st.columns(2)
        with left:
            if st.button("📖 Read the book"):
                roll = roll_dice()
                if roll >=3:
                    healed = heal_player(1)
                    if healed > 0:
                        story = generate_story(
                            "The Forgotten Library", 
                            "read the glowing book", 
                            "The book heals the player by 1 health.", 
                            "Warm light flows from the pages and your injuries heal."
                        )
                        set_result("heal", story, healed)
                    else:
                        story = generate_story(
                            "The Forgotten Library", "read the glowing book", 
                            "The player is at full health, so nothing changes.", 
                            "The book glows, but you are already at full health."
                        )
                        set_result("story", story)
                else:
                    take_damage(1)
                    story = generate_story(
                        "the Forgotten Library", "read the glowing book",
                        "The cursed book causes the player to lose 1 health.",
                        "The writing twists across the page. Sharp pain hits you."
                    )
                    set_result("damage", story, 1)
                st.rerun()

        with right:
            if st.button("🚪 Leave it alone"):
                story = generate_story(
                    "The Forgotten Library", "leave the glowing book alone",
                    "The player leaves the book and continues safely.",
                    "You decide not to touch the strange book."
                )
                set_result("story", story)
    else:
        show_result()
        show_continue_button()

# ============================================================
# ROOM 5 — GUARD ROOM (CHOICES WITHOUT DICE YET)
# ============================================================

elif room == "guard_room":
        show_room("⚔️ The Guard Room", "A ghostly knight blocks the doorway.")
        if has_item("Rusty Dagger"):
            st.info("⚔️ You are carrying a Rusty Dagger (=2 when fighting). ")
        if not st.session_state.action_complete:
            left, right = st.columns(2)
            with left:
                chance_encounter("⚔️ Fight the knight", "The Guard Room", "fight the ghostly knight", 4, "The player defeats the knight and can continue", "You dodge the sword and strike back. The armour crashes down.", "The player escapes the fight but loses 2 health", "The knight strikes you before you can escape", 2, "Rusty Dagger")

            with right:
                chance_encounter("🏃 Run past", "The Guard Room", "running past the ghostly knight", 3, "The player runs past the knight successfully.", "You sprint past the knight and escape through the doorway.", "The player escapes but loses one health while running", "You escape, but the knight's blade catches you as you run.", 1)
            
        else:
            show_result()
            show_continue_button()


# ============================================================
# ROOM 6 — DUNGEON (INVENTORY PERSISTS ACROSS ROOMS)
# ============================================================
 
# see a bottle of red liquid
# left - take it, find a healing potion
# right - leave it, leave the bottle behind

elif room == "dungeon":
    show_room("🧪 The Dungeon", "A bottle of red liquid sits on a stone table.")
    if not st.session_state.action_complete:
        left, right = st.columns(2)
        with left:
            if st.button("🧪 Take the bottle"):
                add_item("Healing Potion")
                outcome = "The player takes the bottle and finds a Healing Potion inside."
                story = generate_story(
                    "The Dungeon",
                    "taking the bottle of red liquid from the stone table",
                    outcome,
                    "You take the bottle from the table and recognize the red liquid as a Healing Potion."
                )
                set_result("item", story, "Healing Potion")
                st.rerun()
        with right:
            if st.button("🚪 Leave it"):
                outcome = "The player leaves the bottle behind and moves on."
                story = generate_story(
                    "The Dungeon",
                    "leaving the bottle of red liquid behind",
                    outcome,
                    "You leave the bottle untouched and move on through the dungeon."
                )
                set_result("story", story)
                st.rerun()
    else:
        show_result()
        if has_item("Healing Potion") and st.session_state.health < st.session_state.max_health:
            if st.button(" Drink Healing Potion"):
                healed = heal_player(2)
                remove_item("Healing Potion")
                story = generate_story(
                    "The Dungeon", "drink the healing potion", 
                    f"The potion restores exactly {healed} health.",
                    "You drink the potion. Warmth spreads through your body."
                )
                set_result("heal", story, healed)
                st.rerun()
        show_continue_button()


# ============================================================
# ROOM 7 — CASTLE GATE (BRANCH BASED ON INVENTORY)
# ============================================================
 
# use the guard room as the template
# check to see if Iron Key held in inventory
# if key in inventory, show button to unlock the gate and escape
# if no key in inventory, show button to climb the wall and escape

elif room == "castle_gate":
    show_room("🏰 The Castle Gate", "You reach the iron gate. Freedom is beyond it")

    if not st.session_state.action_complete:
        if "Iron Key" in st.session_state.inventory:
            st.success(" You have the Iron Key.")
            if st.button(" Unlock the gate"):
                story = generate_story(
                    "The Castle Gate", "unlock the castle gate with the iron key", 
                    "The key works. The player escapes the castle.",
                    "The iron gate swings open and you step into the forest."
                )
                set_result("success", story)
                st.rerun()
        else:
            st.warning("  The gate is locked. You do not have the key.")
            if not st.session_state.action_complete:
                chance_encounter(" Climb the wall", "The castle gate", 
                "climb over the ruined wall", 4, 
                "The player climbs over the wall and escapes the castle", 
                "You climb the ruined wall and land outside", 
                "The player slips, loses 1 health, and does NOT escape", 
                "You slip and crash painfully against a stone wall.", 1)

    else:
        show_result()
        if st.session_state.result_type =="success":
            st.header(" YOU ESCAPED THE CASTLE!")
            st.balloons()
        elif st.session_state.health > 0:
            if st.button(" Try again"):
                st.session_state.action_complete = False
                st.session_state.result_type = ""
                st.session_state.result_message = ""
                st.session_state.result_value = ""
                st.rerun()


        st.divider()
        if st.button(" Play again"):
            restart_game()

