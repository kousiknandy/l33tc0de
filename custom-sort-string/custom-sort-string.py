class Solution:
    def customSortString(self, S1, T1):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        S = list(S1)
        T = list(T1)
        idx = 0
        for c in S:
            i = 0
            for idx2, d in enumerate(T[idx:]):
                if c == d:
                    #print(idx, idx2, i, c, d, T)
                    T[idx], T[idx2+idx-i] = T[idx2+idx-i], T[idx]
                    idx += 1
                    i += 1
            #print(T)
        return "".join(T)
        
s = Solution()
print(s.customSortString("x", "ax"), "xa")
print(s.customSortString("xa", "axe"), "xae")
print(s.customSortString("xyz", "xyyzx"), "xxyyz")
print(s.customSortString("ba", "aaaaaabbbbb"), "bbbbbaaaaaa")
print(s.customSortString("xyz", "zxy"), "xyz")
print(s.customSortString("x", "axe"), "xae")
