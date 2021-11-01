def bubblesort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def selectionsort(arr):
    for i in range(len(arr)-1):
        idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[idx]:
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]
    return arr

def insertionsort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        for j in range(i-1, -1, -1):
            if temp < arr[j]:
                arr[j] = arr[j+1]
            else:
                arr[j] = temp
    return arr

arr = [2,1,4,0,3]
sortedarr = [0,1,2,3,4]
arr1 = [9,6,7,3,5]
arr2 = [8,5,6,2,4]

print(bubblesort(arr))
print(selectionsort(arr1))
print(insertionsort(arr2))