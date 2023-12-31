#import streamlit as st
import base64
from openai import OpenAI


client = OpenAI()

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "2.png"

# Getting the base64 string
base64_image = encode_image(image_path)


response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/png;base64,{base64_image}"
            },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response)