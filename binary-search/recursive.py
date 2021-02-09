from typing import List

def search(arr: List[int], key: int, offset: int = 0) -> int:
    l = 0
    h = len(arr) - 1
    if len(arr) == 0:
        return None
    if h == 0:
        return offset if arr[0] == key else None
    m = (l + h) // 2
    if arr[m] > key:
        return search(arr[m+1:], key, offset+m)
    elif arr[m] < key:
        return search(arr[:m-1], key, offset)
    else:
        return m+offset

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
    
