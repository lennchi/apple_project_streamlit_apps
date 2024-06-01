# import pandas as pd
# import streamlit as st
# import random
#
# df = pd.read_csv("seznam_odrud.csv", encoding='utf-8')
#
# # Make a list of varieties, strip off junk chars
# df = df['Název odrůdy']
# varieties = df.to_list()
# varieties = [variety.strip('\xa0') for variety in varieties]
#
# # Create a random variety
#
# st.set_page_config(
#     page_title="Jablko pro tebe",
#     page_icon="🍎",
#     layout="centered"
# )
#
# st.title('🍎 Jablko pro tebe 🍎')
# st.write('&nbsp;')
#
# if st.button('Vylosuj si odrůdu'):
#     your_apple = random.choice(varieties)
#     st.subheader(your_apple)


import pandas as pd
import streamlit as st
import random

# Load the data
df = pd.read_csv("seznam_odrud.csv", encoding='utf-8')

# Make a list of cultivars, strip off junk chars
varieties = df['Název odrůdy'].to_list()
varieties = [variety.strip('\xa0') for variety in varieties]

# Set page config
st.set_page_config(
    page_title="Jablko pro tebe",
    page_icon="🍎",
    layout="centered"
)

# Markdown for centering
st.markdown(
    """
    <style>
    .centered {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 50px;
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

# Title
# st.markdown('<div class="centered">', unsafe_allow_html=True)
# st.title('🍎 Jablko pro tebe 🍎')
# st.markdown('</div>', unsafe_allow_html=True)

# Center H1 header
header1 = '🍎 Jablko pro tebe 🍎'
st.markdown(f'<div class="centered"><h1>{header1}</h1></div>', unsafe_allow_html=True)


# Center button and output
# button = st.button('Vylosuj si odrůdu')

st.markdown('<div class="centered">', unsafe_allow_html=True)
button = st.button('Vylosuj si odrůdu')
st.markdown('</div>', unsafe_allow_html=True)

if button:
    your_apple = random.choice(varieties)
    st.markdown(f'<div class="centered"><h2>{your_apple}</h2></div>', unsafe_allow_html=True)
