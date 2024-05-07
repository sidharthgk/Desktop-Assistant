import pyttsx3
import speech_recognition 
import pywhatkit

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
    return query

def musicplay():
    speak("Which song would you like to play?")
    try:
        song = takeCommand()
        pywhatkit.playonyt(song)
        speak("Playing" + song)
    except Exception as e:
        print("Error:", str(e))
        speak("Sorry, there was an error playing the song.")