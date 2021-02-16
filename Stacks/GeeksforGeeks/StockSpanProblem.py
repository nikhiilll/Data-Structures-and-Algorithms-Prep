def calculateSpan(a, n):
    """
    TC: O(n)
    SC: O(n)
    """
    span = [1] * n
    stack = []
    i = 0

    while i < n:
        currentSpan = 0
        while stack and a[i] >= a[stack[-1]]:
            j = stack.pop()
            currentSpan += span[j]
        span[i] += currentSpan
        stack.append(i)
        i += 1
    
    return span
