def buildArray(target, n):

    operations = []
    j = 0
    for i in range(1, n + 1):
        if j == len(target):
            return operations
        if i == target[j]:
            j += 1
            operations.append("Push")
        else:
            operations.extend(["Push", "Pop"])
    return operations

target = [1,2]
n = 4
print(buildArray(target, n))