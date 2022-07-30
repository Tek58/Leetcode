class Solution(object):
    def wordSubsets(self, words1, words2):
        res = set(words1)
        letters = {}
        for word in words2:
            for letter in word:
                count = word.count(letter)
                if letter not in letters or count > letters[letter]:
                    letters[letter] = count
                    
        for i in words1:
            for j in letters:
                if i.count(j) < letters[j]:
                    res.remove(i)
                    break
        return list(res)
                