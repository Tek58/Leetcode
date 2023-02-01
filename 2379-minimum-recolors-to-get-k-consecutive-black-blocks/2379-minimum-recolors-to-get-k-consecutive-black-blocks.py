class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = len(blocks)
        for i in range(len(blocks)):
            curr = blocks[i:i + k]
            if len(curr) == k:
                if curr.count('W') < res:
                    res = curr.count('W')

        return res