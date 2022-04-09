class MinStack:
    def __init__(self):
        self.stack = []
        self.minVal = float("inf")
        
    def push(self, x: int) -> None:
        self.minVal = min(self.minVal, x)
        self.stack.append((x, self.minVal))
            
    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.minVal = self.stack[-1][1]
        else:
            self.minVal = float("inf")

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
        
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()