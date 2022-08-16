class Solution:
    def firstUniqChar(self, s: str) -> int:
        store = Counter(s)
        for i in range(len(s)):
            if store[s[i]] == 1:
                return i
        return -1