class Solution(object):
    def near_adj(self, x, y):
        x1, y1 = ord(x), ord(y)
        return abs(x1-y1) <= 1
    
    def removeAlmostEqualCharacters(self, word):
        """
        :type word: str
        :rtype: int
        """
        word = [w for w in word]
        s = 0
        if len(word) == 1: return 0
        for i in range(1, len(word)):
            if self.near_adj(word[i-1], word[i]):
                a = word[i-1]
                b = word[i+1] if i < len(word) - 1 else a
                c = chr(((ord(a) + ord(b)) // 2 + 13 - ord('a')) % 26 + ord('a')) 
                if self.near_adj(word[i-1], c) or (i < len(word) - 1 and self.near_adj(c, word[i+1])):
                    # print(c)
                    c = chr((ord(c)-ord('a')+13)%26+ord('a'))
                # print(a, b,c)
                word[i] = c
                s += 1
        return s
                    
