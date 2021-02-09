class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def minDistance(word1: str, word2: str, memo) -> int:
            l1 = len(word1)
            l2 = len(word2)
            if not l1: return l2
            if not l2: return l1
            if memo[l1][l2] is not None: return memo[l1][l2]
            if word1[l1-1] == word2[l2-1]: return minDistance(word1[:-1], word2[:-1], memo)
            o1 = 1 + minDistance(word1, word2[:-1], memo) # insert
            o2 = 1 + minDistance(word1[:-1], word2[:-1], memo) # replace
            o3 = 1 + minDistance(word1[:-1], word2, memo) # delete
            memo[l1][l2] = min(o1, o2, o3)
            return memo[l1][l2]

        memo = [[None for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        return minDistance(word1, word2, memo)

S = Solution()
print(S.minDistance(word1 = "horse", word2 = "ros"))
print(S.minDistance(word1 = "intention", word2 = "execution"))

