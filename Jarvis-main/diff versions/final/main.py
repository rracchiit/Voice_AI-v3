import speech_recognition as sr
import pyttsx3
from langdetect import detect, LangDetectException
from googletrans import Translator, LANGUAGES

r = sr.Recognizer()
translator = Translator()  # Removed service_urls for simplicity
tts = pyttsx3.init()

while True:
    with sr.Microphone() as source:
        print("Speak Something...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio)
        print(f"Recognized Text: {text}")
        
        input_language = detect(text)
        print(f"Detected Language: {input_language}")
        
        if input_language == "hi":
            translation = translator.translate(text, dest='en')
            print(f"Translated to English: {translation.text}")
            tts.say(translation.text)
            tts.runAndWait()
        elif input_language == "en":
            translation = translator.translate(text, dest='hi')
            print(f"Translated to Hindi: {translation.text}")
            tts.say(translation.text)
            tts.runAndWait()
        else:
            print("Unsupported language")
    
    except sr.UnknownValueError:
        print("Sorry, I didn't understand")
    except LangDetectException:
        print("Language detection failed")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
