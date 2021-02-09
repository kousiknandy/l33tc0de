class FSM(object):
    def __init__(self, statemachine):
        self.machine = statemachine
        self.current = "BEGIN"
        
    def move(self, input):
        try:
            self.current = self.machine[self.current][input]
        except:
            raise
            
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        numbermachine = {
            "BEGIN": {
                " ": "BEGIN",
                "0": "NUM",  "1": "NUM", "2": "NUM",  "3": "NUM", "4": "NUM",
                "5": "NUM",  "6": "NUM", "7": "NUM",  "8": "NUM", "9": "NUM",
                ".": "DEC1", "EOF": "ACCEPT", "+": "NUM", "-": "NUM"
            },
            "NUM": {
                "0": "NUM",  "1": "NUM", "2": "NUM",  "3": "NUM", "4": "NUM",
                "5": "NUM",  "6": "NUM", "7": "NUM",  "8": "NUM", "9": "NUM",
                ".": "DEC1", "e": "EXP1", "EOF": "ACCEPT"
            },
            "DEC1": {
                "0": "DEC2",  "1": "DEC2", "2": "DEC2",  "3": "DEC2", "4": "DEC2",
                "5": "DEC2",  "6": "DEC2", "7": "DEC2",  "8": "DEC2", "9": "DEC2"
            },
            "DEC2": {
                "0": "DEC2",  "1": "DEC2", "2": "DEC2",  "3": "DEC2", "4": "DEC2",
                "5": "DEC2",  "6": "DEC2", "7": "DEC2",  "8": "DEC2", "9": "DEC2",
                "e": "EXP1", "EOF": "ACCEPT" 
            },
            "EXP1": {
                "0": "EXP2",  "1": "EXP2", "2": "EXP2",  "3": "EXP2", "4": "EXP2",
                "5": "EXP2",  "6": "EXP2", "7": "EXP2",  "8": "EXP2", "9": "EXP2",
                "+": "EXP2", "-": "EXP2"
            },
            "EXP2": {
                "0": "EXP2",  "1": "EXP2", "2": "EXP2",  "3": "EXP2", "4": "EXP2",
                "5": "EXP2",  "6": "EXP2", "7": "EXP2",  "8": "EXP2", "9": "EXP2",
                "EOF": "ACCEPT"
            }
        }

        f = FSM(numbermachine)
        for c in s:
            try:
                f.move(c)
            except:
                return False
        else:
            try:
                f.move("EOF")
            except:
                return False
        return True

if __name__ == "__main__":
    testcases = ["0", "1", "1000", "123", "0239", "837893265648926463862649493",
                 "0.234", ".2324", "384632.3259843", "1.2",
                 "321e12", "1.234e19", "1.334e0",
                 "   123", "-100", "-0", "0.", "0.5e-10", "1.2e4.5", "12 3",
                 "1a3", ".1", ".", "+.8", "2e0"]
    for test in testcases:
        s = Solution()
        try:
            s.isNumber(test)
            print test
        except:
            print "! ", test
