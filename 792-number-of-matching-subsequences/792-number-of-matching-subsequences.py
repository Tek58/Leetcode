class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        store = defaultdict(list)

        for word in words:
            store[word[0]].append(word)

        count = 0
        for ch in s:
            curr = store[ch]
            store[ch] = []
            while curr:
                word = curr.pop()[1:]
                if len(word) == 0:
                    count += 1
                else:
                    store[word[0]].append(word)

        return count