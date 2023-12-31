from gpt4v import GPT4Vision

def main():
    # Initialize the GPT4Vision client
    vision_client = GPT4Vision()

    # Specify the path to your image
    image_path = "2.png"  # Replace with the path to your image

    # Specify the user message
    user_message = "What does this image depict?"  # Replace with your desired message

    # Get the description of the image
    description = vision_client.describe(image_path, user_message)
    print(description)

if __name__ == "__main__":
    main()
