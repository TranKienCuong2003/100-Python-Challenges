def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        mid = (left + right)

        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1

sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7

index = binary_search(sorted_list, target)
if index != -1:
    print(f"Element found at index: {index}")
else:
    print("Element not found")
