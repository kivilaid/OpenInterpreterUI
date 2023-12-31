import streamlit as st
from gpt4v import GPT4Vision
from gpttts import GPTTTS
from openai import OpenAI
import os

# Initialize GPT4Vision and OpenAI client
image = GPT4Vision()
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
talk = GPTTTS(client)

st.set_page_config(page_title="Miracle", page_icon="🤖", layout="wide")


def main():


    col1, col2, col3 = st.columns(spec=[1,1,1],gap="small")

    with col1:
#    st.image("https://static.streamlit.io/examples/cat.jpg")

        language = st.selectbox("Select language", options=["Afrikaans", "Arabic", "Armenian", "Azerbaijani", "Belarusian", "Bosnian", "Bulgarian", "Catalan", "Chinese", "Croatian", "Czech", "Danish", "Dutch", "English", "Estonian", "Finnish", "French", "Galician", "German", "Greek", "Hebrew", "Hindi", "Hungarian", "Icelandic", "Indonesian", "Italian", "Japanese", "Kannada", "Kazakh", "Korean", "Latvian", "Lithuanian", "Macedonian", "Malay", "Marathi", "Maori", "Nepali", "Norwegian", "Persian", "Polish", "Portuguese", "Romanian", "Russian", "Serbian", "Slovak", "Slovenian", "Spanish", "Swahili", "Swedish", "Tagalog", "Tamil", "Thai", "Turkish", "Ukrainian", "Urdu", "Vietnamese", "Welsh"],index=13)


    # 1. Let user upload an image or video, or use camera to capture an image
        uploaded_file = st.file_uploader("Upload image or video", label_visibility="hidden", type=["jpg", "jpeg", "png", ".gif", ".webp"])

    with col3:
#    st.image("https://static.streamlit.io/examples/dog.jpg")

        camera_image = st.camera_input("Or take a picture", label_visibility="hidden")

    # Use the uploaded file or the camera image, whichever is available
    file_to_process = uploaded_file if uploaded_file is not None else camera_image

    if file_to_process is not None:
        # Display the uploaded or captured image
        
        with col2:
        
            st.image(file_to_process, caption="Image")

        # 2. Send the file to GPT4Vision for explanation
        with st.spinner("Generating explanation..."):
            explanation = image.describe(image_file=file_to_process, user_message="Describe this image in language:"+language)
        st.success(explanation)
        # 3. Display the explanation
        # st.write(explanation)

        # 4. Send response to GPTTTS to be spoken
        with st.spinner("Generating audio..."):
            audio_file_path = talk.generate_speech(text=explanation, model="tts-1-hd", voice="alloy")
        # 5. Play audio automatically - Read the audio file and pass its content
        with open(audio_file_path, "rb") as audio_file:
            audio_data = audio_file.read()
        st.audio(audio_data, format='audio/mp3', start_time=0)

        # Optionally, delete the audio file after playing
        # os.remove(audio_file_path)

if __name__ == "__main__":
    main()
