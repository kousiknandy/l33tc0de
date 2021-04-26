import operator

class Fancy:

    def __init__(self):
        self.seq = []
        self.ops = []

    def append(self, val: int) -> None:
        self.seq.append(val)

    def addAll(self, inc: int) -> None:
        self.ops.append((len(self.seq), operator.add, inc))

    def multAll(self, m: int) -> None:
        self.ops.append((len(self.seq), operator.mul, m))

    def _start(self, idx):
        l, r = 0, len(self.ops) - 1
        while l < r:
            m = l + (l + r) // 2
            if self.ops[m][0] == idx:
                return m
            if self.ops[m][0] > idx:
                r = m
            else:
                l = m + 1
        return l
        
    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq): return -1
        a = self.seq[idx]
        for i in range(self._start(idx), len(self.ops)):
            l, o, b = self.ops[i]
            if l <= idx: continue
            a = o(a, b)
        return a % 1_000_000_007

fancy = Fancy()
fancy.append(2)# ;   // fancy sequence: [2]
fancy.addAll(3)#;   // fancy sequence: [2+3] -> [5]
fancy.append(7)#;   // fancy sequence: [5, 7]
fancy.multAll(2)#;  // fancy sequence: [5*2, 7*2] -> [10, 14]
print(fancy.getIndex(0))#; // return 10
fancy.addAll(3)#;   // fancy sequence: [10+3, 14+3] -> [13, 17]
fancy.append(10)#;  // fancy sequence: [13, 17, 10]
fancy.multAll(2)#;  // fancy sequence: [13*2, 17*2, 10*2] -> [26, 34, 20]
print(fancy.getIndex(0))#; // return 26
print(fancy.getIndex(1))#; // return 34
print(fancy.getIndex(2))#; // return 20
