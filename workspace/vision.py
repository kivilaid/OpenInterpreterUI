import streamlit as st
import requests
import os
import base64

# Function to encode the image
def encode_image(image_file):
    return base64.b64encode(image_file.read()).decode('utf-8')

st.set_page_config(layout="wide")

# Streamlit page configuration
st.title("Image Analysis with OpenAI's GPT-4")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Display the image
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
    
    # Getting the base64 string
    base64_image = encode_image(uploaded_file)

    # API Key (Replace with your API key)
    
    api_key = os.getenv("OPENAI_API_KEY")


    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
          {
            "role": "user",
            "content": [
              {
                "type": "text",
                #"text": "Describe the image in detail, extract key value pairs"
                "text": "Generate streamlit app code that looks identical to the image"
              },
              {
                "type": "image_url",
                "image_url": {
                  "url": f"data:image/jpeg;base64,{base64_image}",
                  "detail": "high"
                }
              }
            ]
          }
        ],
        "max_tokens": 1000
    }

    # Send request to OpenAI API
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    # Display the response
    if response.status_code == 200:
        st.write(response.json())
    else:
        st.error("Error in API call")
