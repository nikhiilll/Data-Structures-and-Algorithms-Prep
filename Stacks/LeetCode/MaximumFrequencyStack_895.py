import collections

class FreqStack:

    def __init__(self):
        self.freq = collections.Counter()
        self.stack_map = collections.defaultdict(list)
        self.max_freq = 0


    def push(self, x: int) -> None:
        freq, stack_map = self.freq, self.stack_map
        freq[x] += 1
        self.max_freq = max(self.max_freq, freq[x])
        stack_map[freq[x]].append(x)     

    def pop(self) -> int:
        freq, stack_map = self.freq, self.stack_map
        x = stack_map[self.max_freq].pop()
        freq[x] -= 1
        if not stack_map[self.max_freq]: self.max_freq -= 1
        return x
        

        