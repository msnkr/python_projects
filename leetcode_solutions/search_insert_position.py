

def search_position(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


arr, target = [1, 3, 5, 6], 5
result = search_position(arr, target)
print(result)
