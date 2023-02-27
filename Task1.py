import streamlit as st
import pandas as pd

data = pd.read_csv("data.txt")

st.title("Iris Data Explorer")

st.sidebar.subheader("Filter data")

species = st.sidebar.selectbox("Species", data.species.unique())
filtered_data = data[data.species == species]

st.write("Displaying data for species:", species)
st.write(filtered_data)
