class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = [[] for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                transpose[j].append(matrix[i][j])
        return transpose