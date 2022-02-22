class Node:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
        
class Trie:
    def __init__(self):
        self.root = Node()
    
    def getIndex(self,letter):
        return ord(letter) - ord("a")

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            indexChar = self.getIndex(char)
            if curr.children[indexChar] == None:
                newNode = Node()
                curr.children[indexChar] = newNode
            curr = curr.children[indexChar]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            indexChar = self.getIndex(char)
            if curr.children[indexChar] == None:
                return False
            curr = curr.children[indexChar]
        return curr.isEnd
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            indexChar = self.getIndex(char)
            if curr.children[indexChar] == None:
                return False
            curr = curr.children[indexChar]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)