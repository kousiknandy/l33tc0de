def pos(s, c):
    i = 0
    for c1 in s:
        if c == c1:
            return i
        i = i + 1
    return None

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        b = 0
        e = 1
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        max = e - b
        while True:
            if e == len(s):
                if max < (e - b):
                    max = e - b
                    print("  ", s[b:e])
                break
            p = pos(s[b:e], s[e])
            print(" ", s[b:e], s[e], p)
            if p == None:
                e = e + 1
                continue
            if max < (e - b):
                max = e - b
                print("  ", s[b:e])
            b = b + p + 1
            e = e + 1
        return max

S = Solution()
print(S.lengthOfLongestSubstring("au"))
print(S.lengthOfLongestSubstring("abca"))
print(S.lengthOfLongestSubstring("aa"))
print(S.lengthOfLongestSubstring("abcabcd"))
print(S.lengthOfLongestSubstring("pwwabcda"))
