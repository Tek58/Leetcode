class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}
        for word in strs:
            val = "".join(sorted(word)) 
            if val in store:
                store[val].append(word)
            else:
                store[val] = [word]
        
        return store.values()
        