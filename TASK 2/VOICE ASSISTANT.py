import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

engine = pyttsx3.init()
engine.setProperty('rate', 150)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = listener.listen(source)
        try:
            command = listener.recognize_google(audio)
            command = command.lower()
            print(f"👂 You said: {command}")
        except sr.UnknownValueError:
            talk("Sorry, I didn't catch that.")
            return ""
    return command

def run_assistant():
    command = take_command()
    
    if 'play' in command:
        song = command.replace('play', '')
        talk(f'Playing {song}')
        pywhatkit.playonyt(song)
        
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f'Current time is {time}')
        
    elif 'hello' in command:
        talk('Hello there! How can I help you today?')
        
    elif 'stop' in command:
        talk('Goodbye!')
        exit()
        
    else:
        talk("I can’t do that yet, but I’m learning!")

while True:
    run_assistant()
