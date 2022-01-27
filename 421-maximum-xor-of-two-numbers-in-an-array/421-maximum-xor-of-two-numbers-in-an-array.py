class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        numbers, root, result = [], [None, None], 0
        for num in nums:
            numbers.append([0] * 32)
            for ind in range(1, 33):
                numbers[-1][-ind] = num % 2
                num = num >> 1
                
            node = root
            for n in numbers[-1]:
                if not node[n]:
                    node[n] = [None, None]
                node = node[n]
        for num in numbers:
            node, temp = root, 0
            for n in num:
                temp = (temp << 1) + (node[1 - n] is not None)
                node = node[(1 - n) if node[1 - n] else n]
            result = max(result, temp)
        return result
    