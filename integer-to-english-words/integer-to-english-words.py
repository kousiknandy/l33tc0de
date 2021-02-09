class NumberNames:
    def __init__(self, names):
        self.names = names

    def __getitem__(self, index):
        return self.names[index]

class Solution:
    digits = NumberNames(["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",\
                          "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"])
    tens = NumberNames(["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"])
    pow10 = NumberNames(["", "", "Hundred", "Thousand", "Thousand", "Thousand", "Million", "Million", "Million", "Billion"])

    def englify(self, num: str) -> str:
        num = int(num)
        num = str(num)
        l = len(num)
        if l == 1:
            return self.digits[int(num[0])]
        if l == 2:
            if 10 <= int(num) <= 19:
                s = self.digits[int(num)]
            else:
                s = self.tens[int(num[0])]
                if s2 := self.digits[int(num[1])]:
                    s += " " + s2
            return s
        if l == 3:
            s = ""
            if s1 := self.englify(num[:l-2]):
                s += s1 + " " + self.pow10[l-1]
            if s2 := self.englify(num[l-2:]):
                s +=  " " + s2
            return s
        if l >= 4:
            p = (l - 1) // 3 * 3
            s = ""
            if s1 := self.englify(num[:l-p]):
                s += s1 + " " + self.pow10[l-1] 
            if s2 := self.englify(num[l-p:]):
                s +=  " " + s2
            return s
                        
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        return self.englify(str(num))


S = Solution()
for X in [0, 6, 10, 16, 42, 90, 100, 250, 742, 1000, 3742, 10000, 12345, 23742, 33001,  663742, \
          1234567]:
    print(X, S.numberToWords(X))

