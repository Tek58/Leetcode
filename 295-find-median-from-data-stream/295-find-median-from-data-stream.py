class MedianFinder:

    def __init__(self):
        self.container = []
        

    def addNum(self, num: int) -> None:
        self.container.append(num)

    def findMedian(self) -> float:
        self.container.sort()
        x = len(self.container)
        if x%2 != 0:
            return self.container[x//2]
        return (self.container[(x//2)-1] + self.container[x//2])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()