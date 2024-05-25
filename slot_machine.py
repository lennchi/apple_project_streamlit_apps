import streamlit as st
from PIL import Image


# def get_fruits(year):
#     """Identify user's generation based on their birth year and get fruit images for them"""
#     # Boomers
#     if year < 1964:
#         return [img_apple, img_strawberry, img_banana], ['37 %', '36 %', '34 %']
#     # Gen X
#     elif 1964 <= year < 1981:
#         return [img_banana, img_strawberry, img_apple], ['42 %', '39 %', '30 %']
#     # Millenials
#     elif 1981 <= year < 1997:
#         return [img_banana, img_strawberry, img_apple], ['42 %', '39 %', '34 %']
#     # Gen Z
#     else:
#         return [img_strawberry, img_banana, img_apple], ['45 %', '34 %', '23 %']


def get_fruits(generation):
    """Identify user's generation based on their birth year and get fruit images for them"""
    # Boomers
    if generation == 'Baby boomer (1940–1963)':
        return [img_apple, img_strawberry, img_banana], ['37 %', '36 %', '34 %']
    # Gen X
    elif generation == 'Gen X (1964–1980)':
        return [img_banana, img_strawberry, img_apple], ['42 %', '39 %', '30 %']
    # Millenials
    elif generation == 'Mileniál (1981–1996)':
        return [img_banana, img_strawberry, img_apple], ['42 %', '39 %', '34 %']
    # Gen Z
    else:
        return [img_strawberry, img_banana, img_apple], ['45 %', '34 %', '23 %']


img_apple = "fruit_icons_apple.jpg"
img_banana = "fruit_icons_banana.jpg"
img_strawberry = "fruit_icons_strawberry.jpg"

# st.title("Generátor generačního ovoce")
st.write("""
# Generátor generačního ovoce
Víš, jaké jsou TOP-3 ovoce pro tvou generaci?
         """)

# User input for birth year
# birth_year = st.number_input("Zadej rok narození: ", min_value=1940, max_value=2012, step=1)
generation = st.selectbox("", options=['Baby boomer (1940–1963)', 'Gen X (1964–1980)', 'Mileniál (1981–1996)', 'Gen Z (1997–2012)'])

# Slot machine button
if st.button("Dáme ovoce!"):
    images = get_fruits(generation)[0]
    captions = get_fruits(generation)[1]
    slot_1, slot_2, slot_3 = st.columns(3)




    with slot_1:
        img_1 = Image.open(images[0])
        cap_1 = captions[0]
        st.image(img_1, caption=cap_1)

    with slot_2:
        img_2 = Image.open(images[1])
        cap_2 = captions[1]
        st.image(img_2, caption=cap_2)

    with slot_3:
        img_3 = Image.open(images[2])
        cap_3 = captions[2]
        st.image(img_3, caption=cap_3)

