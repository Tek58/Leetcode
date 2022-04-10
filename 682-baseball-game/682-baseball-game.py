class Solution:
    def calPoints(self, ops: List[str]) -> int:
        count = []
        for i in ops:
            if i == '+':
                x = count[-1]
                y = count[-2]
                count.append(x+y)
            elif i == 'C':
                count.pop()
            elif i == 'D':
                x = count[-1]
                count.append(2*x)
            else:
                count.append(int(i))
        return sum(count)
                
                