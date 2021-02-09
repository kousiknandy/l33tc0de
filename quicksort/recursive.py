from typing import List

def partition(arr: List[int], low: int, high: int):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        print(" ", arr, i, j)
        if arr[j] > pivot:
            j += 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    print(" ", arr, "*", i)
    return i

def quicksort(arr: List[int], low: int, high: int):
    if low >= high:
        return
    if low + 1 == high:
        if arr[low] > arr[high]:
            arr[low], arr[high] = arr[high], arr[low]
        return
    p = partition(arr, low, high)
    print(" *", low, high, p)
    quicksort(arr, low, p-1)
    quicksort(arr, p+1, high)

arr = [1, 3, 2, 6]
quicksort(arr, 0, len(arr)-1)
print(arr)

arr = [9, 6, 10, 2, 5, 7, 3, 4]
quicksort(arr, 0, len(arr)-1)
print(arr)
