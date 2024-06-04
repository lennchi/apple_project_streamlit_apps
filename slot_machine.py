import streamlit as st
from PIL import Image
import random
import time


def get_fruits(generation):
    """Get fruit images and percent captions based on user's chosen generation"""
    # Boomers
    if generation == 'Baby boomer (1940–1963)':
        return [img_apple, img_strawberry, img_banana], ['37 %', '36 %', '34 %']
    # Gen X
    elif generation == 'Gen X (1964–1980)':
        return [img_banana, img_strawberry, img_apple], ['42 %', '39 %', '34 %']
    # Millenials
    elif generation == 'Mileniál (1981–1996)':
        return [img_banana, img_strawberry, img_apple], ['42 %', '39 %', '30 %']
    # Gen Z
    else:
        return [img_strawberry, img_banana, img_apple], ['45 %', '34 %', '23 %']


def flash_images():
    imgs = [img_apple, img_banana, img_strawberry, img_lemon, img_grape, img_cherry]
    return random.choice(imgs)


# Images of fruit
img_apple = "img/fruit_icons_apple.jpg"
img_banana = "img/fruit_icons_banana.jpg"
img_strawberry = "img/fruit_icons_strawberry.jpg"
img_lemon = "img/fruit_icons_lemon.jpg"
img_grape = "img/fruit_icons_grape.jpg"
img_cherry = "img/fruit_icons_cherry.jpg"

# st.title("Generátor generačního ovoce")
st.write("""
# Generátor generačního ovoce
Víš, jaké jsou TOP-3 ovoce pro tvou generaci?
         """)

# User input for birth year/generation
# birth_year = st.number_input("Zadej rok narození: ", min_value=1940, max_value=2012, step=1)
generation = st.selectbox("", options=['Baby boomer (1940–1963)', 'Gen X (1964–1980)', 'Mileniál (1981–1996)', 'Gen Z (1997–2012)'])

# Slot machine button
if st.button("Dáme ovoce!"):
    slot_1, slot_2, slot_3 = st.columns(3)

    # Placeholders for the images
    img1_placeholder = slot_1.empty()
    img2_placeholder = slot_2.empty()
    img3_placeholder = slot_3.empty()

    end_time = time.time() + 2

    while time.time() < end_time:
        img1_placeholder.image(Image.open(flash_images()), use_column_width=True)
        img2_placeholder.image(Image.open(flash_images()), use_column_width=True)
        img3_placeholder.image(Image.open(flash_images()), use_column_width=True)
        time.sleep(0.03)

    # # Flash images
    # while time.time() < end_time:
    #     with slot_1:
    #         img1 = slot_1.empty()
    #         img1 = Image.open(flash_images())
    #         st.image(img1, use_column_width=True)
    #     with slot_2:
    #         img2 = slot_2.empty()
    #         img2 = Image.open(flash_images())
    #         st.image(img2, use_column_width=True)
    #     with slot_3:
    #         img3 = slot_3.empty()
    #         img3 = Image.open(flash_images())
    #         st.image(img3, use_column_width=True)
    #     time.sleep(0.5)  # Adjust the speed of flashing

    # Show gen fruit images
    images = get_fruits(generation)[0]
    captions = get_fruits(generation)[1]

    img1_placeholder.image(Image.open(images[0]), caption=captions[0], use_column_width=True)
    img2_placeholder.image(Image.open(images[1]), caption=captions[1], use_column_width=True)
    img3_placeholder.image(Image.open(images[2]), caption=captions[2], use_column_width=True)

    # with slot_1:
    #     img_1 = Image.open(images[0])
    #     cap_1 = captions[0]
    #     st.image(img_1, caption=cap_1)
    #
    # with slot_2:
    #     img_2 = Image.open(images[1])
    #     cap_2 = captions[1]
    #     st.image(img_2, caption=cap_2)
    #
    # with slot_3:
    #     img_3 = Image.open(images[2])
    #     cap_3 = captions[2]
    #     st.image(img_3, caption=cap_3)

