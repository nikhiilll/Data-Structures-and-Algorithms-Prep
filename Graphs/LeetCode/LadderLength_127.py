from collections import deque

def ladderLength(beginWord, endWord, wordList):

    def constructDict(wordList):
        d = {}
        for word in wordList:
            for i in range(len(word)):
                s = word[:i] + "_" + word[i+1:]
                d[s] = d.get(s, []) + [word]

        return d
    
    def bfsWords(begin, end, wordDict):

        queue, visited = deque([(begin, 1)]), set()

        while queue:
            word, steps = queue.popleft()
            if word not in visited:
                visited.add(word)
                if word == end:
                    return steps
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i+1:]
                    neighbourWords = wordDict.get(s, [])
                    for neigh in neighbourWords:
                        if neigh not in visited:
                            queue.append((neigh, steps + 1))
        
        return 0
    
    d = constructDict(set(wordList))
    return bfsWords(beginWord, endWord, d)
