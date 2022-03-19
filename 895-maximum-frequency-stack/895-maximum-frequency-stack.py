class FreqStack:
    def __init__(self):
        self.heap = []
        self.store = collections.defaultdict(int)
        self.counter = 0
         
    def push(self, x):
        self.store[x]+=1
        heapq.heappush(self.heap,(-self.store[x], -self.counter, x))
        self.counter += 1

    def pop(self):
        val = heapq.heappop(self.heap)
        self.store[val[2]] -= 1
        return val[2]

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()