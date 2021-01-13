def floodFill(image, sr, sc, newColor):
    """ 
    TC: O(l * w)
    SC: O(l * w)
    """
    def getNeighbours(x, y, image, newColor):

        neighbours = []

        if x - 1 >= 0 and newColor != image[x - 1][y] and image[x][y] == image[x - 1][y]:
            neighbours.append((x - 1, y))
        if x + 1 < len(image) and newColor != image[x + 1][y] and image[x][y] == image[x + 1][y]:
            neighbours.append((x + 1, y))
        if y - 1 >= 0 and newColor != image[x][y - 1] and image[x][y] == image[x][y - 1]:
            neighbours.append((x, y - 1))
        if y + 1 < len(image[0]) and  newColor != image[x][y + 1] and image[x][y] == image[x][y + 1]:
            neighbours.append((x, y + 1))
        
        return neighbours

    # visited = [[False for _ in range(len(image[0]))] for _ in range(len(image))]
    stack = [(sr, sc)]

    while stack:
        pixelX, pixelY = stack.pop()
        if image[pixelX][pixelY] == newColor:
            continue
        neighbours = getNeighbours(pixelX, pixelY, image, newColor)
        image[pixelX][pixelY] = newColor
        stack.extend(neighbours)
    
    return image

