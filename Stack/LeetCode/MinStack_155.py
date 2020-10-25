class MinStack:

    def __init__(self):
        self._data = []
        

    def push(self, x: int) -> None:
        # self._data.append(x)
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self._data.append((x, curMin))
        

    def pop(self) -> None:
        self._data.pop()
        

    def top(self) -> int:
        return self._data[-1][0]
        

    def getMin(self) -> int:
        # min = float('inf')
        # for num in self._data:
        #     if num < min:
        #         min = num
        # return min
        return self._data[-1][1]