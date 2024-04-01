import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit
import datetime

def speak(text):
    print(text)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 130)
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.7
        print("Listening...")
        try:
            audio = r.listen(source)
            print("Recognizing...")
            query = r.recognize_google(audio)
            print("User said:", query)
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Could you please repeat?")
            return takeCommand()
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return takeCommand()

def execute(query):
    if query == "stop":
        exit()

    sites = {"google": "www.google.com", "youtube": "www.youtube.com", "wikipedia": "www.wikipedia.com",
             "instagram": "www.instagram.com", "twitter": "www.twitter.com", "linkedin": "www.linkedin.com"}
    for site, url in sites.items():
        if f"open {site}" in query:
            speak(f"Opening {site}")
            webbrowser.open(url)
            break

    commands = {"hello": "hi how can i help you today",
                "how are you": "I'm just a desktop assistant but thanks for asking",
                "who created you": "I was created by Sid, Sruthy, Viswam, and Sreehari"}
    for cmd, ans in commands.items():
        if f"{cmd}" == query:
            speak(f"{ans}")
            break

def playMusic():
    speak("Which song would you like to play?")
    try:
        song = takeCommand()
        pywhatkit.playonyt(song)
        speak("Playing" + song)
    except Exception as e:
        print("Error:", str(e))
        speak("Sorry, there was an error playing the song.")


def greet():
    current_time = datetime.datetime.now()
    if 6 <= current_time.hour < 12:
        speak("Good morning!")
    elif 12 <= current_time.hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

if __name__ == '__main__':
    greet()
    speak("Hello, I'm JARVIS A.I. How can I help you?")
    while True:
        query = takeCommand()
        execute(query)
        if query == "play song":
            playMusic()
