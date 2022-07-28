class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        store = Counter(s)
        for i in t:
            if i not in store:
                return False
            store[i] -= 1
        
        for value in store.values():
            if value > 0:
                return False
        return True
        