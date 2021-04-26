class Fancy:

    def __init__(self):
        self.seq = []
        self.ops = [(0, 1, 0)]

    def append(self, val: int) -> None:
        self.seq.append(val)

    def addAll(self, inc: int) -> None:
        self.ops.append((len(self.seq), self.ops[-1][1], self.ops[-1][2]+inc))

    def multAll(self, m: int) -> None:
        self.ops.append((len(self.seq), self.ops[-1][1]*m, self.ops[-1][2]*m))

    def _start(self, idx):
        for i in range(len(self.ops)-1, 0, -1):
            if idx < self.ops[i][0]:
                return i
        return 0
        
    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq): return -1
        print(self.seq, self.ops)
        a = self.seq[idx]
        i = self._start(idx)
        a = self.ops[i][1] * a + self.ops[i][2]
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
