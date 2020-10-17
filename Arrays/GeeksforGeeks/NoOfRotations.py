def no_of_rotations(arr, low, high):
    """
        The linear search way would be to find the index of the lowest element
    """
    if high < low:
        return 0 

    if low == high:
        return low
    
    mid = low + (high - low)//2

    if (mid < high and arr[mid + 1] < arr[mid]):
        return (mid + 1)
    
    if(mid > low and arr[mid] < arr[mid - 1]):
        return mid
    
    if (arr[high] > arr[mid]):
        return no_of_rotations(arr, low, mid - 1)
    else:
        return no_of_rotations(arr, mid + 1, high)


arr = [15, 18, 20, 1, 2, 3, 6, 11, 12, 13, 14] 
n = len(arr)
print(no_of_rotations(arr, 0, n - 1))