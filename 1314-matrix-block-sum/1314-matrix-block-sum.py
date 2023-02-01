class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        prefix = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                prefix[i][j] = mat[i - 1][j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]

        # print(prefix)
        ans = [[0 for _ in range(m)] for _ in range(n)]
        for row in range(n):
            maxRow = max(0, row - k)
            minRow = min(n, row + k + 1)

            for col in range(m):
                maxCol = max(0, col - k)
                minCol = min(m, col + k + 1)
                
                ans[row][col] = prefix[minRow][minCol] - prefix[minRow][maxCol] - prefix[maxRow][minCol] + prefix[maxRow][maxCol]

        return ans