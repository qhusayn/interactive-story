import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
 
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
 
client = genai.Client(api_key=api_key) if api_key else None
 
MODEL_NAME = "gemini-3.5-flash-lite"
 
exhibits = {
    "Roman coin": "The visitor reads a label explaining that the coin is about 2,000 years old.",
    "Dinosaur fossil": "The visitor learns that the fossil belongs to a plant-eating dinosaur.",
    "Ancient pottery": "The visitor discovers that the pot was used for storing food.",
    "Egyptian mummy": "The visitor learns that the mummy was preserved for burial.",
    "Medieval sword": "The visitor discovers that the sword was used by a knight.",
    "Moon rock": "The visitor learns that the rock was brought back from the Moon.",
}
 
def make_prompt(name, exhibit, outcome):
    """Put the role, context, fixed outcome and constraints together."""
    return f"""
Role: You are a friendly museum exhibit narrator.
Context: A visitor named {name} is looking at the {exhibit} exhibit.
Fixed outcome: {outcome}
Constraints:
- Write in second person (you / your).
- Use a child like tone, as if the visitor is an idiot.
- Describe the discovery in 30-50 words.
- Do not change the fixed outcome.
- Do not let the visitor take objects or invent new discoveries.
- Do not introduce new decisions for the visitor.
Return only the short description.
"""  

def generate_description(prompt, fallback):
    if client is None:
        return fallback, "No API key found. Showing fallback description."
 
    try:
        interaction = client.interactions.create(
            model=MODEL_NAME,
            input=prompt,
            generation_config={"thinking_level": "minimal"},
        )
 
        description = interaction.output_text
        if not description:
            return fallback, "Gemini returned no text. Showing fallback description."
 
        return description, None
 
    except Exception as error:
        return fallback, (
            f"The API request failed ({type(error).__name__}). "
            "Showing the fallback."
        )
 
 
st.set_page_config(page_title="Museum", page_icon="🏛️")
st.title("🏛️ Museum")
 
name = st.text_input("Visitor's name")
exhibit = st.selectbox("Choose an exhibit", list(exhibits))
outcome = exhibits[exhibit]
 
prompt = make_prompt(name, exhibit, outcome)
 
if st.button("✨ Generate a description"):
    with st.spinner("Asking Gemini..."):
        description, message = generate_description(prompt, outcome)
 
    st.write(description)
    if message:
        st.warning(message)
