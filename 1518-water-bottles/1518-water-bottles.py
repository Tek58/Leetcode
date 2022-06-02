class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drunk = numBottles
        empty = numBottles
        
        while empty >= numExchange:
            new = empty// numExchange
            left = empty % numExchange
            drunk += new 
            empty = new+ left
        return drunk