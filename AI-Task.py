import speech_recognition as sr
import pyttsx3
import datetime
import os
import time
import subprocess
import requests


Name="Friday"


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()


def tellme():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<10:
        speak("Good morining, you have Marketing Paper due at 11:59 PM")
    elif hour>=10 and hour<13:
        speak("Good Afternoon, you have python 2 module 2 assigment due tomorrow at 11:30 PM")
    elif hour>=13 and hour<17:
        speak("Good Evening, you have Dicussion about \"Do you believe that social media is stimulating or inhibiting critacal thinking" "due in wednesday")
    elif hour>=17 and hour<22:
        speak("that is all the reminders of the upcoming assigments you have for today")
    else:
        speak("Hello, you have no assigments due today")

def Command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

    try: 
        statement=r.recognize_google(audio,language='en-in')
        print(f"user said:{statement}\n")

    except:
        speak("Pardon me, I didn't quite catch that")
        return "None"

    return statement

speak("Loading your AI personal assistant Friday")
tellme()

if __name__=='__main__':

   while True:
        speak("How can I help you now?")
        statement = Command().lower()
        if statement == 0:
            continue

        elif "bye Friday" in statement or "Goodbye Friday" in statement or "Stop Friday" in statement:
            speak('your personal assistant Friday is shutting down, have a good day')

        elif statement == "":
            speak("yes? I am waiting.....")

        else:
            speak("Sorry, I didn't quite catch that")

        break
