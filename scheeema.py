
import streamlit as st
from datetime import datetime

def main():
    st.title("Insurance Data Input")

    # Part 1 - Standard Fields
    insured_name = st.text_input("Insured Name")
    underwriter = st.selectbox("Underwriter", ["", "Adam", "Adesola", "Agustin", "Bram", "Debbie", "George", "Henrik", "Joaquin", "Oli", "Sarah", "Tram", "Will"])
    underwriting_assistant = st.selectbox("Underwriting Assistant", ["", "Adam", "Agustin", "Bram", "Joaquin", "Sarah", "Tram", "Will"])
    new_renewal = st.selectbox("New/Renewal", ["", "New", "Renewal"])
    inception = st.date_input("Inception", datetime.today())
    expiry = st.date_input("Expiry", datetime.today())
    broker_name = st.selectbox("Broker Name", ["", "TBC"])
    broker_company = st.selectbox("Broker Company", ["", "TBC"])
    currency = st.selectbox("Currency", ["", "USD", "EUR", "GBP", "Other"])  # Example currencies
    product = st.selectbox("Product", ["", "Insurance", "Reinsurance", "Lead Insurance", "Fronting"])

    # Part 2A - Additional Fields for Insurance or Lead Insurance
    if product in ["Insurance", "Lead Insurance"]:
        insured_country = st.selectbox("Insured Country", ["", "TBA"])  # Placeholder for country list

    # Part 2B - Additional Fields for Reinsurance
    if product == "Reinsurance":
        cedant = st.selectbox("Cedant", ["", "TBA"])  # Placeholder for cedant list
        cedant_country = st.selectbox("Cedant Country", ["", "TBA"])  # Placeholder for country list

    # Submit button
    if st.button("Submit"):
        st.write("Data Submitted:")
        st.write(f"Insured Name: {insured_name}")
        st.write(f"Underwriter: {underwriter}")
        st.write(f"Underwriting Assistant: {underwriting_assistant}")
        st.write(f"New/Renewal: {new_renewal}")
        st.write(f"Inception: {inception}")
        st.write(f"Expiry: {expiry}")
        st.write(f"Broker Name: {broker_name}")
        st.write(f"Broker Company: {broker_company}")
        st.write(f"Currency: {currency}")
        st.write(f"Product: {product}")
        if product in ["Insurance", "Lead Insurance"]:
            st.write(f"Insured Country: {insured_country}")
        if product == "Reinsurance":
            st.write(f"Cedant: {cedant}")
            st.write(f"Cedant Country: {cedant_country}")

if __name__ == "__main__":
    main()
