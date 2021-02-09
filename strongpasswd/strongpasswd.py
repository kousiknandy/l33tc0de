import string

class Solution:
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        lenchanges = 0
        if l < 6:
            lenchanges = 6 -l
        if l > 20:
            lenchanges = l - 20
        lowcase = 0
        for x in s:
            if x in string.lowercase:
                break
        else:
            lowcase = 1
        upcase = 0
        for x in s:
            if x in string.uppercase:
                break
        else:
            upcase = 1
        digits = 0
        for x in s:
            if x in string.digits:
                break
        else:
            digits = 1
