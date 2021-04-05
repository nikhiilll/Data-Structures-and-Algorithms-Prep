from collections import defaultdict, deque

def firstNonRepeatingCharacter(string):

    # dq = deque([])
    # freq = defaultdict(int)

    # for i in len(string):
    #     if freq[string[i]] == 0:
    #         dq.append(i)
    #         freq[string[i]] += 1
    #     else:
    #         freq[string[i]] += 1
    #         while dq and freq[string[dq[0]]] > 1:
    #             dq.popleft()
    
    # return dq[0] if dq else -1

    """
    TC: O(n)
    SC: O(1)
    """
    freq = defaultdict(int)

    for char in string:
        freq[char] += 1

    for i in range(len(string)):
        if freq[string[i]] == 1:
            return i

    return -1