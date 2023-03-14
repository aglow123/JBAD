import speech_recognition as sr
import time
from mic.tts import speak


def listen():
    r = sr.Recognizer()
    while True:
        time.sleep(1)
        print("Say the word")
        speak("say the word")
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                tekst = r.recognize_google(audio, language='en_EN')
                return tekst
            except sr.UnknownValueError:
                print('Try again')
                speak('try again')
            except sr.RequestError as e:
                print('Error:', e)
                speak('error')
