def sumOddLengthSubarrays(arr):

    sum = 0
    sum_array = []
    n = len(arr)

    for i in range(1, n + 1, 2):
        for j in range(0, n - i + 1):
            sum_array += arr[j : j + i]
    
    for val in sum_array:
        sum += val
    
    return sum

arr = [31,38,4,7,13,37,25,35,21,25,50,47,8,28,24,25,21,31,54,45,50,34,47,3,50,7,13,13,12,6,41,12,44,36,60,8,3,39,44,30,20,1,9,8,31,58,44,5,31,30]
print(sumOddLengthSubarrays(arr))


"""
TC: O(n)
SC: O(1)

Consider the subarray that contains A[i],
we can take 0,1,2..,i elements on the left,
from A[0] to A[i],
we have i + 1 choices.

we can take 0,1,2..,n-1-i elements on the right,
from A[i] to A[n-1],
we have n - i choices.

In total, there are (i + 1) * (n - i) subarrays, that contains A[i].
And there are ((i + 1) * (n - i) + 1) / 2 subarrays with odd length, that contains A[i].
A[i] will be counted ((i + 1) * (n - i) + 1) / 2 times.

res, n = 0, len(A)
        for i, a in enumerate(A):
            res += ((i + 1) * (n - i) + 1) / 2 * a
        return res

"""