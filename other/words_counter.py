from collections import defaultdict


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


def words_counter(txtfile, lenofranking):
    counter = defaultdict(lambda: 0)
    for word in words_generator(txtfile):
        counter[word] += 1

    ranking = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    while lenofranking < len(ranking) and ranking[lenofranking][1] == ranking[lenofranking-1][1]:
        lenofranking += 1
    return ranking[:lenofranking]


for item in words_counter("potop.txt", 10):
    print(item)
