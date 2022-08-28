class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        new_grid = []
        for i in range(len(mat)):
            temp = []
            for j in range(len(mat[0])):
                temp.append(0)
            new_grid.append(temp)
        
        diagonal_start = []
        for i in range(len(mat)):
            diagonal_start.append((i,0))
        for j in range(1,len(mat[0])):
            diagonal_start.append((0,j))
        
        queue = deque([diagonal_start[0]])
        left = 1
        temp = []
        curr_val = []
        while queue:
            row, col = queue.popleft()
            temp.append((row,col))
            curr_val.append(mat[row][col])
            if (row == len(mat)-1) or (col == len(mat[0])-1):
                curr_val.sort()
                for index, val in enumerate(temp):
                    newRow = val[0]
                    newCol = val[1]
                    new_grid[newRow][newCol] = curr_val[index]
                temp = []
                curr_val = []
                
                if left < len(diagonal_start):
                    queue.append(diagonal_start[left])
                    left += 1
            else:
                if row+1 < len(mat) and col+1 < len(mat[0]):
                    queue.append((row+1, col+1))
            
        return new_grid