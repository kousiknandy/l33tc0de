class Solution:
    @lru_cache
    def is_palindrome(self, s):
        l= len(s)
        if l < 2: return True
        for i in range(l//2):
            if s[i] != s[l-i-1]: return False
        return True
    
    def nextpart(self, s):
        # print(s)
        r = []
        if len(s) == 0: return None
        if len(s) == 1: return [[s]]
        for i in range(1,len(s)):
            w = s[:i]
            if self.is_palindrome(w):
                t = self.nextpart(s[i:])
                if t:
                    r += [[w] + x for x in t if x]
        if self.is_palindrome(s): r += [[s]]
        return r

    def partition(self, s: str) -> List[List[str]]:
        return self.nextpart(s)
