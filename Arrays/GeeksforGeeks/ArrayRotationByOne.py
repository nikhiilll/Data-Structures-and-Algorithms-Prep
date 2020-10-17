import array

def rotate_right_one(arr):
    n = len(arr)
    temp = arr[n - 1]
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
    
    arr[0] = temp
    print(arr)

def rotate_left_one(arr):
    temp = arr[0]
    n = len(arr)
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp
    print(arr)

arr = array.array('i', [1, 2, 3, 4, 5])
rotate_right_one(arr)
rotate_left_one(arr)