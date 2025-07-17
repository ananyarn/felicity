# =====================================================
# MANUAL DELETION IN A FIXED SIZE ARRAY (LOW-LEVEL LOGIC)
# =====================================================

# Simulating a static array with fixed size
SIZE = 10
arr = [0] * SIZE
n = 6
arr[0:n] = [10, 20, 30, 40, 50, 60]

def print_array(arr, n):
    """Prints the active elements of the array."""
    print("Array:", arr[:n])

# 1. Delete from the beginning
def delete_from_beginning(arr, n):
    if n == 0:
        print("Underflow: Array is empty.")
        return n
    for i in range(1, n):
        arr[i - 1] = arr[i]
    arr[n - 1] = 0  # Optional: clear last element
    return n - 1

# 2. Delete from a specific index
def delete_from_index(arr, n, index):
    if n == 0:
        print("Underflow: Array is empty.")
        return n
    if index < 0 or index >= n:
        print("Invalid index.")
        return n
    for i in range(index + 1, n):
        arr[i - 1] = arr[i]
    arr[n - 1] = 0
    return n - 1

# 3. Delete from the end
def delete_from_end(arr, n):
    if n == 0:
        print("Underflow: Array is empty.")
        return n
    arr[n - 1] = 0
    return n - 1

# Demo for manual deletions
print("Initial fixed-size array:")
print_array(arr, n)

n = delete_from_beginning(arr, n)
print("\nAfter deleting from beginning:")
print_array(arr, n)

n = delete_from_index(arr, n, 2)
print("\nAfter deleting from index 2:")
print_array(arr, n)

n = delete_from_end(arr, n)
print("\nAfter deleting from end:")
print_array(arr, n)


# ==================================================
# DELETION IN PYTHON LIST (DYNAMIC ARRAY BEHAVIOR)
# ==================================================

arr = [10, 20, 30, 40, 50, 60]
print("\nPython list before deletion:", arr)

# 1. Delete from the beginning
arr.pop(0)
print("After deleting from beginning:", arr)

# 2. Delete from a specific index
arr.pop(2)  # Removes element at index 2
print("After deleting from index 2:", arr)

# 3. Delete from the end
arr.pop()
print("After deleting from end:", arr)

# -----------------------------------------
# Summary:
# - arr.pop(index) → Deletes element at the given index and returns it
# - arr.pop() → Deletes the last element (default behavior)
# - arr.remove(value) → Deletes the first occurrence of the value (not index-based)
# - Python lists are dynamic: memory and shifting are handled internally
