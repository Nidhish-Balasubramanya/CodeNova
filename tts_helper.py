import requests
import os
import json
import streamlit as st
from gtts import gTTS
from config import get_access_token  
from google.cloud import texttospeech

# Load credentials from Streamlit secrets
creds_json = st.secrets["GOOGLE_APPLICATION_CREDENTIALS_JSON"]
creds_dict = json.loads(creds_json)

# Save to a temporary file
temp_path = "/tmp/gcp_credentials2.json"
with open(temp_path, "w") as f:
    json.dump(creds_dict, f)

# Set environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = temp_path


access_token = get_access_token()

url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token}"
}

# Function to detect programming language
def detect_language(code):
    keywords = {
        "python": ["def ", "self", "lambda"],
        "java": ["public class", "System.out.println(", "import java."],
        "c": ["printf(", "scanf("],
        "cpp": ["std::cout", "std::cin", "using namespace std;", "cout", "cin"],
        "r": ["<-", "library(", "ggplot("],
        "javascript": ["console.log(", "function(", "var ", "let ", "const "]
    }

    for lang, signs in keywords.items():
        if any(sign in code for sign in signs):
            return lang.capitalize()

    return "Unknown"

# Function to get AI-generated explanation
def get_code_explanation(code, language):
    body = {
        "input": f"Generate an script for a person to explain the following {language} code. always start with an 'Hello!'. The code is as Follows {code} ",
        "parameters": {"decoding_method": "greedy", "max_new_tokens": 4000},
        "model_id": "ibm/granite-20b-code-instruct",
        "project_id": "33f5277e-ac20-4539-81fd-0ab8217c908f"
    }

    try:
        response = requests.post(url, headers=headers, json=body)
        if response.status_code == 200:
            response_data = response.json()
            explanation = response_data.get("results", [{}])[0].get("generated_text", "No explanation generated.")
            return explanation.replace("`", "")
        else:
            return f"Error: {response.text}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"

# Function to convert text to speech
'''
def text_to_speech_gtts(text):
    # folder path
    folder_path="tts_outputs"

    # Generate the audio file
    tts = gTTS(text=text, lang='en')
    audio_file = os.path.join(folder_path, "explanation.mp3")
    tts.save(audio_file)
    return audio_file

def text_to_speech_google(text):
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    name="en-US-Chirp-HD-F",  
    ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    audio_file = "explanation.mp3"
    with open(audio_file, "wb") as out:
        out.write(response.audio_content)

    return audio_file
'''

def text_to_speech_google(text):
    save_directory = "tts_outputs"  # Specify the desired folder
    filename = "explanation.mp3"  # Fixed filename

    # Ensure the directory exists
    os.makedirs(save_directory, exist_ok=True)

    # Define the full path
    audio_file_path = os.path.join(save_directory, filename)

    try:
        client = texttospeech.TextToSpeechClient()
        synthesis_input = texttospeech.SynthesisInput(text=text)

        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name="en-US-Chirp-HD-F",
            ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
        )

        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        response = client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        # Save the file to the specified directory
        with open(audio_file_path, "wb") as out:
            out.write(response.audio_content)

        return audio_file_path
    except Exception as e:
        print(f"Error in text_to_speech_google: {e}")
        return None
