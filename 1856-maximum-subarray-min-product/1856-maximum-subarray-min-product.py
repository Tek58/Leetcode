class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        prefix = [0]
        stack = []
        maxSMP = 0
        for i, num in enumerate(nums):
            prefix.append(num+prefix[i])
            index = i
            while stack and num < stack[-1][0]:
                topElement, lastIndex = stack.pop()
                val = (prefix[i] - prefix[lastIndex]) * topElement
                maxSMP = max(maxSMP, val)
                index = lastIndex
            stack.append((num, index))

        for num, i in stack:
            val = (prefix[-1] - prefix[i]) * num
            maxSMP = max(maxSMP, val)
        
        return maxSMP % (10**9 + 7)
                
                
