class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        queue = deque([])
        ans = []
        for num in sorted(changed):
            if queue and num == queue[0]:
                queue.popleft()
            else:
                queue.append(2 * num)
                ans.append(num)

        if queue:
            return []
        return ans