class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transformations = set()
        for word in words:
            curTransformation = ''
            for letter in word:
                morseLetter = code[ord(letter)-97]
                curTransformation += morseLetter
            transformations.add(curTransformation)
        
        return len(transformations)