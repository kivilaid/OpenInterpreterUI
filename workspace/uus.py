streamlitimport streamlit as st

def create_upload_file():
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        st.write(bytes_data)

if __name__ == "__main__":
    create_upload_file()
