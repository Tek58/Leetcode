class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for i in range(len(temperatures))]
        stack = [0]
        for i in range(1,len(temperatures)):
            curr = temperatures[i]
            while stack and temperatures[stack[-1]] < curr :
                prevIndex = stack.pop()
                result[prevIndex] = i - prevIndex
            stack.append(i)
        return result
            