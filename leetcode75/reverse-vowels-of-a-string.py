class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = ["a", "e", "i", "o", "u"]
        isvow = lambda x: x.lower() in vow
        s = list(s)
        i, j = 0, len(s)-1
        while i<j:
            while not isvow(s[i]): 
                i += 1
                if i >= j: break
            while not isvow(s[j]): 
                j -= 1
                if j <= i: break
            if i >= j: break
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return "".join(s)
