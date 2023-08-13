def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2

        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1  


arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23

index = binary_search(arr, target)
if index != -1:
    print("Target found at index:", index)
else:
    print("Target element not found in the array.")