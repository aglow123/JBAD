from functions import antonyms, definitions, homophones, rhymes, synonyms
from mic.tts import speak


def show_menu(options):
    options = list(options.items())
    for num, option in enumerate(options, start=0):
        print("{}. {}".format(num, option[0]))
    correct_choices = range(0, len(options))
    while True:
        try:
            speak("What do you want to do?")
            choice = int(input("Input the selected number >> "))
            assert choice in correct_choices
        except (ValueError, AssertionError):
            pass
        else:
            func, args, kwargs = options[choice][1]
            return func(*args, **kwargs)


start_menu = {
    "quit": (exit, (1,), {}),
    "synonyms": (synonyms, (), {}),
    "antonyms": (antonyms, (), {}),
    "definitions": (definitions, (), {}),
    "rhymes": (rhymes, (), {}),
    "homophones": (homophones, (), {})
}

if __name__ == '__main__':
    while True:
        show_menu(start_menu)
