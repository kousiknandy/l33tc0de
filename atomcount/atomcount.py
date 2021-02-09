class Solution:
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        molstack = []
        atoms = {}
        currscope = {}
        for c in formula:
            if c == '(':
                if currentsymbol:
                    
                molstack.append(currscope)
                currscope = {}
                counter = 0
            if c == ')':
                
