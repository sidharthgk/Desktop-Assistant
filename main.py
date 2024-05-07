import tkinter as tk
from PIL import Image, ImageTk
import pyttsx3
import speech_recognition 
import requests
from bs4 import BeautifulSoup
import datetime
import os
import openai


# Initialize the text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print(audio)

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def alarm(query):
    timehere = open("Alarmtext.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

def start_assistant():
    speak("Initializing assistant...")
    while True:
        query = takeCommand().lower()
        if "hey jarvis" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Okay goodbye")
                    break 
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                    if "close" in query:
                        from Dictapp import closeappweb
                        closeappweb(query)
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                elif "temperature" in query or "weather" in query:
                    location = "kottayam"  # You can replace "Kerala" with the location extracted from the user's query
                    search = f"temperature in {location}"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    try:
                        temperature_element = data.find("div", class_="BNeawe iBp4i AP7Wnd").text
                        temperature = temperature_element.split('°')[0] + 'degrees'
                        speak(f"Current temperature in {location} is {temperature}")
                    except AttributeError:
                        speak(f"Sorry, I couldn't find the temperature for {location}.")
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"The current time is {strTime}")
                elif "jarvis sleep" == query:
                    speak("Going to sleep")
                    exit()
                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that", "")
                    rememberMessage = query.replace("jarvis", "")
                    speak("You told me to " + rememberMessage)
                    remember = open("Remember.txt", "a")
                    remember.truncate(0)
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt", "r")
                    speak("You told me to " + remember.read())
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()
                elif "music" in query or "song" in query:
                    from Playmusic import musicplay
                    musicplay()
                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()

def create_gui():
    root = tk.Tk()
    root.title("Jarvis Desktop Assistant")

    # Set background color to light purple
    root.configure(bg="#e6e6fa")

    # Load GIF image for the bot
    img = Image.open("bot.png")
    img = img.resize((300, 300))
    img = ImageTk.PhotoImage(img)

    # Add Label to display the GIF
    image_label = tk.Label(root, image=img, bg="#e6e6fa")
    image_label.image = img  # Keep a reference to the image
    image_label.pack(pady=20)

    # Add Speak Button with dark purple color
    speak_button = tk.Button(root, text="Speak", font=("Helvetica", 14, "bold"), command=start_assistant, bg="#89CFF0", fg="white", padx=20, pady=10)
    speak_button.pack(padx=20, pady=(0, 20))

   

    root.mainloop()

if __name__ == "__main__":
    create_gui()
