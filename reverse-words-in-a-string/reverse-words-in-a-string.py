class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))

S = Solution()
print(S.reverseWords("hello world"))
print(S.reverseWords("hello     world"))
print(S.reverseWords("  hello world  "))


