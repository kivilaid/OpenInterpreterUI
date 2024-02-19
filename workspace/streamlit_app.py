
import streamlit as st
from PyPDF2 import PdfReader
import subprocess
import os

def extract_text_from_pdf(pdf_path):
    pdf = PdfReader(pdf_path)
    text = ''
    for page in pdf.pages:
        text += page.extract_text() + ''
    return text

def convert_text_to_docx(text, docx_path):
    temp_txt_path = './workspace/temp_text.txt'
    with open(temp_txt_path, 'w', encoding='utf-8') as file:
        file.write(text)
    subprocess.run(['pandoc', temp_txt_path, '-o', docx_path], check=True)
    os.remove(temp_txt_path)
    return docx_path

st.title('PDF to DOCX Converter')
st.header('Upload your PDF')
uploaded_file = st.file_uploader('Choose a file', type='pdf')
if uploaded_file is not None:
    st.write('File uploaded successfully!')
    with open('./workspace/uploaded_file.pdf', 'wb') as f:
        f.write(uploaded_file.getbuffer())
    if st.button('Convert to DOCX'):
        text = extract_text_from_pdf('./workspace/uploaded_file.pdf')
        docx_path = './workspace/converted_file.docx'
        convert_text_to_docx(text, docx_path)
        with open(docx_path, 'rb') as file:
            st.download_button(label='Download DOCX', data=file, file_name='converted_file.docx')
