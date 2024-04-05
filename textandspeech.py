import pyttsx3
import os
from gtts import gTTS
import speech_recognition as sr


def home_page():
    print("""
    Welcome!
    Convert your speech to text or text to speech.

    1. Speech to Text
    2. Text to Speech
    """)
    option = int(input('Select (1/2) for your choice of conversion: '))
    if option == 1:
        speech_to_text()
    elif option == 2:
        text_to_speech()
    else:
        print('Invalid option! Please select 1 or 2.')


def text_to_speech():
    text=input("entre the text to read: ").strip()
    if text:
        try:
            language = input("Enter the language code (e.g., 'en' for English): ")
            tts = gTTS(text=text, lang=language, slow=False)
            filename = "output.mp3"
            tts.save(filename)
            print("Text converted to speech successfully!")
            os.system("start output.mp3")  # Play the generated audio file
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    else:
        print('invalid entry!!!')

def speech_to_text():
#   just for voice to text
    recognizer= sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print('listening speak now! ')
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
        
            audio=recognizer.listen(source)
            recognize_text=recognizer.recognize_google(audio)
            print('you said', recognize_text)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
while True:
    home_page()