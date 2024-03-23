import speech_recognition as sr
import pyttsx3
import webbrowser

def speak(text):
    print(text)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 110)
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.7
        print("Listening...")
        try:
            audio = r.listen(source)  # could add timeout
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print("User said:", query)
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Could you please repeat?")
            return takeCommand()  # Retry if speech is not understood
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return "Audio not clear"

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
    else:
        speak("I'm sorry, I don't understand that command.")

if __name__ == '__main__':
    speak("Hello, I'm JARVIS A.I. How can I help you?")
    while True:
        query = takeCommand()
        execute(query)
