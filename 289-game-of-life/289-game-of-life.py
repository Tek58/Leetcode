class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        newBoard = [([0] * (len(board[0])+2)) for i in range(len(board)+2)] #surrounded board
        
        #opy value of board to newBoard
        for i in range(len(board)):
            for j in range(len(board[i])):
                newBoard[i+1][j+1] = board[i][j]

        for i in range(1,len(newBoard)-1):
            for j in range(1,len(newBoard[i])-1):
                board[i-1][j-1] = self.process(i, j, newBoard)

    
    def process(self, row, col, grid):
        count = 0
        for i in range(row-1, row + 2):
            for j in range(col-1, col + 2):
                if grid[i][j] == 1 and (i, j) != (row, col):
                    count += 1
        
        if grid[row][col]:
            if count < 2 or count > 3:
                return 0
            else:
                return 1
        elif count == 3:
            return 1
        return 0
            
        
        