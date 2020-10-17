import array
"""
The array can be sorted at the start if not sorted and then this method can be used.
"""
def find_pair_sum(arr, sum):
    n = len(arr)
    left_ptr = 0
    right_ptr = n - 1
    while left_ptr < right_ptr:
        if arr[left_ptr] + arr[right_ptr] > sum:
            right_ptr -= 1
        elif arr[left_ptr] + arr[right_ptr] < sum:
            left_ptr += 1
        else:
            print("Sum found in: {} {}".format(arr[left_ptr], arr[right_ptr]))
            break
    else:
        print("No sum found")

arr = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
find_pair_sum(arr, 20)