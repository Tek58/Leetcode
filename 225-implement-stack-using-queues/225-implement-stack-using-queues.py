class MyStack:

    def __init__(self):
        self.value = []
        self.size = 0
        

    def push(self, x: int) -> None:
        self.size = self.size + 1
        self.value = [x] + self.value
        

    def pop(self) -> int:
        if self.size == 0:
            return
        self.size = self.size - 1
        val = self.value[0]
        self.value = self.value[1:]
        return val
        

    def top(self) -> int:
        return self.value[0]
        

    def empty(self) -> bool:
        if self.size == 0:
            return True
        return False
    
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()