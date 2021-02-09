class Solution:
    def nearestPalindromic_bak(self, n):
        """
        :type n: str
        :rtype: str
        """
        l = len(n)//2
        hside = n[:l]
        mirr = hside[::-1]
        #print("    ", n, l, n[:l+1], mirr)
        return n[:(len(n)+1)//2] + mirr

    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        l = (len(n) + 1) // 2
        hside = n[:l]
        last = hside[-1]
        minus = c_prev(last)
        plus = c_next(last)
        lesshalf = str(int(hside)-1) #hside[:-1] + minus
        equalhalf = hside
        morehalf = str(int(hside)+1) #hside[:-1] + plus
        x0 = gen_mirr(lesshalf, len(n)%2)
        x1 = gen_mirr(equalhalf, len(n)%2)
        x2 =  gen_mirr(morehalf, len(n)%2)
        choices = [abs(int(x1)-int(n)),
                   abs(int(x0)-int(n)),
                   abs(int(x2)-int(n))]
        print(x0, x1, x2)
        if choices[0] != 0:
            return x1
        if choices[0] == choices[1]:
            return x2
        if choices[0] == choices[2]:
            return x0
        if choices[1] <= choices[2]:
            return x0
        return x2
        
def gen_mirr(s, t):
    if not t:
        return s+s[::-1]
    return s[:-1]+s[::-1]
    
def c_prev(c):
    prev = {"1": "0", "2": "1", "3": "2", "4": "3", "5": "4",
            "6": "5", "7": "6", "8": "7", "9": "8", "0": "0"}
    return prev[c]

def c_next(c):
    next = {"0": "1", "1": "2", "2": "3", "3": "4", "4": "5",
            "5": "6", "6": "7", "7": "8", "8": "9", "9": "9"}
    return next[c]

    
def test(s, n):
    x = s.nearestPalindromic(n)
    print(n, "<->", x)
    
s = Solution()
test(s, "1")
test(s, "9")
test(s, "10")
test(s, "100")
test(s, "123")
test(s, "364542")
test(s, "644722")
test(s, "9999")
test(s, "14342")
test(s, "109")
test(s, "15")
test(s, "90")
test(s, "5")
test(s, "1099")
