class maxHeap:
    def __init__(self):
        self.ar = []
        self.sz = 0

    def __repr__(self):
        return str(self.sz) + ":" + str(self.ar)
        
    def push(self, el):
        place = self.sz
        self.ar.append(el)
        self.sz += 1
        print(" ", self)
        while True:
            parent = (place - 1) // 2 if place > 0 else 0
            if parent == place:
                break
            if self.ar[parent] < self.ar[place]:
                self.ar[parent], self.ar[place] = self.ar[place], self.ar[parent]
                print(" ", self)
            else:
                break
            place = parent
        print(self)

    def pop(self):
        if self.sz == 0:
            return None
        place = 0
        el = self.ar[place]
        last = self.ar.pop()
        self.sz -= 1
        if self.sz > 0:
            self.ar[place] = last 
        while True:
            left = 2 * place + 1
            right = 2 * place + 2
            largest = place
            if left < self.sz:
                if self.ar[left] > self.ar[place]:
                    largest = left
            if right < self.sz:
                if self.ar[right] > self.ar[place]:
                    largest = right if self.ar[right] > self.ar[left] else left
            if place == largest:
                break
            self.ar[largest], self.ar[place] = self.ar[place], self.ar[largest]
            print(" ", self)
            place = largest
        print(self)
        return el

def counter(start = 0):
    while True:
        yield start
        start += 1
    
class Solution:
    def countInversions(self, A):
        counter = 0
        for i in range(len(A)):
            for j in range(len(A)-1):
                if A[j] > A[j+1]:
                    A[j], A[j+1] = A[j+1], A[j]
                    counter += 1
        return counter

# H = maxHeap()
# C = counter()
# H.push((20, next(C)))
# H.push((10, next(C)))
# H.push((15, next(C)))
# H.push((5, next(C)))
# H.push((25, next(C)))
# H.push((30, next(C)))
# H.push((0, next(C)))
# x = H.pop()
# print(x)
# x = H.pop()
# print(x)
# x = H.pop()
# print(x)
# x = H.pop()
# print(x)
# x = H.pop()
# print(x)
# x = H.pop()
# print(x)
# x = H.pop()
# print(x)

S = Solution()
print(S.countInversions([ 84, 2, 37, 3, 67, 82, 19, 97, 91, 63, 27, 6, 13, 90, 63, 89, 100, 60, 47, 96, 54, 26, 64, 50, 71, 16, 6, 40, 84, 93, 67, 85, 16, 22, 60 ]))
print(S.countInversions([2, 4, 1, 3, 5]))

