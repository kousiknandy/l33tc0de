class Solution:
    def build_trie(self, words):
        for w in words:
            p = self.trie
            # print(p)
            for c in w:
                if c not in p: p[c] = {}
                p = p[c]
                if c not in self.chars: self.chars.append(c)
            else:
                p[None] = None

    def next_word(self, s):
        # print(" ", s)
        if len(s) == 0: return True
        p = self.trie
        st = []
        for i in range(len(s)):
            c = s[i]
            if c not in self.chars: raise
            if c not in p: 
                for j in range(len(st)):
                    i = st.pop()
                    if n := self.next_word(s[i+1:]):
                        return True
                return False
            p = p[c]
            if None in p:
                st.append(i)
        for j in range(len(st)):
            i = st.pop()
            if n := self.next_word(s[i+1:]):
                return True
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.trie = {}
        self.chars = []
        self.build_trie(wordDict)
        # print(self.trie)
        try:
            return self.next_word(s)
        except:
            return False
