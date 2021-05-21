"""
TC: O(m * n)
SC: O(min(m, n))
"""


def longestCommonSubsequence(text1, text2):

    if not text1 or not text2:
        return 0

    if len(text1) > len(text2):
        text1, text2 = text2, text1

    odd = [0 for _ in range(len(text1) + 1)]
    even = [0 for _ in range(len(text1) + 1)]

    for i in range(1, len(text2) + 1):
        if i % 2 == 0:
            current = even
            previous = odd
        else:
            current = odd
            previous = even
        for j in range(1, len(text1) + 1):
            if text2[i - 1] == text1[j - 1]:
                current[j] = previous[j - 1] + 1
            else:
                current[j] = max(current[j - 1], previous[j])

    return even[-1] if len(text2) % 2 == 0 else odd[-1]
