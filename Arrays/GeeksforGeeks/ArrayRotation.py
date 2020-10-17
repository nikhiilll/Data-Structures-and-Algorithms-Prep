import array

def rotate_array(arr, d, n):
    """
        New array approach
    """
    new_array = array.array('i', [])
    for i in range(len(arr)):
        new_array.insert((i - d) % len(arr), arr[i])
    print(new_array)


#Best case solution
#Time: O(n) Space: O(1)
def rotate_array_best(arr, d, n):
    d = d % n
    g_c_d = gcd(d, n)
    for i in range(g_c_d):
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp
    
    print(arr)

def gcd(a, b): 
    if b == 0: 
        return a; 
    else: 
        return gcd(b, a % b)

arr = array.array('i', [2, 3, 4, 5, 6, 7, 8, 9])
rotate_array(arr, 3, len(arr))
rotate_array_best(arr, 3, len(arr))


"""
Method 4 (The Reversal Algorithm) :
Algorithm : 
 

rotate(arr[], d, n)
  reverse(arr[], 1, d) ;
  reverse(arr[], d + 1, n);
  reverse(arr[], 1, n);
"""


