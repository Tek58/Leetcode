from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        x = Counter (arr)
        if len(x) == 1:
            return 1

        count = 0
        total = 0
        lis = [y for z, y in x.items()]
        lis.sort(reverse=True)
        
        for i in lis:
            total += i
            count += 1
            if total >= len(arr)//2:
                return count
