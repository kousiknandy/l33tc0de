class Solution:
    def repeated_chars(self, A: str) -> bool:
        map = {}
        for c in A:
            if c in map:
                return True
            else:
                map[c] = 1
        return False
    
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B): return False
        first_mismatch = None
        second_mismatch = None
        for i in range(len(A)):
            if A[i] == B[i]: continue
            if first_mismatch is None:
                first_mismatch = i
            elif second_mismatch is None:
                second_mismatch = i
                if not (A[first_mismatch] == B[second_mismatch] and
                        A[second_mismatch] == B[first_mismatch]):
                    return False
            else:
                return False
        if second_mismatch is None:
            if first_mismatch is None:
                if self.repeated_chars(A):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return True

S = Solution()
print(S.buddyStrings(A = "ab", B = "ba")) # True
print(S.buddyStrings(A = "ab", B = "ab")) # False
print(S.buddyStrings(A = "aaaaaaabc", B = "aaaaaaacb")) # True
print(S.buddyStrings(A = "aa", B = "aa")) # True <- tricky
                
