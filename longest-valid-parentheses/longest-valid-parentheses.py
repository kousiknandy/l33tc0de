class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk = []
        mxl = p = tot = 0
        for i in range(len(s)):
            if s[i] == "(":
                stk.append(i-mxl)
                mxl = 0
                continue
            if len(stk):
                c = stk.pop()
                mxl = max(mxl, i - c + 1)
                if len(stk) == 0:
                    p += mxl
                    mxl = 0
                tot = max(tot, p, mxl)
            else:
                p = 0
        return tot

S = Solution()
print(S.longestValidParentheses("(()()")) # 4
print(S.longestValidParentheses("()()")) # 4
print(S.longestValidParentheses("((())())")) # 8
print(S.longestValidParentheses("((()")) # 2
print(S.longestValidParentheses("))))(())")) # 4
print(S.longestValidParentheses("))))(())))))")) # 4
print(S.longestValidParentheses("))))((")) # 0
print(S.longestValidParentheses("(((())))(())))))")) # 12
print(S.longestValidParentheses("(()(((()")) # 2
