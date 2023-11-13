

def search_position(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None


arr = sorted([9, 5, 7, 8, 1, 4, 7, 6, 7, 8, 0, 0, 1, 8])
print(arr)
target = 9

result = search_position(arr, target)

if result != None:
    print("{} is at index: {}".format(target, result))
else:
    print("Target not found")
