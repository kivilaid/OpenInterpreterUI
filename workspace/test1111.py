import streamlit as st

st.set_page_config(page_title="Sisesta sõiduki registreerimismärk")

# Custom styles
st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
        font-weight: bold;
    }
    .green-button {
        background-color: #4CAF50; 
        color: white; 
        padding: 0.25em 0.5em;
        border: none;
        border-radius: 0.3em;
        font-size: 1em;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

# Page title
st.markdown('<div class="big-font">Sisesta sõiduki registreerimismärk</div>', unsafe_allow_html=True)

# Input for vehicle registration number
vehicle_reg = st.text_input("", placeholder="123 ABC")

# Text below the text input
st.markdown("""
Palun valige Inges Kindlustuse liikluskindlustuse lepingute sõlmimisel ja uuendamisel sõiduki kasutusala! Täpsemalt saab lugeda [siit](#)!
""")

# Radio buttons for usage options
usage_options = ["Tavakasutus", "Takso", "Õppesõiduk", "Alarmsõiduk", "Lühirent", "Ohtlikud veosed", "Kuller"]
st.radio("Palun valige kasutusala:", usage_options)

# Submit button
if st.button("VAATA HINDA", key='submit', help="Submit to see price"):
    # You can put the logic here to calculate the price or any other action required when the button is pressed
    st.success("Hind on vaadatud!")