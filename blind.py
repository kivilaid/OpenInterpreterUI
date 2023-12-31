import streamlit as st
import requests
import os
import openai
import base64
from IPython.display import Audio

api_key = os.getenv("OPENAI_API_KEY")

# Function to encode the image
def encode_image(image_file):
    return base64.b64encode(image_file.read()).decode('utf-8')

def text_to_speech(text):
    response = openai.audio.speech.create(
        model="tts-1-hd",
        voice="alloy",
        input=text,
    )
    response.stream_to_file("output.mp3")    
    return response['audio']

st.set_page_config(layout="wide",page_title="AI Image and Video Analysis",page_icon="🧊")

st.title("AI Image and Video Analysis")

uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

openai_response = "I got nothing to say"


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
    analyze_button = st.button('Analyze', key="analyze",use_container_width=True, on_click=None)

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

            # Add a button for text-to-speech after successful response
    if st.button('Convert to Speech', key="tts"):
        # with st.spinner("Converting text to speech..."):
        audio_url = text_to_speech(openai_response)
        if audio_url:
            st.audio(audio_url, format='audio/mp3', start_time=0)
        else:
            st.error("Error in text to speech API call")
        # st.success("Done")        

        # Send data to webhook
        # webhook_response = send_to_webhook(uploaded_file.name, openai_response)
                
        # else:
        # st.error("Viga API päringus")
