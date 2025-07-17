# ===================================
# LINEAR SEARCH IN PYTHON
# ===================================

# ----------- Using for loop -----------
def linear_search_for(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # Not found

# ----------- Using while loop -----------
def linear_search_while(arr, target):
    i = 0
    while i < len(arr):
        if arr[i] == target:
            return i
        i += 1
    return -1  # Not found


# ----------- Test the functions -----------
arr = [10, 20, 30, 40, 50]

print("Using for loop:", linear_search_for(arr, 30))    # Output: 2
print("Using while loop:", linear_search_while(arr, 60))  # Output: -1

# Summary:
# Linear Search checks each element one by one until the target is found.
# Time Complexity: O(n)
# Space Complexity: O(1)
# Works on unsorted lists.
# Stops at the first match.
# Returns -1 if the element is not found.