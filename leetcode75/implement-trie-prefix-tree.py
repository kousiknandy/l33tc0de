from collections import defaultdict


class Trie:

    def __init__(self):
        self.root = {}

    def traverse(self, word, create, prefix):
        level = self.root
        for c in word:
            if c not in level:
                if create:
                    level[c] = {}
                else:
                    return False
            level = level[c]
        if create:
            level[None] = None
            return
        return prefix or (None in level)

    def insert(self, word: str) -> None:
        return self.traverse(word, True, False)

    def search(self, word: str) -> bool:
        return self.traverse(word, False, False)

    def startsWith(self, prefix: str) -> bool:
        return self.traverse(prefix, False, True)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
