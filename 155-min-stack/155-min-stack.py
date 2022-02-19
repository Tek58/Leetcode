class MinStack:

    def __init__(self):
        self.value = []
        self.minStack = []
        

    def push(self, x: int) -> None:
        self.value.append(x)
        x = min(x, self.minStack[-1] if self.minStack else x)
        self.minStack.append(x)

    def pop(self) -> None:
        self.value.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.value[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()