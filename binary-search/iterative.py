from typing import List

def search(arr: List[int], key: int) -> int:
    l = 0
    h = len(arr) - 1
    while l <= h:
        m = (l + h) // 2
        if arr[m] > key:
            l = m + 1
        elif arr[m] < key:
            h = m - 1
        else:
            return m
    return None

if __name__ == "__main__":
    a = sorted([1])
    print(search(a, 1)) # 0
    print(search(a, 0)) # None
    print(search(a, 10)) # None
    
    a = sorted([1, 3, 6, 8, 9])
    print(search(a, 6)) # 2
    print(search(a, 7)) # None
    print(search(a, 0)) # None
    print(search(a, 10)) # None
    
    a = sorted([1, 3, 6, 8])
    print(search(a, 3)) # 1
    print(search(a, 7)) # None
    print(search(a, 0)) # None
    print(search(a, 10)) # None
    
