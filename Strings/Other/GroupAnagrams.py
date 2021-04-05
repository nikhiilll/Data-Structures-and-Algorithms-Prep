from collections import defaultdict

def groupAnagrams(words):
    """
    TC: O(w * nlogn)
    SC: O(wn)
    """
    wordMap = defaultdict(list)

    for word in words:
        ascWord = "".join(sorted(word))
        wordMap[ascWord].append(word)
    
    return list(wordMap.values())