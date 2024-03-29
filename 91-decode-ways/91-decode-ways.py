class Solution:
    def numDecodings(self, s: str) -> int:
        mapping = set()
        for i in range(1, 27):
            mapping.add(str(i))
        
        return self.break_string(s, 0, mapping, {})
        
    
    def break_string(self, s, count, mapping, memo):
        if s == "":
            return count + 1

        ans = 0
        if s not in memo:
            for i in range(len(s)):
                if s[:i+1] in mapping:
                    ans += self.break_string(s[i+1:], count, mapping, memo)
            memo[s] = ans
            
        return memo[s]