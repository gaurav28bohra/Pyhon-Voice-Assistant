import pyaudio
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try :
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except UnknownValueError as e:
            print("OOPSS!! Didn't catch that.")
def speechtx(x) :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',160)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__' :
    if sptext().lower() == "hey peter" :
        while True :
            data1 = sptext().lower()
            if "your name" in data1 :
                name = "my name is peter"
                speechtx(name)
            elif "old are you" in data1 :
                age = "my age is 22"
                speechtx(age) 
            elif "time" in data1 :
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtx(time)
            elif "youtube" in data1 :
                webbrowser.open("https://www.youtube.com")
            elif "exit" in data1 :
                 bye = "Thank you"
                 speechtx(bye)
                 break
            #time.sleep(5)

    else :
        print("thanks")