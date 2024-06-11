from flask import Flask, render_template, request, send_file, redirect, url_for
from google.cloud import texttospeech
from dotenv import load_dotenv
import os
import PyPDF2
import google.cloud.texttospeech_v1 as texttospeech_v1

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Access the environment variable
credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
client = texttospeech.TextToSpeechClient.from_service_account_file(credentials_path)

# List of available voices
voices = client.list_voices().voices

@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    if request.method == 'POST':
        # Handle PDF file upload
        pdf_file = request.files['pdf_file']
        if pdf_file:
            voice_name = request.form['voice']
            convert_pdf(pdf_file, voice_name)
            message = "Conversion finished successfully!"
        else:
            message = "Please select a PDF file."
    else:
        message = "Audio file not found - please convert a pdf first"
    return render_template('index.html', voices=voices, message=message)
    

@app.route('/play', methods=['GET'])
def play_audio():
    try:
        return send_file('output.mp3', mimetype='audio/mpeg')
    except FileNotFoundError:
        message = "Audio file not found - please convert a pdf first"
        return redirect(url_for('index'))
    
@app.route('/download', methods=['GET'])
def download_audio():
    try:
        return send_file('output.mp3', as_attachment=True)
    except FileNotFoundError:
        message = "Audio file not found - please convert a pdf first"
        return redirect(url_for('index'))
    
def convert_pdf(pdf_file, voice_name):
    # Extract text from PDF
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()

    # Convert text to speech
    input_text = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code=voice_name[:5],
        name=voice_name
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16,
        speaking_rate=1
    )

    # Create the SynthesizeSpeechRequest object
    synthesis_request = texttospeech_v1.SynthesizeSpeechRequest(
        input=input_text,
        voice=voice,
        audio_config=audio_config
    )

    # Perform the text-to-speech request
    response = client.synthesize_speech(request=synthesis_request)

    # Save the synthesized audio to a file
    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

if __name__ == '__main__':
    app.run(debug=True)