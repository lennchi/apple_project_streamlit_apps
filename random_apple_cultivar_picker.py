import pandas as pd
import streamlit as st
import random
import base64


# PANDAS
# Load the data
df = pd.read_csv("seznam_odrud.csv", encoding='utf-8')

# Make a list of cultivars, strip off junk chars
varieties = df['Název odrůdy'].to_list()
varieties = [variety.strip('\xa0') for variety in varieties]


# STREAMLIT
# Set page config
st.set_page_config(
    page_title="Jablko pro tebe",
    page_icon="🍎",
    layout="centered"
)

# CSS markdown for centering
st.markdown(
    """
    <style>
    .centered {
        justify-content: center;
        align-items: center;
    }
    .centered h1 {
        text-align: center;
    }
    .centered div {
        text-align: center;
    }
    .stButton button {
        display: block;
        margin: 0 auto;
    }       
    </style>
    """,
    unsafe_allow_html=True
)

# Center apple img
st.image('img/streamlit_apple_900.png')

# Center the header
header = 'Jablko pro tebe'
st.markdown(f'<div class="centered"><h1>{header}</h1></div>', unsafe_allow_html=True)

# Center the button
st.markdown('<div class="centered">', unsafe_allow_html=True)
button = st.button('Vylosuj si odrůdu')
st.markdown('</div>', unsafe_allow_html=True)

# Button behavior and output
if button:
    your_apple = random.choice(varieties)
    st.markdown(f'<div class="centered"><h2>{your_apple}</h2></div>', unsafe_allow_html=True)
