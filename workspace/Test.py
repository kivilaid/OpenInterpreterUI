
import streamlit as st
import random


def main():

    st.sidebar.title('Menu')
menu_options = ['Home', 'Gallery', 'Contact']
menu_choice = st.sidebar.selectbox('Choose a page:', menu_options)

st.title("love")
st.markdown("<style>body {background-color: lightgrey;}</style>", unsafe_allow_html=True)


if __name__ == '__main__':
    # List of URLs for images of huge cars
    car_images = [
        'https://example.com/huge_car1.jpg',
        'https://example.com/huge_car2.jpg',
        'https://example.com/huge_car3.jpg',
        # Add more image URLs as needed
    ]


# Create a 3x3 grid for image placeholders
    for i in range(3):
        cols = st.columns(3)
        for col in cols:
            # Randomly select an image of a huge car
            random_car_image = random.choice(car_images)
            col.image(random_car_image, caption='Huge Car')

    main()  
