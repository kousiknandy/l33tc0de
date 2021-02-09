class Solution:
    def infinite_a(self, a):
        count = 1
        while True:
            for c in reversed(a):
                yield c, count
            count += 1
            
    def repeatedStringMatch(self, a: str, b: str) -> int:
        a_seq = self.infinite_a(a)
        matched = False
        for x in reversed(b):
            for y, count in a_seq:
                if x == y:
                    matched = True
                    break
                if matched:
                    if count > 1:
                        return -1
                    
                if count > 2: return -1
        return count


S = Solution()
print(S.repeatedStringMatch("abcd", "cdabcdab"))  # 3
print(S.repeatedStringMatch("abcd", "wxyz"))  # -1
print(S.repeatedStringMatch("abcabcabcabc","abac")) # -1
print(S.repeatedStringMatch("aaac","aac")) # 1
