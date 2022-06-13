class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        container = triangle[len(triangle)-1]
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                container[j] = triangle[i][j] + (min(container[j], container[j+1]))
        
        return container[0]
            
        