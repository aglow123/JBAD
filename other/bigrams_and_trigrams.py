from collections import defaultdict, deque


def words_generator(txtfile):
    with open(txtfile, 'r', encoding='UTF-8') as file:
        for line in file:
            if line:    #ignore blank lines
                tokens = line.split()  # list of tokens in line sepatared by any whitespace
                for token in tokens:
                    if token not in '.,,?!-;:()"':      #ignore symbols
                        word = ""
                        for char in token:
                            if char not in '.,,?!-;:()"':
                                word += char
                        yield word.lower()       #yield lowercased word - token without punctuation


def bigrams_generator(txtfile):
    temp = ''
    for i, word in enumerate(words_generator(txtfile)):
        if i==0:
            temp = word
        else:
            yield temp, word
            temp = word


def trigrams_generator(txtfile):
    temp1 = ''
    temp2 = ''
    for i, word in enumerate(words_generator(txtfile)):
        if i == 0:
            temp1 = word
        elif i == 1:
            temp2 = word
        else:
            yield temp1, temp2, word
            temp1 = temp2
            temp2 = word


def words_counter(txtfile, lenofranking):
    counter = defaultdict(lambda: 0)
    for word in words_generator(txtfile):
        counter[word] += 1

    ranking = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    while True:
        if ranking[lenofranking][1] == ranking[lenofranking-1][1]:
            lenofranking += 1
        else:
            break
    return ranking[:lenofranking]


def bigrams_counter(txtfile, lenofranking):
    counter = defaultdict(lambda: 0)
    for bigram in bigrams_generator(txtfile):
        counter[bigram] += 1

    ranking = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    while True:
        if lenofranking >= len(ranking):
            break
        if ranking[lenofranking][1] == ranking[lenofranking - 1][1]:
            lenofranking += 1
        else:
            break
    return ranking[:lenofranking]


def trigrams_counter(txtfile, lenofranking):
    counter = defaultdict(lambda: 0)
    for trigram in trigrams_generator(txtfile):
        counter[trigram] += 1

    ranking = sorted(counter.items(), key=lambda x: x[1], reverse=True)     #key = itemgetter(1) from operator import
    while True:
        if lenofranking >= len(ranking):
            break
        if ranking[lenofranking][1] == ranking[lenofranking - 1][1]:
            lenofranking += 1
        else:
            break
    return ranking[:lenofranking]


def gen_ngram(tokens, n=2):
    ngram = deque()
    for token in tokens:
        ngram.append(token)
        if len(ngram) == n:
            yield tuple(ngram)
            ngram.popleft()


# for words in bigrams_generator('nkjp.txt'):
#     print(words)
print(trigrams_counter('potop.txt', 10))
