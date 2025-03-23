class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        i, j = 0, 0
        ans = ""
        while i < l1 or j < l2:
            if i < l1: 
                ans += word1[i]
                i += 1
            else:
                ans += word2[j:]
                break
            if j < l2:
                ans += word2[j]
                j += 1
            else:
                ans += word1[i:]
                break
        return ans
