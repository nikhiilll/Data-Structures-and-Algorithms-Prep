"""
TC: O(n^3 + m)
SC: O(m + n)
"""


def numbersInPi(pi, numbers):

    numbersSet = set(numbers)
    minSpaces = findMinSpaces(pi, numbersSet, {}, 0)
    return -1 if minSpaces == float("inf") else minSpaces


def findMinSpaces(pi, numbersSet, cache, idx):

    if idx == len(pi):
        return -1
    if idx in cache:
        return cache[idx]

    minSpaces = float("inf")
    for i in range(idx, len(pi)):
        prefix = pi[idx: i + 1]
        if prefix in numbersSet:
            minSpacesInRem = findMinSpaces(pi, numbersSet, cache, i + 1)
            minSpaces = min(minSpaces, minSpacesInRem + 1)
    cache[idx] = minSpaces
    return minSpaces
