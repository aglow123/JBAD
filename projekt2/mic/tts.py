import pyttsx3 as tts


def speak(sentence):
    engine = tts.init()
    engine.setProperty('volume', 0.7)
    engine.setProperty('rate', 130)
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[2].id)
    engine.say(sentence)
    engine.runAndWait()
