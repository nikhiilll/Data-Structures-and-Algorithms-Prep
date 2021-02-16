class StockSpanner:

    def __init__(self):
        self._data = [] 

    def next(self, price: int) -> int:
        if len(self._data) == 0:
            self._data.append((price, 1))
        else:
            if price >= self._data[-1][0]:
                self._data.append((price, self._data[-1][1] + 1))
            else:
                self._data.append((price, 1))
        return self._data[-1][1]
                