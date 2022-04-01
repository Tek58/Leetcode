class Solution:
    def reverseString(self, s: List[str]) -> None:
        self.helper(s, 0)
    
    def helper(self, s, index):
        if index >= len(s)//2:
            return 
        self.helper(s, index + 1)
        curr = len(s) - index -1
        s[curr] , s[index] = s[index], s[curr]