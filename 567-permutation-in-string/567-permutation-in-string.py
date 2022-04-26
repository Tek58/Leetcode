class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = Counter(s1)
        s2Count = Counter(s2[:len(s1)])
        left = 0
        for right in range(len(s1), len(s2)):
            flag = True
            for key, val in s1Count.items():
                if (key in s2Count and s2Count[key] != val) or key not in s2Count:
                    flag = False
                    break
            if flag:
                return flag
            s2Count[s2[right]] += 1
            s2Count[s2[left]] -= 1
            left += 1              
        flag = True
        for key, val in s1Count.items():
            if (key in s2Count and s2Count[key] != val) or key not in s2Count:
                flag = False
                break
        if flag:
            return flag