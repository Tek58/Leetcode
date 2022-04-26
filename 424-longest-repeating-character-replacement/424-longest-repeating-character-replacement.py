class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        store = defaultdict(int)
        res = 0
        maxFrequency = 0
        while right < len(s):
            store[s[right]] += 1
            maxFrequency = max(maxFrequency, store[s[right]])
            curr = (right - left)+1 - maxFrequency
            if curr <= k:
                res = max(res, ((right - left)+1))
            else:
                while ((right - left)+1 - maxFrequency) > k:
                    store[s[left]] -= 1
                    left += 1
            right += 1
        return res
                
                