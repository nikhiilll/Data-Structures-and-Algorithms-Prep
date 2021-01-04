def minCameraCover(root):
    """
    TC: O(n)
    SC: Average Case: O(logn) | Worst Case: O(n)
    """
    noOfCameras = 0

    def isCameraNeeded(node):

        nonlocal noOfCameras

        if not node:
            return 1
        
        leftCamera = isCameraNeeded(node.left)
        rightCamera = isCameraNeeded(node.right)

        if leftCamera == 0 or rightCamera == 0:
            noOfCameras += 1
            return 2
        elif leftCamera == 2 or rightCamera == 2:
            return 1
        else:
            return 0
    
    if isCameraNeeded(root) == 0:
        noOfCameras += 1
    return noOfCameras