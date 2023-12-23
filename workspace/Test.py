
import streamlit as st


def main():

    st.sidebar.title('Menu')
menu_options = ['Home', 'Gallery', 'Contact']
menu_choice = st.sidebar.selectbox('Choose a page:', menu_options)

st.title("love")
st.markdown("<style>body {background-color: lightgrey;}</style>", unsafe_allow_html=True)


if __name__ == '__main__':

# Create a 3x3 grid for image placeholders
    for i in range(3):
        cols = st.columns(3)
        for col in cols:
            col.image('https://via.placeholder.com/150/0000FF/808080?Text=Tuned+Car', caption='Placeholder')

    main()  
