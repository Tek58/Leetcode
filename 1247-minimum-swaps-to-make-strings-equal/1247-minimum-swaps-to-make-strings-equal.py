class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        if len(s1) != len(s2):
            return -1
        x_y = y_x = 0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                if s1[i] == 'x':
                    x_y += 1
                else:
                    y_x += 1
                    
        r1, x_y = divmod(x_y,2)
        r2, y_x = divmod(y_x,2)
        
        if x_y != y_x:
            return -1
        
        return r1 + r2 + x_y + y_x