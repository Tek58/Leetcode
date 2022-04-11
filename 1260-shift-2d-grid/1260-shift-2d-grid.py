class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if k == 0:
            return grid
        nums = [0] * len(grid) * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                nums[i * len(grid[0]) + j] = grid[i][j]
        k = k % len(nums)
        
        nums = nums[-k:] + nums[:-k]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = nums[i * len(grid[0]) + j]
        return grid
            
        
        