"""
TC: O(n * m)
SC: O(n * m)
"""


def levenshteinDistance(str1, str2):

    edits = [[i for i in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
    for c in range(len(str1) + 1):
        edits[c][0] = c

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                edits[i][j] = edits[i - 1][j - 1]
            else:
                edits[i][j] = 1 + min(edits[i - 1][j - 1],
                                      edits[i - 1][j], edits[i][j - 1])

    return edits[-1][-1]


def levenshteinDistance2(str1, str2):

    if len(str1) > len(str2):
        str1, str2 = str2, str1

    oddEdits = [None for _ in range(len(str1) + 1)]
    evenEdits = [i for i in range(len(str1) + 1)]

    for i in range(1, len(str2) + 1):
        if i % 2 == 0:
            currentEdit = evenEdits
            previousEdit = oddEdits
        else:
            currentEdit = oddEdits
            previousEdit = evenEdits
        currentEdit[0] = i
        for j in range(1, len(str1) + 1):
            if str1[j - 1] == str2[i - 1]:
                currentEdit[j] = previousEdit[j - 1]
            else:
                currentEdit[j] = 1 + min(previousEdit[j],
                                         previousEdit[j - 1], currentEdit[j - 1])

    return evenEdits[-1] if len(str2) % 2 == 0 else oddEdits[-1]
