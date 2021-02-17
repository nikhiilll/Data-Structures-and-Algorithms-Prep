def getMaxArea(histogram):
    """
    TC: O(n)
    SC: O(n)
    """
    stack = []
    maxArea = float("-inf")
    index = 0

    while index < len(histogram):

        if not stack or histogram[stack[-1]] <= histogram[index]:
            stack.append(index)
            index += 1
        else:
            top = stack.pop()
            area = histogram[top] * ((index - stack[-1] - 1) if stack else index)
            maxArea = max(maxArea, area)
    
    while stack:
        top = stack.pop()
        area = histogram[top] * ((index - stack[-1] - 1) if stack else index)
        maxArea = max(maxArea, area)

    return maxArea
        