import base64
from openai import OpenAI

class GPT4Vision:
    def __init__(self):
        self.client = OpenAI()

    def encode_image(self, image_file):
        """
        Encode the image to base64 format.

        :param image_file: File object of the image.
        :return: Base64 encoded string of the image.
        """
        return base64.b64encode(image_file.read()).decode('utf-8')

    def describe(self, image_file, user_message):
        """
        Get a description of the image using OpenAI's GPT-4 Vision API.

        :param image_file: File object of the image.
        :param user_message: Custom text message to send as user input.
        :return: The API response.
        """
        base64_image = self.encode_image(image_file)

        response = self.client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": user_message},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{base64_image}"
                            },
                        },
                    ],
                }
            ],
            max_tokens=1000,
        )
        return response.choices[0].message.content

# # Example usage
# gpt4v = GPT4Vision()
# image_path = "/path/to/image.png"
# with open(image_path, "rb") as image_file:
#     user_message = "Describe this image for me."
#     description = gpt4v.describe(image_file, user_message)
#     print(description)
