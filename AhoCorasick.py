import collections


def build(patterns):
    trie = {}
    statepattern = {}
    statein = 1
    for pattern in patterns:
        point = trie
        stateout = 0
        for char in pattern:
            if stateout not in point:
                point[stateout] = {char: statein}
                stateout = statein
                statein += 1
            elif char not in point[stateout]:
                point[stateout][char] = statein
                stateout = statein
                statein += 1
            else:
                stateout = point[stateout][char]
        statepattern[stateout] = len(pattern)
    queue = collections.deque([0])
    statwfail = []
    while queue:
        i = queue.popleft()
        statwfail.append(i)
        if i in list(point.keys()):
            listofvalues = list(point[i].values())
            for j in listofvalues:
                queue.append(j)
        if i == 0:
            point[0]['fail'] = 0
        else:
            for status in statwfail:
                if i in list(point[status].values()):
                    for key, val in list(point[status].items()):
                        if val == i:
                            break
                    label = key
                    parent = status
                    if parent == 0:
                        if i in list(point.keys()):
                            point[i]['fail'] = 0
                        else:
                            point[i] = {'fail': 0}
                        break
                    else:
                        while True:
                            status = point[status]['fail']
                            if label in list(point[status].keys()):
                                if i in list(point.keys()):
                                    point[i]['fail'] = point[status][label]
                                else:
                                    point[i] = {'fail': point[status][label]}
                                break
                            elif status == 0:
                                if i in list(point.keys()):
                                    point[i]['fail'] = 0
                                else:
                                    point[i] = {'fail': 0}
                                break
                        break
    return trie, statepattern


def search(aut, text):
    trie = aut[0]
    statepattern = aut[1]
    stateout = 0
    result = []
    for i in range(len(text)):
        while True:
            if text[i] in trie[stateout]:
                stateout = trie[stateout][text[i]]
                break
            else:
                stateout = trie[stateout]['fail']
                if stateout == 0 and text[i] not in trie[stateout]:
                    break
        if stateout in statepattern.keys():
            result.append(i-statepattern[stateout]+1)
    return result


myaut = build(("a", "ab", "abc"))
# myaut = build(("abc", "aab", "cba"))
print(search(myaut, 'abcab'))
