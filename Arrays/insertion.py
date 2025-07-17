# =======================================================
# MANUAL INSERTION IN A FIXED SIZE ARRAY (LOW-LEVEL LOGIC)
# =======================================================

# Simulating a static array of fixed size
SIZE = 10
arr = [0] * SIZE  # Pre-allocated array (using zeros)
n = 5  # Current number of meaningful elements

# Initialize the array with sample data
arr[0:n] = [10, 20, 30, 40, 50]

def print_array(arr, n):
    """Prints the active portion of the array."""
    print("Array:", arr[:n])

# 1. Insert at the beginning
def insert_at_beginning(arr, n, value):
    if n >= SIZE:
        print("Overflow: Cannot insert, array is full.")
        return n
    # Shift elements right
    for i in range(n, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = value
    return n + 1

# 2. Insert at a specific index
def insert_at_index(arr, n, value, index):
    if n >= SIZE:
        print("Overflow: Cannot insert, array is full.")
        return n
    if index < 0 or index > n:
        print("Invalid index.")
        return n
    for i in range(n, index, -1):
        arr[i] = arr[i - 1]
    arr[index] = value
    return n + 1

# 3. Insert at the end
def insert_at_end(arr, n, value):
    if n >= SIZE:
        print("Overflow: Cannot insert, array is full.")
        return n
    arr[n] = value
    return n + 1

# Demo for manual insertions
print("Initial fixed-size array:")
print_array(arr, n)

n = insert_at_beginning(arr, n, 5)
print("\nAfter inserting 5 at beginning:")
print_array(arr, n)

n = insert_at_index(arr, n, 25, 3)
print("\nAfter inserting 25 at index 3:")
print_array(arr, n)

n = insert_at_end(arr, n, 99)
print("\nAfter inserting 99 at end:")
print_array(arr, n)


# ===============================================
# INSERTION IN PYTHON LIST (DYNAMIC ARRAY BEHAVIOR)
# ===============================================

# Python lists are dynamic; no manual shifting needed
arr = [10, 20, 30, 40, 50]
print("\nOriginal Python list:", arr)

# 1. Insert at the beginning
arr.insert(0, 5)
print("After inserting 5 at beginning:", arr)

# 2. Insert at a specific index
arr.insert(3, 25)
print("After inserting 25 at index 3:", arr)

# 3. Insert at the end
arr.append(99)
print("After inserting 99 at end:", arr)

# ------------------------------
# Summary:
# - insert(index, value): Inserts at any index, shifts elements right
# - append(value): Adds to end of list
# - Both are built-in methods of Python’s list class
# - Python lists are dynamic arrays (resize automatically)