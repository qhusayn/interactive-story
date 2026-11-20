# PRACTISE: Change the tour to add 'reception' and 'workshop'. Add a suitable description to each place. 

import streamlit as st

if "room_number" not in st.session_state:
    st.session_state.room_number = 0
 
if "rooms" not in st.session_state:
    st.session_state.rooms = ["entrance", "gallery"]
 
 
current_room = st.session_state.rooms[st.session_state.room_number]
 
st.title("Museum Tour")
st.write(f"Current Room: {current_room}")
 
if current_room == "entrance":
    st.write("Welcome to the museum entrace")
    if st.button("Continue to Gallery"):
        st.session_state.room_number = 1
        st.rerun()
else:
    st.write("You are in the art gallery, please be quiet")
    