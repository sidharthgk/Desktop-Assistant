import speech_recognition as sr
import pyttsx3
import webbrowser

# it converts text provided to speech and speaks it out for the user
def speak(text):
    print(text)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 110)
    engine.say(text)
    engine.runAndWait()

# it takes in users command in audio and converts it to text
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
        except sr.UnknownValueError: # this error occurs when its not able to identify words
            print("Sorry, I didn't catch that. Could you please repeat?")
            return takeCommand()  # Retry if speech is not understood
        except sr.RequestError as e: # when its not able to reach google servers
            print("Could not request results; {0}".format(e))
            return takeCommand()

# this is used to execute basic queries 
def execute(query):
    if query == "stop": # the program ends if user says stop
        exit()
    # dictionary is used to open different sites
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
        if query.lower() == "hey jarvis":
            execute(query)
        else:
            print("waiting")

def greet() :
    exit() # add greetings based on time here
