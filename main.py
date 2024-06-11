"""Synthesizes speech from the input string of text."""
from google.cloud import texttospeech
from dotenv import load_dotenv
import os
import PyPDF2

# Load environment variables from .env file
load_dotenv()

# Open the PDF file in read-binary mode
with open('file.pdf', 'rb') as file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(file)

    # Get the number of pages in the PDF
    num_pages = len(pdf_reader.pages)

    # Initialize an empty string to store the text
    text = ''

    # Iterate over each page and extract the text
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()


# Access the environment variable
credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

client = texttospeech.TextToSpeechClient()

# text = input("What do you want to say? ")

input_text = texttospeech.SynthesisInput(text=text)

# Note: the voice can also be specified by name.
# Names of voices can be retrieved with client.list_voices().
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    name="en-US-Studio-M",
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.LINEAR16,
    speaking_rate=1
)

response = client.synthesize_speech(
    request={"input": input_text, "voice": voice, "audio_config": audio_config}
)

# The response's audio_content is binary.
with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')