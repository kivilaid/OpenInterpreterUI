from pathlib import Path
from openai import OpenAI

class GPTTTS:
    def __init__(self, client):
        self.client = client

    def generate_speech(self, text="No text", model="tts-1-hd", voice="alloy"):
        """
        Generate speech from text using OpenAI's text-to-speech API.

        :param text: The text to convert to speech. Defaults to "No text".
        :param model: The TTS model to use. Defaults to "tts-1-hd".
        :param voice: The voice to use. Defaults to "alloy".
        :return: Path to the generated speech file.
        """
        # Set default values if parameters are empty
        model = model if model else "tts-1-hd"
        voice = voice if voice else "alloy"

        # Create the speech file path
        speech_file_path = Path(__file__).parent / "speech.mp3"

        # Generate the speech
        response = self.client.audio.speech.create(
            model=model,
            voice=voice,
            input=text
        )

        # Save the speech to a file
        response.stream_to_file(speech_file_path)

        return speech_file_path

# Example usage
if __name__ == "__main__":
    client = OpenAI()  # Initialize the OpenAI client
    tts = GPTTTS(client)

    # Generate speech
    file_path = tts.generate_speech(
        text="Today is a wonderful day to build something people love!",
        model="tts-1-hd",
        voice="alloy"
    )
    print(f"Speech generated at: {file_path}")
