import streamlit as st


st.title("Tap Me App")


name = st.text_input("Enter your name")


age = st.slider("Select your age", 0, 100)


if st.button("Hey Tap me"):
    
    st.write(f"Hello, {name}! You are {age} years old.")
