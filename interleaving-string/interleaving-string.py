class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def isInterleave2(s1: str, s2: str, s3: str, mem = {}, depth=0) -> bool:
            n = m = i = j = k = l = 0
            if len(s1) == 0: return s2 == s3
            if len(s2) == 0: return s1 == s3
            if len(s1) + len(s2) != len(s3): return False
            print(" "*depth, s1, s2, s3, mem)
            if (len(s1), len(s2)) in mem: return mem[(len(s1),len(s2))]
            while True:
                a = s1[i] if i < len(s1) else None
                b = s2[j] if j < len(s2) else None
                c = s3[k] if k < len(s3) else None
                if not c and (a or b): return False
                if c == a and c != b:
                    if l in [0, 2]:
                        l = 1
                        n += 1
                    i += 1
                    k += 1
                if c != a and c == b:
                    if l in [0, 1]:
                        l = 2
                        m += 1
                    j += 1
                    k += 1
                if c == a and c == b:
                    o1 = isInterleave2(s1[i:], s2[j+1:], s3[k+1:], mem, depth+1)
                    mem[(len(s1[i:]), len(s2[j+1:]))] = o1
                    if o1:
                        return True
                    o2 = isInterleave2(s1[i+1:], s2[j:], s3[k+1:], mem, depth+1)
                    mem[(len(s1[i+1:]), len(s2[j:]))] = o2
                    return o2
                if c != a and c != b:
                    mem[(len(s1)-i, len(s2)-j)] = False
                    return False
            mem[(len(s1), len(s2))] = True
            return True

        mem = {}
        return isInterleave2(s1, s2, s3, mem)
        
S = Solution()
print(S.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"))
print(S.isInterleave(s1 = "a", s2 = "b", s3 = "a"))
print(S.isInterleave("aabcc","dbbca","aadbbcbcac"))
print(S.isInterleave(
    "cbcccbabbccbbcccbbbcabbbabcababbbbbbaccaccbabbaacbaabbbc",
    "abcbbcaababccacbaaaccbabaabbaaabcbababbcccbbabbbcbbb",
    "abcbcccbacbbbbccbcbcacacbbbbacabbbabbcacbcaabcbaaacbcbbbabbbaacacbbaaaabccbcbaabbbaaabbcccbcbabababbbcbbbcbb"))
print(S.isInterleave(
    "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa",
    "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab",
    "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"))
