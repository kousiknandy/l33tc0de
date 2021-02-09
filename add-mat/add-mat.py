from typing import List

def add(*arg: List[List[int]]) -> List[List[int]]:
    sumatrix = []
    for z in zip(*arg):
        #print(list(z))
        r = [sum(list(r)) for r in zip(*list(z))]
        #print(r)
        sumatrix.append(r)
    return sumatrix

m1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
m2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
print(add(m1, m2))

