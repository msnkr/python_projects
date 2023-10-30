def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[idx]:
                idx = j
                
        arr[i], arr[idx] = arr[idx], arr[i]

arr = [2, 6, 5, 1, 4]

selection_sort(arr)
print(arr)