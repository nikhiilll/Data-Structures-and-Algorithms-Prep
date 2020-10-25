class CustomStack:

    def __init__(self, maxSize: int):
        self._data = [] * maxSize
        self.maxSize = maxSize
        

    def push(self, x: int) -> None:
        if len(self._data) != self.maxSize:
            self._data.append(x)
        

    def pop(self) -> int:
        if self._data != []:
            return self._data.pop()
        else:
            return (-1)
        

    def increment(self, k: int, val: int) -> None:
        if k < len(self._data):
            for i in range(k):
                self._data[i] += val
        else:
            for i in range(len(self._data)):
                self._data[i] += val