class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) <= 1: return True
        left = 0
        right = len(s) - 1
        deleted = 0
        o_left = o_right = None
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
                if deleted == 1:
                    o_left = left - 1
                    o_right = right + 1
                continue
            if deleted == 0:
                print("mismatch", left, right, s[left:right+1], "trying left char")
                left += 1
                deleted = 1
                continue
            elif deleted == 1:
                print("mismatch", left, right, s[left:right+1], "trying right char")
                if o_left is None:
                    left -= 1
                else:
                    left = o_left - 1
                if o_right is None:
                    right -= 1
                else:
                    right = o_right - 1
                deleted = 2
                continue
            elif deleted == 2:
                print("mismatch", left, right, s[left:right+1], "giving up")
                return False
        return True

S = Solution()
print(S.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))  # True
