def serialize(root):

    values = []

    def serializeRec(node):
        if node:
            values.append(str(node.val))
            serializeRec(node.left)
            serializeRec(node.right)
        else:
            values.append("#")
    
    serializeRec(root)
    return " ".join(values)

def deserialize(data):

    values = iter(data.split())
    def deserializeRec():
        currentValue = next(values)
        if currentValue == "#":
            return None
        node = TreeNode(int(currentValue))
        node.left = deserializeRec()
        node.right = deserializeRec()
        return node
    
    return deserializeRec()
            