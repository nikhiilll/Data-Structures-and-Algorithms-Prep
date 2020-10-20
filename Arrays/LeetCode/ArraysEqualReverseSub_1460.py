def canBeEqual(target, arr):

    target.sort()
    arr.sort()

    if target == arr:
        return True
    else:
        return False