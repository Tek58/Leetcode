class Solution(object):
    def kthSmallest(self, matrix, k):
        lis = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                lis.append(matrix[i][j])
        lis.sort()
        return lis[k-1]
        