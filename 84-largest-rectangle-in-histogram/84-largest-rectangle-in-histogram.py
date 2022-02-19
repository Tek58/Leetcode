class Solution:
    def largestRectangleArea(self, height):
        height.append(0)
        maxRectangle = 0
        rectangle = []
        for i in range(len(height)):
            curr, index = height[i], i
            while rectangle and curr < rectangle[-1][0]:
                lastHeight, lastIndex = rectangle.pop()
                maxRectangle = max(maxRectangle, (lastHeight*(i - lastIndex)))
                index = lastIndex
            rectangle.append((curr, index))
            
        return maxRectangle
                
            
        