import streamlit as st
# Main title
st.title('Build your own digital insurance company')
# Creating a login form in the sidebar
with st.sidebar:
    with st.form("login_form"):
        email = st.text_input("","Email")
        password = st.text_input("", type="password")
        submitted = st.form_submit_button("Sign in",use_container_width=True)
        if submitted:
            st.success("You have been logged in!")
        if st.button("Reset Password"):
            st.info("A password reset link has been sent to your email.")
# Here you can add the main content of your app