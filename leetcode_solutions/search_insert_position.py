

def search_position(arr, target):
    left, right = 0, len(arr) - 1

    for x in arr:
        idx = arr[target]

        if arr[idx] == target:
            return arr[idx]

        elif arr[idx] < target:
            left = arr[target] + 1

        else:
            right = arr[target] - 1

    return 1


arr, target = [1, 3, 5, 6], 5
result = search_position(arr, target)
print(result)
