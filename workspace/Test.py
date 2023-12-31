import streamlit as st
# Set up the page layout
st.set_page_config(layout="wide", page_title=None, page_icon=None, initial_sidebar_state="auto", menu_items={'Get Help': None, 'Report a bug': None, 'About': None, 'Get started': None})
# Top-level header with welcome message and current time
st.title(f"Good morning, Ando Kivilaid!")
st.subheader("Monday, 25 December, 2023 9:32")
# Sidebar for navigation
with st.sidebar:
    st.header("Navigation")
    st.button("New quote")
    st.button("Policies")
    st.button("Quotes")
    st.button("Customers")
    st.button("Invoicing")
    st.button("Reporting")
    st.button("Tools")
# Main section
with st.container():
    # Add new Quote Section
    st.header("Add new Quote")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.button("Travel Insurance")
    with col2:
        st.button("Errors and Omissions")
    with col3:
        st.button("Underwriting Information")
    with col4:
        st.button("Property Owners Insurance")
    # Information about us
    st.header("Information about us")
    st.markdown("""
    1. About us
    2. Features
    3. Blog
    4. Brokers and Agents
    """)
# Latest quotes and policies
with st.container():
    st.header("Latest quotes")
    st.table(data=[{"Product": "Sports Memorabilia", "Quote nr": "100000001", "Customer": "ando", "Broker": "Test", "Start": "26.07.2023", "End": "25.07.2024", "Calculated": "-", "Issuer": "Sergei Pozniak", "Premium": "0,00", "Status": "Created"}])
    st.header("Latest policies")
    # This could be filled with actual data
    st.table(data=[{"Product": "Product Name", "Policy No": "123456", "Customer": "Customer Name", "Broker": "Broker Name", "Start": "Start Date", "End": "End Date", "Issued": "Issued Date", "Premium": "Premium Amount", "Last Action": "Last Action"}])
# To run the app, save this script as a .py file and run it using the Streamlit command.
# streamlit run your_script.py