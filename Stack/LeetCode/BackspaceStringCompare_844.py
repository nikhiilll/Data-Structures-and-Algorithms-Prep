def backspaceCompare(S, T):

    stack_S = []
    stack_T = []

    for c in S:
        if c == "#":
            if stack_S:
                stack_S.pop()
        else:
            stack_S.append(c)
    
    for c in T:
        if c == "#":
            if stack_T:
                stack_T.pop()
        else:
            stack_T.append(c)
    
    return ("".join(stack_T) == "".join(stack_S))

S = "a#c"
T = "b"
print(backspaceCompare(S, T))



"""
class Solution(object):
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))



"""