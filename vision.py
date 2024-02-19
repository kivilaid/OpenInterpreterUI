import streamlit as st
import requests
import os
import base64

# Function to encode the image
def encode_image(image_file):
    return base64.b64encode(image_file.read()).decode('utf-8')

# Function to send data to webhook
def send_to_webhook(filename, openai_response):
    webhook_url = "https://hook.eu2.make.com/yjhba9ogkl2011loe9m6bmprib8zr6su"
    data = {
        "filename": filename, 
        "openai_response": openai_response,
        "image_url": image_url
    }
    response = requests.post(webhook_url, json=data)
    return response

st.set_page_config(layout="wide")
st.title("AI Image and Video Analysis")

uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, use_column_width=True)
    base64_image = encode_image(uploaded_file)
    image_url = f"data:image/jpeg;base64,{base64_image}"

    # Add radio buttons
    analysis_option = st.radio(
        "Choose analysis type:",
        ('Describe', 'Key values', 'Streamlit'),
        horizontal=True
    )

    # Add wide button
    analyze_button = st.button('Analyze', key="analyze")

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
                      "url": image_url,
                      "detail": "high"
                    }
                  }
                ]
              }
            ],
            "max_tokens": 1000
        }
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        return response

    # Handling Analyze button action
    if analyze_button:
        action_text = {
            'Describe': "Describe this image in detail",
            'Key values': "Extract key value pairs from this image",
            'Streamlit': "Generate Streamlit python app full code from this image"
        }.get(analysis_option, "Describe this image in detail")

        with st.spinner("Examining image..."):
            response = make_api_call(action_text)
            if response.status_code == 200:
                st.success("Done")
                openai_response = response.json()['choices'][0]['message']['content']
                st.write(openai_response)

                # Send data to webhook
                webhook_response = send_to_webhook(uploaded_file.name, openai_response)
                
            else:
                st.error("Viga API päringus")
