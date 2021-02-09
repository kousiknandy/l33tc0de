class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lettermap = [0] * 26
        remaining = lambda c: lettermap[ord(c) - ord('a')]
        for c in s:
            lettermap[ord(c) - ord('a')] += 1
        stk = []
        for c in s:
            print(c, stk, end=", ")
            if len(stk) == 0:
                stk.append(c)
                lettermap[ord(c) - ord('a')] -= 1
                print(stk)
                continue
            while stk[-1] > c and remaining(stk[-1]) > 0:
                stk.pop()
                if len(stk) == 0:
                    stk.append(c)
                    lettermap[ord(c) - ord('a')] -= 1
                    break
            else:
                if c not in stk: stk.append(c)
                lettermap[ord(c) - ord('a')] -= 1
                continue                
            if stk[-1] < c:
                if c not in stk: stk.append(c)
                lettermap[ord(c) - ord('a')] -= 1
                continue
            if c not in stk and remaining(c) == 1:
                stk.append(c)
                lettermap[ord(c) - ord('a')] -= 1
            print(stk)
        return "".join(stk)

S = Solution()
print(S.removeDuplicateLetters("cbacdcbc"))  # acdb
print(S.removeDuplicateLetters("ecbacba"))   # eacb
