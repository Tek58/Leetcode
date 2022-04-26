class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Count = defaultdict(int)
        s2Count = defaultdict(int)
        for i in range(len(s1)):
            s1Count[s1[i]] += 1
            s2Count[s2[i]] += 1
            
        left = matches = 0
        for i in range(26):
            curr = chr(ord('a')+i)
            if s1Count[curr] == s2Count[curr]:
                matches += 1
            
                    
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            curr = s2[right]
            s2Count[curr] += 1
            if s1Count[curr] == s2Count[curr]:
                matches += 1
            elif s1Count[curr] + 1 == s2Count[curr]:
                matches -= 1
                
            curr = s2[left]
            s2Count[curr] -= 1
            if s1Count[curr] == s2Count[curr]:
                matches += 1
            elif s1Count[curr] - 1 == s2Count[curr]:
                matches -= 1
            
            left += 1              
        return matches == 26