class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if k >= m + n - 2:
            return m + n - 2
        
        DIR = [0, 1, 0, -1, 0]
        queue = deque([(0, 0, k)])
        seen = set([(0, 0, k)])
        step = 0
        while queue:
            for _ in range(len(queue)):
                r, c, k = queue.popleft()
                if r == m - 1 and c == n - 1:
                    return step
                for i in range(4):
                    nr, nc = r + DIR[i], c + DIR[i + 1]
                    if nr < 0 or nr == m or nc < 0 or nc == n:
                        continue
                    newK = k - grid[nr][nc]
                    newState = (nr, nc, newK)
                    if newK >= 0 and newState not in seen:
                        seen.add(newState)
                        queue.append(newState)
            step += 1

        return -1