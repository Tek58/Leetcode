class Solution:
    def candy(self, ratings: List[int]) -> int:
        length = len(ratings)
        if length == 1:
            return 1
        
        left = [1 for i in range(length)]
        right = [1 for i in range(length)]
        
        for i in range(length -1):
            if  ratings[i+1] > ratings[i]:
                left[i+1] = left[i] + 1
            
            index = length - 1 - i
            index1 = length - 1 - i -1
            if ratings[index1] > ratings[index]:
                right[index1] = right[index] + 1
                
        total = 0
        for i in range(length):
            total += (max(right[i], left[i]))
                  
        return total