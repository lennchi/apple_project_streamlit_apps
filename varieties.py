import pandas as pd
import streamlit as st
import random

df = pd.read_csv("seznam_odrud.csv", encoding='utf-8')

# Make a list of varieties, strip off junk chars
df = df['Název odrůdy']
varieties = df.to_list()
varieties = [variety.strip('\xa0') for variety in varieties]

# Create a random variety picker
st.title('🍎 Jablko pro tebe 🍎')

if st.button('Vylosuj si odrůdu'):
    your_apple = random.choice(varieties)
    st.write(your_apple)
