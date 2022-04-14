arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def binary_search(arr, target):
    start, end = 0, len(arr)-1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid+1
        elif arr[mid] > target:
            end = mid-1
        else:
            return mid
    return -1

print(binary_search(arr, 10))