class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        top_val = [0]*7
        bot_val = [0]*7
        val_total = [len(tops)]*7
        for top, bot in zip(tops, bottoms):
            print(top, bot)
            if top == bot:
                val_total[top] -= 1
            else:
                top_val[top] += 1
                bot_val[bot] += 1
                
        for val in range(1, 7):
            if (val_total[val] - top_val[val]) == bot_val[val]:
                return min(top_val[val], bot_val[val])
            
        return -1