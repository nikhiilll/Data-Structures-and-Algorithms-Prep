def classPhotos(redShirtHeights, blueShirtHeights):
    """
    TC: O(nlogn)
    SC: O(1)
    """
    def helper(arr1, arr2):
        for i in range(len(arr1)):
            if arr1[i] >= arr2[i]:
                return False
        return True
    
    redShirtHeights.sort(reverse = True)
    blueShirtHeights.sort(reverse = True)

    if redShirtHeights[0] > blueShirtHeights[0]:
        return helper(blueShirtHeights, redShirtHeights)
    else:
        return helper(redShirtHeights, blueShirtHeights)