class Solution(object):
    def findSubstring(self, s, words):
        res = []
        n, m = len(words), len(words[0])
        words = collections.Counter(words)
        
        for i in range(len(s) - n * m + 1 ):
            temp = collections.Counter()
            count = 0
            for j in range(i, i + n * m, m):
                w = s[j : j + m]
                if w in words:
                    temp[w] += 1
                    count += 1
                    if temp[w] > words[w]: 
                        break
                    if count == n:
                        res.append(i)
        return res
        