class TrieNode:
    def __init__(self, val, is_end=False):
        self.val = val
        self.children = {}
        self.is_end = is_end

class PrefixTree:

    def __init__(self):
        self.root = TrieNode("", {})

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word.lower():
            if c not in curr.children:
                curr.children[c] = TrieNode(c)
            curr = curr.children[c]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word.lower():
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix.lower():
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return True
        
        