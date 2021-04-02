# def interweavingStrings(one, two, three):

#     combinations = set()
#     findAllPossibleStrings(one, two, "", combinations)
#     return three in combinations

# def findAllPossibleStrings(one, two, currPerm, combinations):

#     if not one and not two:
#         combinations.add(currPerm)
#         return
#     elif not one:
#         combinations.add(currPerm + two)
#         return
#     elif not two:
#         combinations.add(currPerm + one)
#         return

#     findAllPossibleStrings(one[1:], two, currPerm + one[0], combinations)
#     findAllPossibleStrings(one, two[1:], currPerm + two[0], combinations)

def interweavingStrings(one, two, three):

    if len(one) + len(two) != len(three):
        return False

    cache = [[None for _ in range(len(two) + 1)] for _ in range(len(one) + 1)]
    return interwovenString(one, two, three, 0, 0, cache)


def interwovenString(one, two, three, i, j, cache):

    if cache[i][j] is not None:
        return cache[i][j]

    k = i + j
    if k == len(three):
        return True

    if i < len(one) and one[i] == three[k]:
        cache[i][j] = interwovenString(one, two, three, i + 1, j, cache)
        if cache[i][j]:
            return True

    if j < len(two) and two[j] == three[k]:
        cache[i][j] = interwovenString(one, two, three, i, j + 1, cache)
        return cache[i][j]

    cache[i][j] = False
    return False

print(interweavingStrings("algoexpert",
                          "your-dream-job", "1your-algodream-expertjob"))
