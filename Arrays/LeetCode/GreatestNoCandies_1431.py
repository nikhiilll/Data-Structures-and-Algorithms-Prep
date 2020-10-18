def kidsWithCandies(candies, extraCandies):
    max = -1
    result = []
    for candy in candies:
        if candy > max:
            max = candy
        
    for candy in candies:
        if (candy + extraCandies >= max):
            result.append(True)
        else:
            result.append(False)
    
    return result

candies = [4,2,1,1,2]
extraCandies = 1
print(kidsWithCandies(candies, extraCandies))
