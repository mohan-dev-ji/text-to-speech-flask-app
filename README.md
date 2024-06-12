Text-to-Speech App
This is a Flask web application that allows users to convert PDF files to speech using the Google Text-to-Speech API. The application provides a user-friendly interface for selecting a PDF file, choosing a voice, and converting the text to speech.

Features
Upload PDF files
Select from a list of available voices
Convert PDF text to speech
Play the synthesized audio
Download the synthesized audio as an MP3 file

Prerequisites
Python 3.x
pip (Python package installer)
Installation
Clone the repository:
git clone https://github.com/mohan-dev-ji/text-to-speech-flask-app

Navigate to the project directory:
cd text-to-speech-app

Create and activate a virtual environment (optional but recommended):
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`

Install the required packages:
pip install -r requirements.txt

Set up the Google Text-to-Speech API credentials by following the instructions in the Google Cloud Documentation.
Start the Flask development server:
python app.py

The application should now be running at http://localhost:5000.
Usage
Open the application in your web browser at http://localhost:5000.
Click the "Choose File" button to select a PDF file from your local machine.
Select a voice from the dropdown menu.
Click the "Convert" button to convert the PDF text to speech.
Once the conversion is complete, you can click the "Play" button to play the synthesized audio or the "Download" button to download the audio as an MP3 file.

Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
License
This project is licensed under the MIT License.

Acknowledgments
Flask - The web framework used
PyPDF2 - For PDF text extraction
Google Text-to-Speech API - For text-to-speech conversion