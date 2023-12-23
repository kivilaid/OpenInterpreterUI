import streamlit as st

def calculate_insurance(age, bmi, smoking_status):
    base_price = 100
    age_factor = 3 * age
    bmi_factor = 2 * bmi
    smoking_factor = 100 if smoking_status == 'smoker' else 0
    insurance_cost = base_price + age_factor + bmi_factor + smoking_factor
    return insurance_cost

def main():
    st.title('Insurance Cost Calculator')

    with st.expander("Trip Details"):
        # Placeholder for trip details inputs
        st.date_input("Departure")
        st.date_input("Return")
        st.text_input("Destination")

    with st.expander("Risk Factors"):
        # Placeholder for risk factors inputs
        st.selectbox("Travel activity level", ["Low", "Medium", "High"])
        st.selectbox("Accommodation type", ["Hotel", "Hostel", "Rental", "Other"])

    with st.expander("Options"):
        # Placeholder for additional options
        st.checkbox("Include flight insurance")
        st.checkbox("Include luggage insurance")

    with st.expander("Insured Individuals"):
        # Placeholder for insured individuals details
        st.number_input("Number of adults", min_value=1, max_value=10, value=1)
        st.number_input("Number of children", min_value=0, max_value=10, value=0)

    age = st.number_input('Enter your age', min_value=18, max_value=100, value=30)
    bmi = st.number_input('Enter your BMI', min_value=10.0, max_value=50.0, value=22.5)
    smoking_status = st.selectbox('Do you smoke?', ('non-smoker', 'smoker'))

    if st.button('Calculate Insurance Cost'):
        cost = calculate_insurance(age, bmi, smoking_status)
        st.subheader(f'Estimated insurance cost: ${cost}')

if __name__ == "__main__":
    main()
