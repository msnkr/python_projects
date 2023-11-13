

def search_position(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right: # Don't forget the 
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return None


arr = sorted(["test", "test", "test", "test", "name", "test", "test"])
target = "name"

result = search_position(arr, target)

if result != None:
    print(result)
else:
    print("Target not found")
