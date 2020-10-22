def threeConsecutiveOdds(arr):

    i = 0
    while i < len(arr) - 2:
        if arr[i] % 2 != 0:
            print(arr[i])
            if arr[i + 2] % 2 != 0:
                print(arr[i + 2])
                if arr[i + 1] % 2 != 0:
                    print(arr[i + 1])
                    return True
            i += 3  
        i += 1
    
    return False

arr = [1,2,34,3,4,5,7,23,12]
print(threeConsecutiveOdds(arr))

            
            