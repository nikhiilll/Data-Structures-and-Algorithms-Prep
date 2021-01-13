from collections import deque

def minStepToReachTarget(KnightPos, TargetPos, N):

    visited = [[False for _ in range(N)] for _ in range(N)]

    #Shift position to (0, 0) origin from (1, 1) origin
    KnightPos[0] = KnightPos[0] - 1
    KnightPos[1] = KnightPos[1] - 1
    TargetPos[0] = TargetPos[0] - 1
    TargetPos[1] = TargetPos[1] - 1
    minSteps = float("inf")
    queue = deque([(KnightPos, 0)])     #Queue for BFS Traversal

    while queue:
        node = queue.popleft()
        currentPath = node[1]
        nodePosRow, nodePosCol = node[0][0], node[0][1]

        if nodePosRow == 0 and nodePosCol == 0:
            minSteps = min(minSteps, currentPath)
            continue

        visited[nodePosRow][nodePosCol] = True
        neighbours = getNeighbours(nodePosRow, nodePosCol, N)

        for neighbour in neighbours:
            if not visited[neighbour[0]][neighbour[1]]:
                queue.append((neighbour, currentPath + 1))
    
    return minSteps

def getNeighbours(row, col, N):

    neighbours = []

    if N > row - 2 >= 0 and N > col - 1 >= 0:
        neighbours.append([row - 2, col - 1])
    if N > row - 2 >= 0 and 0 <= col + 1 < N:
        neighbours.append([row - 2, col + 1])
    if 0 <= row + 2 < N and N > col - 1 >= 0:
        neighbours.append([row + 2, col - 1])
    if 0 <= row + 2 < N and 0 <= col + 1 < N:
        neighbours.append([row + 2, col + 1])

    if N > row - 1 >= 0 and N > col - 2 >= 0:
        neighbours.append([row - 1, col - 2])
    if 0 <= row + 1 < N and N > col - 2 >= 0:
        neighbours.append([row + 1, col - 2])
    if N > row - 1 >= 0 and 0 <= col + 2 < N:
        neighbours.append([row - 1, col + 2])
    if 0 <= row + 1 < N and 0 <= col + 2 < N:
        neighbours.append([row + 1, col + 2])
    
    return neighbours
    

