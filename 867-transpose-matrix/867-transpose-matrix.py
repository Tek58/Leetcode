class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = []
        for col in range(len(matrix[0])):
            transpose.append([]) 
            for row in range(len(matrix)):
                transpose[col].append(matrix[row][col])
        return transpose