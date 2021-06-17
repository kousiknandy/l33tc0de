import sys

def collatz(l):
    for n in l:
        if n == 1: continue
        yield 3 * n + 1 if n % 2 else n // 2

r = range(1, 1000 if len(sys.argv) < 2 else int(sys.argv[1]))
for _ in range(50 if len(sys.argv) < 3 else int(sys.argv[2])):
    r = collatz(r)
for _ in r: print(_, end=" ")
