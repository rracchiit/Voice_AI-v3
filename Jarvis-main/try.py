from openai import OpenAI
import speech_recognition as sr
import pyttsx3
import time

# Initialize OpenAI client
client = OpenAI(api_key="meow")

def openAI(user_prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"API Error: {e}")  # Print the real issue
        return "Sorry, something went wrong."


def speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening carefully...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio, language="en-in").lower()
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Speech can't be recognized")
        return ''
    except sr.RequestError:
        print("Error, can't connect to Google services")
        return ''

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello sir, how may I assist you today")    

    while True:
        user_input = speech()
        
        if any(keyword in user_input for keyword in ["exit", "bye", "close"]):
            speak("Goodbye")    
            break
        
        if user_input:
            gpt_response = openAI(user_input)
            speak(gpt_response)
