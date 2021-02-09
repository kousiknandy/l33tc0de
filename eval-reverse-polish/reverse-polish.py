from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opmap = {
            "+" : lambda x, y: x + y,
            "-" : lambda x, y: x - y,
            "*" : lambda x, y: x * y,
            "/" : lambda x, y: int(x / y)
            }
        for t in tokens:
            if t in opmap:
                y = stack.pop()
                x = stack.pop()
                z = opmap[t](x, y)
                print(x, t, y, "=", z)
                stack.append(z)
                continue
            stack.append(int(t))
        return stack.pop()

S = Solution()
print(S.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))

