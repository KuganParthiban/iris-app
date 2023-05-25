import streamlit as st
import numpy as np

st.title("Create a Selectbox")

contact_options = ["Email", "Phone", "WhatsApp"]

st.header("Selectbox from a list")

contact_selected = st.selectbox("How would you like to be contacted ?",
                                options=contact_options)

st.write("Selectbox returns:", contact_selected,
         "of type", type(contact_selected))