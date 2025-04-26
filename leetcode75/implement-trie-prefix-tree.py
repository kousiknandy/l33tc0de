from collections import defaultdict


class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        level = self.root
        for c in word:
            if c not in level:
                level[c] = {}
            level = level[c]
        level[None] = None

    def search(self, word: str) -> bool:
        level = self.root
        for c in word:
            if c not in level:
                return False
            level = level[c]
        return None in level

    def startsWith(self, prefix: str) -> bool:
        level = self.root
        for c in prefix:
            if c not in level:
                return False
            level = level[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
