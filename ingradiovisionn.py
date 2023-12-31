import streamlit as st
import requests
import os
import base64

# Function to encode the image
def encode_image(image_file):
    return base64.b64encode(image_file.read()).decode('utf-8')

st.set_page_config(layout="wide")

# Streamlit page configuration
st.title("AI Image and Video Analysis")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Display the image
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
    
    # Getting the base64 string
    base64_image = encode_image(uploaded_file)

    # Add buttons
    btn_describe = st.button('Describe')
    btn_key_values = st.button('Key values')
    btn_streamlit_code = st.button('Streamlit')

    # API Key (Replace with your API key)
    api_key = os.getenv("OPENAI_API_KEY")
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Function to make API call
    def make_api_call(text):
        payload = {
            "model": "gpt-4-vision-preview",
            "messages": [
              {
                "role": "user",
                "content": [
                  {
                    "type": "text",
                    "text": text
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
        with st.spinner("Examining image..."):
            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        return response

        if btn_describe:
            response = make_api_call("Describe this image in detail")
            if response.status_code == 200:
                st.write(response.json()['choices'][0]['message']['content'])
            else:
                st.error("Viga API päringus")

        elif btn_key_values:
            response = make_api_call("Extract key value pairs from this image")
            if response.status_code == 200:
                st.write(response.json()['choices'][0]['message']['content'])
            else:
                st.error("Viga API päringus")

        elif btn_streamlit_code:
            response = make_api_call("Generate Streamlit python app full code from this image")
            if response.status_code == 200:
                st.write(response.json()['choices'][0]['message']['content'])
            else:
                st.error("Viga API päringus")
