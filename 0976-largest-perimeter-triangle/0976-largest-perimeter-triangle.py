class Solution:
    def largestPerimeter(self, A: List[int]) -> int: 
        A = sorted(A)
        for i in range(1,len(A)-1):
            last_element, second_last, third_last = A[-i], A[-i-1], A[-i-2]
            if last_element <  (second_last + third_last):
                return last_element + second_last + third_last
            if len(A) <= 3:
                break
        return 0