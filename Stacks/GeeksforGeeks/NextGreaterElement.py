def nextGreaterElement(arr, n):
    """
    TC: O(n)
    SC: O(n)
    """
    ans = [-1] * n
    i = 0
    stack = []

    while i < n:
        while stack and arr[i] > arr[stack[-1]]:
            j = stack.pop()
            ans[j] = arr[i]
        stack.append(i)
        i += 1
    
    return ans