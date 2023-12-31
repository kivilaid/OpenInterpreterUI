import streamlit as st
import os
import fitz  # PyMuPDF
import openai
import json
from docx import Document
import pandas as pd

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

def extract_text_from_docx(file_path):
    try:
        doc = Document(file_path)
        text = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
        return text
    except Exception as e:
        return str(e)

def extract_key_value_pairs_gpt(text, json_file_path):
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

        response_data = json.loads(response.choices[0].message['content'])
        
        # Save response data as JSON
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(response_data, json_file, ensure_ascii=False, indent=4)

        return response_data
    except Exception as e:
        return str(e)

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

def main():
    st.title("File Upload and Format Detection")

    # Create a directory to save files
    if not os.path.exists('uploaded_files'):
        os.makedirs('uploaded_files')

    uploaded_file = st.file_uploader("Upload a file", type=['pdf', 'docx'])
    if uploaded_file is not None:
        # Display file details
        file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type}
        st.write(file_details)

        # Save the file
        if save_uploaded_file(uploaded_file):
            file_path = os.path.join("uploaded_files", uploaded_file.name)
            st.success("File Saved")

            # Check the file type and process accordingly
            if uploaded_file.type == "application/pdf":
                text = extract_text_from_pdf(file_path)
            elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                text = extract_text_from_docx(file_path)
            else:
                st.error("Unsupported file type")
                return

            # Prepare JSON file path
            json_file_name = os.path.splitext(uploaded_file.name)[0] + ".json"
            json_file_path = os.path.join("uploaded_files", json_file_name)

            # Send text to GPT-4 for key-value pair extraction
            key_value_pairs = extract_key_value_pairs_gpt(text, json_file_path)

            if isinstance(key_value_pairs, dict):
                # Flatten the JSON structure if it contains nested objects or arrays
                flattened_data = flatten_json(key_value_pairs)

                # Convert to DataFrame for display
                df = pd.DataFrame(list(flattened_data.items()), columns=['Key', 'Value'])
                st.write("Extracted Key-Value Pairs from GPT-4:")
                st.table(df)

                # Display the JSON data
                st.json(key_value_pairs, expanded=True)
            else:
                st.error("Error in key-value pair extraction: " + str(key_value_pairs))
        else:
            st.error("Error saving file")

if __name__ == "__main__":
    main()
