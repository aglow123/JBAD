def token_generator(filename, filetype):
    if filetype == 'txt':
        with open(filename, 'r', encoding='UTF-8') as file:
            for line in file:
                words = line.split()  # dzieli po ciagu bialych znakow
                for word in words:
                    yield word
    elif filetype == 'conll':
        with open(filename) as file:
            for line in file:
                words = line.split()  # dzieli po ciagu bialych znakow
                try:
                    yield words[0][1:-1]
                except IndexError:
                    pass  # świadomi odpowiedzialności karnej except może być pusty


def sentence_generator(filename, filetype):
    sentence = []
    for token in token_generator(filename, filetype):
        sentence += [token]
        if token in ".!?":
            yield sentence
            sentence = []


for sentence in sentence_generator("potop.txt", "txt"):
    print(sentence)

for sentence in sentence_generator("nkjp.txt", "txt"):
    print(sentence)

for sentence in sentence_generator("nkjp.conll", "conll"):
    print(sentence)

