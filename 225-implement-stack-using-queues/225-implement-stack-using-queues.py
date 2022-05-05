class MyStack:

    def __init__(self):
        self.queue = deque()
        
    def push(self, x: int) -> None:
        self.queue.append(x)
        
    def pop(self) -> int:
        for i in range(len(self.queue) - 1):
            val = self.queue.popleft()
            self.queue.append(val)
        return self.queue.popleft()
        
    def top(self) -> int:
        # x = None
        # for i in range(len(self.queue)):
        #     x = self.queue.popleft()
        #     self.queue.append(x)    
        # return x
        return self.queue[-1]

    def empty(self) -> bool:
        return True if not (self.queue) else False
    
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
        
