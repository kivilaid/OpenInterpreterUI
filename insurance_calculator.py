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

    st.header("Trip Details")
    departure_date = st.date_input("Departure Date")
    return_date = st.date_input("Return Date")
    destination = st.text_input("Destination")
    trip_duration = (return_date - departure_date).days
    st.text(f"Trip Duration: {trip_duration} days")

    st.header("Risk Factors")
    travel_activity_level = st.selectbox("Travel Activity Level", ["Low", "Medium", "High"])
    accommodation_type = st.selectbox("Accommodation Type", ["Hotel", "Hostel", "Rental", "Other"])
    preexisting_medical_conditions = st.text_area("Pre-existing Medical Conditions")

    st.header("Options")
    include_flight_insurance = st.checkbox("Include Flight Insurance")
    include_luggage_insurance = st.checkbox("Include Luggage Insurance")
    include_cancellation_insurance = st.checkbox("Include Trip Cancellation Insurance")

    st.header("Insured Individuals")
    number_of_adults = st.number_input("Number of Adults", min_value=1, max_value=10, value=1)
    number_of_children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
    insured_names = st.text_area("Names of Insured Individuals")

    st.header("Personal Details")
    age = st.number_input('Age', min_value=18, max_value=100, value=30)
    bmi = st.number_input('BMI', min_value=10.0, max_value=50.0, value=22.5)
    smoking_status = st.selectbox('Smoking Status', ('Non-smoker', 'Smoker'))
    passport_number = st.text_input("Passport Number")

    if st.button('Calculate Insurance Cost'):
        # The calculation logic will be updated to include the new fields
        cost = calculate_insurance(age, bmi, smoking_status, trip_duration, travel_activity_level, accommodation_type, preexisting_medical_conditions, include_flight_insurance, include_luggage_insurance, include_cancellation_insurance, number_of_adults, number_of_children)
        st.subheader(f'Estimated insurance cost: ${cost}')

if __name__ == "__main__":
    main()
