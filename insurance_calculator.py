import streamlit as st

def home_page():
    st.title('Welcome to TravelSafe Insurance!')
    st.markdown("""
        ## Protect Your Travel, Embrace Adventure
        TravelSafe Insurance provides you with peace of mind, so you can enjoy your journey without worries. 
        Whether you're traveling solo or with loved ones, we've got you covered.

        - **Comprehensive Coverage:** From flight cancellations to medical emergencies, we've got your back.
        - **Flexible Plans:** Tailor your insurance to match your travel needs.
        - **24/7 Support:** Our dedicated team is here to assist you, anytime, anywhere.

        Embark on your next adventure with confidence. Get your travel insurance quote today!
    """)
    st.image("public/oi-web.png", caption='Travel with peace of mind.')

def calculate_insurance(age, bmi, smoking_status):
    base_price = 100
    age_factor = 3 * age
    bmi_factor = 2 * bmi
    smoking_factor = 100 if smoking_status == 'smoker' else 0
    insurance_cost = base_price + age_factor + bmi_factor + smoking_factor
    return insurance_cost
from fpdf import FPDF
import datetime

def create_home_insurance_pdf(form_data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Home Insurance Application", ln=True, align='C')

    for question, answer in form_data.items():
        pdf.cell(200, 10, txt=f"{question}: {answer}", ln=True)

    pdf_file_path = f'home_insurance_application_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.pdf'
    pdf.output(pdf_file_path)
    return pdf_file_path

def home_insurance_page():
    st.title('Home Insurance Application')
    with st.form("home_insurance_form"):
        property_address = st.text_input("Property Address")
        property_value = st.number_input("Property Value", min_value=50000, max_value=10000000, value=250000)
        year_built = st.number_input("Year Built", min_value=1900, max_value=datetime.datetime.now().year, value=1980)
        construction_type = st.selectbox("Construction Type", ["Wood", "Brick", "Stone", "Concrete"])
        security_system = st.selectbox("Security System", ["None", "Alarm", "Surveillance", "Alarm and Surveillance"])
        fire_alarm = st.checkbox("Fire Alarm")
        smoke_detectors = st.checkbox("Smoke Detectors")
        sprinkler_system = st.checkbox("Sprinkler System")
        insurance_history = st.text_area("Previous Insurance Claims History")
        submit_button = st.form_submit_button('Submit Application')

    if submit_button:
        form_data = {
            "Property Address": property_address,
            "Property Value": property_value,
            "Year Built": year_built,
            "Construction Type": construction_type,
            "Security System": security_system,
            "Fire Alarm": fire_alarm,
            "Smoke Detectors": smoke_detectors,
            "Sprinkler System": sprinkler_system,
            "Insurance History": insurance_history
        }
        # Sample calculation (to be replaced with actual logic)
        insurance_cost = property_value * 0.005  # Example: 0.5% of property value
        pdf_file_path = create_home_insurance_pdf(form_data)
        st.success(f"Estimated insurance cost: ${insurance_cost}")
        st.download_button(label="Download Application PDF", data=open(pdf_file_path, "rb"), file_name=pdf_file_path, mime='application/pdf')

def main():
    st.sidebar.title("Navigation")
    menu = ["Home", "Insurance Cost Calculator"]
    menu = ["Home", "Insurance Cost Calculator", "Home Insurance Application"]
    choice = st.sidebar.radio("Menu", menu, index=1)

    if choice == "Home":
        home_page()
    elif choice == "Insurance Cost Calculator":
        st.title('Insurance Cost Calculator')
        # Insurance Cost Calculator form...
    elif choice == "Home Insurance Application":
        home_insurance_page()

    with st.form("insurance_form"):
        cols = st.columns(2)
        with cols[0]:
            departure_date = st.date_input("Departure Date")
            destination = st.text_input("Destination")
            travel_activity_level = st.selectbox("Travel Activity Level", ["Low", "Medium", "High"])
            include_flight_insurance = st.checkbox("Include Flight Insurance")
            age = st.number_input('Age', min_value=18, max_value=100, value=30)
            smoking_status = st.selectbox('Smoking Status', ('Non-smoker', 'Smoker'))
            passport_number = st.text_input("Passport Number")

        with cols[1]:
            return_date = st.date_input("Return Date")
            trip_duration = (return_date - departure_date).days
            st.text(f"Trip Duration: {trip_duration} days")
            accommodation_type = st.selectbox("Accommodation Type", ["Hotel", "Hostel", "Rental", "Other"])
            preexisting_medical_conditions = st.text_area("Pre-existing Medical Conditions")
            include_luggage_insurance = st.checkbox("Include Luggage Insurance")
            bmi = st.number_input('BMI', min_value=10.0, max_value=50.0, value=22.5)
            include_cancellation_insurance = st.checkbox("Include Trip Cancellation Insurance")

        st.header("Insured Individuals")
        number_of_adults = st.number_input("Number of Adults", min_value=1, max_value=10, value=1)
        number_of_children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
        insured_names = st.text_area("Names of Insured Individuals")

        submit_button = st.form_submit_button('Calculate Insurance Cost')

    if submit_button:
        # The calculation logic will be updated to include the new fields
        cost = calculate_insurance(age, bmi, smoking_status, trip_duration, travel_activity_level, accommodation_type, preexisting_medical_conditions, include_flight_insurance, include_luggage_insurance, include_cancellation_insurance, number_of_adults, number_of_children)
        st.subheader(f'Estimated insurance cost: ${cost}')

if __name__ == "__main__":
    main()
