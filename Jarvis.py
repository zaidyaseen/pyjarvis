import datetime
import wikipedia
import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")

    else:
        speak("good evening")

    speak("I am javis how can I help you.")
def takeCommand():
    ''' it takes microphone for the user and returns the string output'''
    r  = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Reconizing...")
        qurey = r.recognize_google(audio, language="en-us")
        print(f"User said: {qurey}\n")
    except Exception as e:
        print("say that again please...")
        return "none"
    return qurey


if __name__ == '__main__':
    wishMe()
    while True:
        qurey = takeCommand().lower()

        # Logic for executing tasks based on qurey
        if 'wikipedia' in qurey:
            speak('Searching Wikipedia...')
            query = qurey.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in qurey:
            webbrowser.open('youtube.com')

        elif 'google' in qurey:
            webbrowser.open('google.com')    

        elif 'learn' in qurey:
            webbrowser.open('w3schools.com')   

        elif 'play music' in qurey:
            music_dir = 'C:\\Users\\zaidy\\Desktop\\jarvis'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[2]))
        elif 'time' in qurey:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(strTime)
        elif 'code' in qurey:
            Codepath = "C:\\Users\\zaidy\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(Codepath)


        elif 'my name' in qurey:
            webbrowser.open("https://archive.org/details/QuranMajeed15LinesSaudiPrint/page/n597/mode/2up")

        elif 'what is your name' in qurey:
            speak('My name is jarvis') 

        elif 'zoom' in qurey:
            zoompath = 'C:\\Users\\zaidy\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe'
            os.startfile(zoompath)


