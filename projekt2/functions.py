import warnings

import wikipedia as wikipedia

from mic.stt import listen
from mic.tts import speak
from datamuse import Datamuse
import re

warnings.catch_warnings()
warnings.simplefilter('ignore')


def synonyms():
    user_word = listen()
    api = Datamuse()
    words = api.words(rel_syn=user_word, max=5)
    if not words:
        result = 'Sorry, synonyms for word: \'{}\', not found.'.format(user_word)
    elif len(words) == 1:
        result = 'Synonym for word: \'{}\', is: '.format(user_word) + ''.join(get_words(words))
    else:
        result = 'Synonyms for \'{}\' are: '.format(user_word) + ''.join(get_words(words))
    print(result)
    speak(result)


def antonyms():
    user_word = listen()
    api = Datamuse()
    words = api.words(rel_ant=user_word, max=5)
    if not words:
        result = 'Sorry, antonyms for word: \'{}\', not found.'.format(user_word)
    elif len(words) == 1:
        result = 'Antonym for word: \'{}\', is: '.format(user_word) + ''.join(get_words(words))
    else:
        result = 'Antonyms for \'{}\' are: '.format(user_word) + ''.join(get_words(words))
    print(result)
    speak(result)


def definitions():
    user_word = listen()
    result = 'Definition for \'{}\' is: \n'.format(user_word) + get_definition(user_word)
    print(result)
    speak(result)


def rhymes():
    user_word = listen()
    api = Datamuse()
    words = api.words(rel_rhy=user_word, max=5)
    if not words:
        result = 'Sorry, rhymes for word: \'{}\', not found.'.format(user_word)
    elif len(words) == 1:
        result = 'Rhyme for word: \'{}\', is: '.format(user_word) + ''.join(get_words(words))
    else:
        result = 'Rhymes for \'{}\' are: '.format(user_word) + ''.join(get_words(words))
    print(result)
    speak(result)


def homophones():
    user_word = listen()
    api = Datamuse()
    words = api.words(rel_hom=user_word, max=5)
    if not words:
        result = 'Sorry, homophones for word: \'{}\', not found.'.format(user_word)
    elif len(words) == 1:
        result = 'Homophone for word: \'{}\', is: '.format(user_word) + ''.join(get_words(words))
    else:
        result = 'Homophones for word: \'{}\', are: '.format(user_word) + ''.join(get_words(words))
    print(result)
    speak(result)


def get_words(words):
    result = []
    for item in words:
        if item == words[-1]:
            result.append(item.get("word"))
        else:
            result.append(item.get("word") + ', ')
    return result


def get_definition(term_to_find: str):
    word = wikipedia.search(term_to_find)[0]
    try:
        summary = wikipedia.summary(word, auto_suggest=False, redirect=True)
    except wikipedia.DisambiguationError as e:
        try:
            summary = wikipedia.summary(e.options[0], auto_suggest=False)
        except wikipedia.DisambiguationError as e:
            summary = wikipedia.summary(e.options[0], auto_suggest=True)
    if len(summary.split(". ")[0]) > 2:
        return re.sub(r"\(.+?\)", '', ". \n".join(summary.split(". ")[:2]))
    else:
        return re.sub(r"\(.+?\)", '', ". \n".join(summary.split(". ")))
