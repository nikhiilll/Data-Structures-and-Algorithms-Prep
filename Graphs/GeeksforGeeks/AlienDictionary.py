from collections import defaultdict, deque

def findOrder(dict, N, K):

    charSet = set("".join(dict))
    inDegree = {c: 0 for c in charSet}
    graph = defaultdict(list)
    queue = deque()
    ascOrder = ""

    for i in range(len(dict) - 1):
        word1 = dict[i]
        word2 = dict[i + 1]
        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                graph[c1].append[c2]
                inDegree[c2] += 1
                break

    for key, value in inDegree.items():
        if value == 0:
            queue.append(key)

    while queue:
        char = queue.popleft()
        ascOrder += char

        for n in graph[char]:
            inDegree[n] -= 1
            if inDegree[n] == 0:
                queue.append(n)
    
    if set(ascOrder) != charSet:
        ascOrder = ""
    
    return ascOrder



