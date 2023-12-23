
import streamlit as st
import random


def main():
    st.sidebar.title('Menu')
    menu_options = ['Home', 'Gallery', 'Contact', 'Travel insurance']
    menu_choice = st.sidebar.selectbox('Choose a page:', menu_options)

    st.title("love")
    st.markdown("<style>body {background-color: lightgrey;}</style>", unsafe_allow_html=True)

    # List of URLs for images of huge cars
    car_images = [
        'https://example.com/huge_car1.jpg',
        'https://example.com/huge_car2.jpg',
        'https://example.com/huge_car3.jpg',
        # Add more image URLs as needed
    ]

    
if menu_choice == 'Travel insurance':
    with st.form('travel_insurance_form'):
        st.write('Travel Insurance Calculator')
        age = st.number_input('Age', min_value=18, max_value=100, step=1)
        destination = st.text_input('Destination')
        duration = st.number_input('Duration of Travel (days)', min_value=1, max_value=365, step=1)
        submit_button = st.form_submit_button('Calculate')
        if submit_button:
            st.write('Calculation would be performed here.')
# Create a 3x3 grid for image placeholders
for i in range(3):
    cols = st.columns(3)
    for col in cols:
        # Randomly select an image of a huge car
        random_car_image = random.choice(car_images)
        col.image(random_car_image, caption='Huge Car')

if __name__ == '__main__':
    main()
