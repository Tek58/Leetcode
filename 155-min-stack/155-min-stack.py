class MinStack:

    def __init__(self):
        self.value = []
        self.size = 0
        

    def push(self, x: int) -> None:
        self.size = self.size + 1
        self.value = [x] + self.value        

    def pop(self) -> None:
        if self.size == 0:
            return
        self.size = self.size - 1
        val = self.value[0]
        self.value = self.value[1:]
        return val      

    def top(self) -> int:
        return self.value[0]
        

    def getMin(self) -> int:
        return min(self.value)
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()