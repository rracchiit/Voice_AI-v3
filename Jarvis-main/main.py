import speech_recognition as sr
import pyttsx3
from langdetect import detect
from googletrans import Translator

r = sr.Recognizer()
translator = Translator(service_urls=['translate.google.com'])
tts = pyttsx3.init()

while True:
    with sr.Microphone() as source:
        print("Speak Something...")
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
    try:
        text = r.recognize_google(audio)
        input_language = detect(text)

        if input_language =="hi":
            translation = translator.translate(text, det='en')
            print(f"Translated to English:{translation.text}")

            tts.say(translation.text)
            tts.runAndWait
        elif input_language == "en":
            print(f"Translated to Hindi: {translation.text}")
            tts.say(translation.text)
            tts.runAndWait()
        else:
            print("Unsupported language")
    except sr.UnknownValueError:
        print("Sorry, i didnt understand")
