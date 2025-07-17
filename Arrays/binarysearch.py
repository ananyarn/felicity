# ===================================
# BINARY SEARCH IN PYTHON
# ===================================
# Works only on sorted lists (ascending order)

# ----------- Using while loop -----------
def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found

# ----------- Using recursion -----------
def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1  # Target not found

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


# ----------- Test cases -----------
arr = [10, 20, 30, 40, 50, 60, 70]

print("Iterative:", binary_search_iterative(arr, 50))     # Output: 4
print("Recursive:", binary_search_recursive(arr, 25, 0, len(arr) - 1))  # Output: -1


# ===================================
# ✅ SUMMARY
# ===================================

# Binary Search Algorithm:
# - Used to find the position of a target element in a **sorted list**
# - Repeatedly divides the list in half to reduce search space

# ➤ Time Complexity: O(log n)
# ➤ Space Complexity:
#     - Iterative version: O(1)
#     - Recursive version: O(log n) due to recursion stack
# ➤ Only works when the input list is sorted
# ➤ Faster than linear search for large datasets

# Example:
# For arr = [10, 20, 30, 40, 50], searching for 30
# → mid = 2 → arr[2] = 30 → Found!