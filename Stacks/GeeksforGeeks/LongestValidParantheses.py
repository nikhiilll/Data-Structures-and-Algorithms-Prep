def maxLength(S):
    """
    TC: O(n)
    SC: O(n)
    """
    stack = []
    count = 0
    left = -1

    for i in range(len(S)):
        if S[i] == "(":
            stack.append(i)
        else:
            if not stack:
                left = i
            else:
                stack.pop()
                if not stack:
                    count = max(count, i - left)
                else:
                    count = max(count, i - stack[-1])
    
    return count
        