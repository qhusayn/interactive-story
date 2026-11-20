import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
import random
 
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
 
client = genai.Client(api_key=api_key) if api_key else None
 
MODEL_NAME = "gemini-3.5-flash-lite"
 
def roll_dice():
    return random.randint(1,6)

st.write("You need a 4, 5 or 6 to cross a narrow bridge.")
if st.button("🎲 Attempt the bridge"):
    roll = roll_dice()
    st.write(f"You rolled {roll}.")
    if roll == 6:
        st.success("Excellent! A perfect crossing!")
    elif roll == 5:
        st.success("Success! You crossed the bridge well.")
    elif roll ==4:
        st.success("Success! You crossed the bridge safely.")
    elif roll ==3:
        st.error("Failure! You tripped and twisted your ankle, return to the start.")
    elif roll ==2:
        st.error("Failure! You fell from the bridge into water, return to the start.")
    else:
        st.error("Failure! You died.")