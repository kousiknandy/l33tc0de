import sys

def collatz(l):
    """Collatz conjecture, for even n divide by 2, for odd multiply by 3 add 1
    and repeat. Eventually the number will converge to 1. Given a list, apply
    collatz operation and return the next value (ignore 1 as converged already)"""
    for n in l:
        if n == 1: continue
        yield 3 * n + 1 if n % 2 else n // 2

r = range(1, 1000 if len(sys.argv) < 2 else int(sys.argv[1]))
for _ in range(50 if len(sys.argv) < 3 else int(sys.argv[2])):
    # this is collatz curry ... apply collatz repeatedly ...
    # note that we have stacked up generators all the way and
    # none of the below functions execute now they are just
    # chained up like: collatz(collatz(collatz(collatz(....))))
    r = collatz(r)
# if we had enough number rounds the below list should be empty
for _ in r: print(_, end=" ") # otherwise go deeper in generators
