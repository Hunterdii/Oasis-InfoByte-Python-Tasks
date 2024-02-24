import pyttsx3
import speech_recognition as sr
import pyautogui
import time
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

email_dict = {"friend": "friend@example.com", "family": "family@example.com"}  

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    assistant_name = "Hunterdii"
    speak(f"I am {assistant_name}. Please tell me how may I help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enter your email
    server.login('jestonpatel9879@gmail.com', 'codesownway0707')
    server.sendmail('jasonhunts0707@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_url = "https://music.youtube.com/playlist?list=PLIL965-SXjbVEiWwe1l6RApWYDnbhc_Oz&si=g69JUw7JlEO2s0k2"
            webbrowser.open(music_url)
            time.sleep(5)
            pyautogui.press('space')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir , the current time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\hetpa\\OneDrive\\Desktop\\Python Programs\\server.py"
            os.startfile(codepath)

        elif 'search google for' in query:
            search_query = query.replace('search google for', '')
            webbrowser.open(f"https://www.google.com/search?q={search_query}")

        elif 'search youtube for' in query:
            search_query = query.replace('search youtube for', '')
            webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")

        elif 'search in hindi for' in query:
            search_query = query.replace('search in hindi for', '')
            search_query = search_query.encode('utf-8')
            webbrowser.open(f"https://www.google.com/search?hl=hi&q={search_query}")

        elif 'search in gujarati for' in query:
            search_query = query.replace('search in gujarati for', '')
            search_query = search_query.encode('utf-8')
            webbrowser.open(f"https://www.google.com/search?hl=gu&q={search_query}")

        elif 'send email to' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                speak("Who should I send it to? ")
                recipient = takecommand().lower()
                to = email_dict[recipient]
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email.")

        elif 'open notepad' in query:
            os.system("start notepad.exe")

        elif 'open calculator' in query:
            os.system("start calc.exe")

        elif 'open command prompt' in query:
            os.system("start cmd.exe")

        # elif 'play a game' in query:
        #     game_path = "C:\\Games\\game.exe"  
        #     os.startfile(game_path)

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

