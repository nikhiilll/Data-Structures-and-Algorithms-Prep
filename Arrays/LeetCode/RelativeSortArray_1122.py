def relativeSortArray(arr1, arr2):

    result = []
    not_in2 = []

    set1 = set(arr1)
    set2 = set(arr2)
    
    for element in arr2:
        count = arr1.count(element)
        result += [element] * count
    
    for element in (set1 - set2):
        count = arr1.count(element)
        not_in2 += [element] * count

    not_in2.sort()
    return (result + not_in2)

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print(relativeSortArray(arr1, arr2))         