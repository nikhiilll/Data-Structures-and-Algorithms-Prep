def wordBreak(s, wordDict):

    wordDictSet = set(wordDict)

    def isBreakable(start, end, str, wordSet):

        if start == end:
            return True

        i = start

        while i <= end:
            if str[start:i] in wordSet and isBreakable(i, end, str, wordSet):
                return True
            i += 1
        return False

    return isBreakable(0, len(s), s, wordDictSet)


def wordBreak2(s, wordList):

    doesWordEnd = [False for _ in s]

    for i in range(len(s)):
        for word in wordList:
            if word == s[i - len(word) + 1: i + 1] and (doesWordEnd[i - len(word)] or (i - len(word)) == -1):
                doesWordEnd[i] = True

    return doesWordEnd[-1]


print(wordBreak2("leetcode", ["leet", "code"]))
