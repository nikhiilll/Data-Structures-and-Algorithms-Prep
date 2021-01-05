def kthSmallest(root, k):
    """
    TC: O(n)
    SC: Average Case - O()
    """
    if not root:
        return 
    
    counter = [0]
    kthsmall = [0]

    def findKthSmallest(node, counter, kthsmall, k):

        if not node:
            return
        if counter[0] == k:
            return
        findKthSmallest(node.left, counter, kthsmall, k)
        if counter[0] < k:
            counter[0] += 1
            kthsmall[0] = node.val
        if counter[0] < k:
            findKthSmallest(node.right, counter, kthsmall, k)
        
        return
    
    findKthSmallest(root, counter, kthsmall, k)
    return kthsmall[0]