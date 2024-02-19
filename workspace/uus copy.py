import streamlit as st
import os
import fitz  # PyMuPDF
import openai
import json

def save_uploaded_file(uploaded_file):
    try:
        with open(os.path.join("uploaded_files", uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
        return True
    except:
        return False

def extract_text_from_pdf(file_path):
    try:
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        return str(e)

def extract_key_value_pairs_gpt(text):
    try:
        # Set your OpenAI API key
        openai.api_key = os.getenv("OPENAI_API_KEY")

        response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",
            response_format={ "type": "json_object" },
            messages=[
                {
                    "role": "system",
                    "content": "You are helpful and precise key-value pair extractor. Respond in JSON format."
                },
                {
                    "role": "user",
                    "content": text
                }
            ],
            temperature=0.3,
            max_tokens=4000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        return json.loads(response.choices[0].message['content'])
    except Exception as e:
        return str(e)

def main():
    st.title("File Upload and Format Detection")

    # Create a directory to save files
    if not os.path.exists('uploaded_files'):
        os.makedirs('uploaded_files')

    uploaded_file = st.file_uploader("Upload a file", type=None)
    if uploaded_file is not None:
        # Display file details
        file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type}
        st.write(file_details)

        # Save the file
        if save_uploaded_file(uploaded_file):
            file_path = os.path.join("uploaded_files", uploaded_file.name)
            st.success("File Saved")

            # If the file is a PDF, extract text and send to GPT-4
            if uploaded_file.type == "application/pdf":
                text = extract_text_from_pdf(file_path)
                key_value_pairs = extract_key_value_pairs_gpt(text)
                st.write("Extracted Key-Value Pairs from GPT-4:")
                st.text_area("Key-Value Pairs", key_value_pairs, height=300)
        else:
            st.error("Error saving file")

if __name__ == "__main__":
    main()
