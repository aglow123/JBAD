from collections import defaultdict, deque


class AhoCorasick:
    def __init__(self, patterns):
        self.patterns = patterns
        self.trie, self.statepattern = self.build()

    def __repr__(self):
        return repr(self.trie)

    def build(self):
        trie = {}
        statepattern = defaultdict(list)   #state where pattern ends and its length
        statein = 1
        for pattern in self.patterns:
            point = trie
            stateout = 0
            lens, inds = self.substring(pattern)
            for i in range(len(pattern)):
                if stateout not in point:
                    point[stateout] = {pattern[i]: statein}
                    stateout = statein
                    statein += 1
                elif pattern[i] not in point[stateout]:
                    point[stateout][pattern[i]] = statein
                    stateout = statein
                    statein += 1
                else:
                    stateout = point[stateout][pattern[i]]
                if i in inds:
                    for e in range(len(inds)):
                        if inds[e] == i:
                            len_e = lens[e]
                            if len_e not in statepattern[stateout]:
                                statepattern[stateout].append(len_e)
            if len(pattern) not in statepattern[stateout]:
                statepattern[stateout].append(len(pattern))

        queue = deque([0])
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

    def substring(self, pattern):
        len_small = []
        index_end_small = []
        for pattern1 in self.patterns:
            if pattern1 != pattern and pattern1 in pattern:
                len_small.append(len(pattern1))
                index_end_small.append(pattern.index(pattern1) + len(pattern1) - 1)
        return len_small, index_end_small

    def search(self, text):
        stateout = 0
        result = []
        for i in range(len(text)):
            while True:
                if text[i] in self.trie[stateout]:
                    stateout = self.trie[stateout][text[i]]
                    break
                else:
                    stateout = self.trie[stateout]['fail']
                    if stateout == 0 and text[i] not in self.trie[stateout]:
                        break
            if stateout in self.statepattern.keys():
                for element in self.statepattern[stateout]:
                    result.append(i - element + 1)
        return result


# myaut = AhoCorasick(("abc", "bc", "c"))
myaut = AhoCorasick(("abc", "aab", "cba", "ab"))
print(myaut.search('aabcbab'))
print(repr(myaut))
