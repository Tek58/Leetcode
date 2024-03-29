class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        score = 0
        tokens.sort()
        
        while tokens:
            if tokens[0] <= P:
                P -= tokens[0]
                score += 1
                tokens.pop(0)
            else:
                if score and len(tokens)>2:
                    score -= 1
                    P += tokens.pop()
                else:
                    tokens.pop()
                    
        return score