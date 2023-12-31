import streamlit as st

def create_authentication_interface():
    st.title("Turvaline autentimine asutuste e-teenustes")

    authentication_methods = ["ID-kaart", "Mobiil-ID", "Smart-ID", "EU eID"]
    selected_method = st.radio("Choose authentication method:", authentication_methods)

    if selected_method == "Smart-ID":
        st.image("logo_smart_id.png", width=100)  # Replace with the actual logo image path
        st.header("Smart-ID")

        st.markdown("""
            Teenusesse eesti.ee sisselogimiseks vajate kehtivat Smart-ID kontot. Sisestage oma isikukood
            ning vajutage "Jätka". Seejärel saadetakse Teie Smart-ID rakendusse kontrollkood.
        """)

        personal_id = st.text_input("Isikukood", max_chars=11, value="EE")
        if st.button("Jätka"):
            st.success("Authentication process would start here.")
    # Here you can add more cases for other authentication methods

    st.markdown("---")
    st.markdown("Tagasi teenusepakkuja juurde")
    if st.button("Abi smart-id.com lehelt"):
        st.write("Help page would be opened.")

create_authentication_interface()