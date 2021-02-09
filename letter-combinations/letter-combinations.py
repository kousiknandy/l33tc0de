from typing import List

class Solution:
    def letters(self, digits):
        lettermap = [[], [], ["a","b","c"], ["d","e", "f"], ["g","h", "i"], ["j","k","l"],
                    ["m","n","o"], ["p","q","r","s"], ["t","u","v"], ["w","x","y","z"]]
        if (len(digits) == 0): yield ""
        else:
            for l in lettermap[ord(digits[0]) - ord("0")]:
                for tail in self.letters(digits[1:]):
                    #print(l, tail)
                    yield l + tail
            
    def letterCombinations(self, digits: str) -> List[str]:
        return list(self.letters(digits))

S = Solution()
print(S.letterCombinations("23"))
