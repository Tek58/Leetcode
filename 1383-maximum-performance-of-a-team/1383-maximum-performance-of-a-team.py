class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        heap, speedSum = [], 0

        res = 0
        for efficiency, speed in sorted(zip(efficiency, speed), reverse=True):

            heapq.heappush(heap, speed)
            speedSum += speed

            if len(heap) == k + 1:
                speedSum -= heapq.heappop(heap)

            res = max(res, speedSum * efficiency)

        return res % (10 ** 9 + 7)