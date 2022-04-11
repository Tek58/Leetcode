class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = defaultdict(int)
        left = maxLen = 0
        for i in range(len(s)):
            store[s[i]] += 1
            while store[s[i]] > 1:
                store[s[left]] -= 1
                left += 1
            maxLen = max(maxLen, (i - left)+1)            
        return maxLen
                
                
            