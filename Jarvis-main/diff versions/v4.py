import speech_recognition as sr
import pyttsx3
from googletrans import Translator, LANGUAGES

# Initialize the recognizer, translator, and TTS engine
recognizer = sr.Recognizer()
translator = Translator()
tts_engine = pyttsx3.init()

# Get user input for the target language
languagev2 = input("Enter 'fr' for [French] or 'es' for [Spanish]: ")

if languagev2 not in ['fr', 'es']:
    print("Invalid input. Please restart and choose either 'fr' for French or 'es' for Spanish.")
else:
    # Function to handle translation and text-to-speech
    def translate_and_speak(text, target_language):
        try:
            # Translate text to the desired language
            translation = translator.translate(text, dest=target_language)
            translated_text = translation.text
            print(f"Translated to {LANGUAGES[target_language]}: {translated_text}")
            
            # Use text-to-speech to speak the translated text
            tts_engine.say(translated_text)
            tts_engine.runAndWait()
            
        except Exception as e:
            print(f"Error: {e}")

    # Main loop to continuously listen and translate
    while True:
        with sr.Microphone() as source:
            print("Listening for speech...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            
            try:
                # Recognize the speech using Google Web Speech API
                recognized_text = recognizer.recognize_google(audio)
                print(f"Recognized: {recognized_text}")

                # Check for exact exit commands (only the single words "exit", "close", "bye", "quit")
                exit_commands = ['exit', 'close', 'bye', 'quit']
                if recognized_text.lower().strip() in exit_commands:
                    print("Exit command detected. Exiting...")
                    tts_engine.say("Goodbye!")
                    tts_engine.runAndWait()
                    break

                # Translate and speak in the chosen language
                translate_and_speak(recognized_text, languagev2)
                
            except sr.UnknownValueError:
                print("Sorry, I did not understand the audio.")
            except sr.RequestError as e:
                print(f"Request error: {e}")
            except Exception as e:
                print(f"Error: {e}")
