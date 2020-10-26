def removeDuplicates(s, k):

    stack = []
    S = list(s)
    isPopped = True

    while isPopped:

        isPopped = False
        count_duplicate = 1

        for c in S:
            if not stack:
                stack.append(c)
            elif stack[-1] != c:
                stack.append(c)
                count_duplicate = 1
            else:
                count_duplicate += 1
                stack.append(c)

            if count_duplicate == k:
                while count_duplicate > 0:
                    stack.pop()
                    count_duplicate -= 1
                    isPopped = True

        S = stack
        stack = []
    
    return "".join(S)

s = "pbbcggttciiippooaais"
k = 2
print(removeDuplicates(s, k))



"""
    
    stack = []

    for c in s:
        if not stack or stack[-1][0] != c:
            stack.append((c, 1))
        else:
            count = (stack.pop()[1] + 1) % k
            if count:
                stack.append((c, count))




"""
        
            


