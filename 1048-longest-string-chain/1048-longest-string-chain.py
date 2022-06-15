class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        word_dict = defaultdict(int)
        
        total_max = 0
        
        for w in words:
            for i in range(len(w)):
                wc = w[:i] + w[i+1:]
                word_dict[w] = max(word_dict[wc] + 1, word_dict[w])
            total_max = max(total_max, word_dict[w])
    
        return total_max
        