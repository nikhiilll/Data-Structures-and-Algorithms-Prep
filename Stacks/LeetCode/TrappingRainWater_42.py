def trap(height):
    """
    TC: O(n)
    SC: O(n)
    """
    # n = len(height)

    # if n < 3:
    #     return 0

    # leftHeight = [-1] * n
    # current = height[0]

    # for i in range(1, n - 1):
    #     if current > height[i]:
    #         leftHeight[i] = current
    #     current = max(current, height[i])
    
    # trapped = 0
    # current = height[-1]

    # for i in range(n - 2, 0, -1):
    #     if leftHeight[i] != -1 and current > height[i]:
    #         trapped += (min(leftHeight[i], current) - height[i])
    #     current = max(current, height[i])
    
    # return trapped

    """
    TC: O(n)
    SC: O(1)
    """
    n = len(height)
    if n < 3:
        return 0

    leftMax, rightMax = height[0], height[n - 1]
    left, right = 0, n -1
    trapped = 0

    while left < right:
        leftMax = max(leftMax, height[left])
        rightMax = max(rightMax, height[right])
        if leftMax <= rightMax:
            trapped += leftMax - height[left]
            left += 1
        else:
            trapped += rightMax - height[right]
            right -= 1
    
    return trapped
