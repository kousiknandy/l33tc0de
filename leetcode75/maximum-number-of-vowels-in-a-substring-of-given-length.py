class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vows = {'a', 'e', 'i', 'o', 'u'}
        v = 0
        for c in s[:k]: 
            if c in vows: v += 1
        mx = v
        for i in range(len(s)-k):
            if s[i+k] in vows: v += 1
            if s[i] in vows: v -= 1
            mx = max(mx,v)
        return mx 
