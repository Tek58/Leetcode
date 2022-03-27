class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        store = Counter(ransomNote)
        store1 = Counter(magazine)
        for key, val in store.items():
            if key not in store1:
                return False
            if store[key] > store1[key]:
                return False
        return True
            