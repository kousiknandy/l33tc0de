from typing import List

class Solution:
    def genCombinations(self, left, right, depth = 0):
        #print(" "*depth, left, right)
        if left == 0:
            if right:
                yield ")" * right
            return
        if left > right: return
        if right == 0: return
        for tail in self.genCombinations(left - 1, right, depth+1):
            yield "("  + tail
        for tail in self.genCombinations(left, right - 1, depth+1):
            yield ")"  + tail
                
    def generateParenthesis(self, n: int) -> List[str]:
        return list(self.genCombinations(n, n))

S = Solution()
for i in range(8):
    print(S.generateParenthesis(i))

