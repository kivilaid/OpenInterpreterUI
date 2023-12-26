import streamlit as st
import textract
import pandas as pd
from docx import Document
import PyPDF2

def create_upload_file():
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
        st.write(file_details)
        if uploaded_file.type == "application/pdf":
            pdf_reader = PyPDF2.PdfFileReader(uploaded_file)
            text = ""
            for page in range(pdf_reader.getNumPages()):
                text += pdf_reader.getPage(page).extractText()
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            doc = Document(uploaded_file)
            text = ' '.join([paragraph.text for paragraph in doc.paragraphs])
        elif uploaded_file.type == "text/plain":
            text = uploaded_file.getvalue().decode()
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
            df = pd.read_excel(uploaded_file)
            text = df.to_string()
        else:
            st.error("File type not supported.")
            return
        st.text_area("Extracted Text", text, height=200)

if __name__ == "__main__":
    create_upload_file()
