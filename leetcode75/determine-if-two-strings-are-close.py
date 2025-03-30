from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1 = Counter(word1)
        w2 = Counter(word2)
        if sorted(w1.keys()) != sorted(w2.keys()): return False
        if sorted(w1.values()) != sorted(w2.values()): return False
        return True
