class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()

        max_width = max(horizontalCuts[0], h - horizontalCuts[-1])
        max_height = max(verticalCuts[0], w - verticalCuts[-1])

        if len(horizontalCuts) > 1:
            for i in range(1, len(horizontalCuts)):
                max_width = max(max_width, horizontalCuts[i] - horizontalCuts[i - 1])
                
        if len(verticalCuts) > 1:
            for j in range(1, len(verticalCuts)):
                max_height = max(max_height, verticalCuts[j] - verticalCuts[j - 1])
                
        return (max_height * max_width) % (10**9 + 7)