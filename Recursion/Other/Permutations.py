def getPermutations(array):

    permutations = []
    permutationsHelper(array, [], permutations)
    return permutations

def permutationsHelper(array, currentPermutation, permutations):

    if not array and currentPermutation:
        permutations.append(currentPermutation)
    else:
        for i in range(len(array)):
            newPermutation = currentPermutation + [array[i]]
            permutationsHelper(array[:i] + array[i + 1:], newPermutation, permutations)