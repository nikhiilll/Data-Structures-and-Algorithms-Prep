class stack:
    """
    For all the three methods:
    TC: O(1)
    SC: O(1)
    """
    def __init__(self):
        self.s = []
        self.minEle = None
    
    def push(self, x):
        if not self.minEle or self.minEle == -1:
            self.minEle = x
        else:
            self.minEle = min(self.minEle, x)
        self.s.append((x, self.minEle))
    
    def pop(self):
        if self.s:
            ele = self.s.pop()
            self.minEle = self.getMin()
            return ele[0]
        return -1
    
    def getMin(self):
        if not self.s:
            return -1
        return self.s[-1][1]