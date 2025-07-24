# ------------------------------
# Pass by Value vs Pass by Reference in Python
# ------------------------------

# ------------------------------
# 1. Pass by Value (Immutable Types)

def modify(x):
    x = x + 10
    print("Inside function:", x)

a = 5
modify(a)
print("Outside function:", a)

# Output:
# Inside function: 15
# Outside function: 5
# Explanation: 'a' is an integer (immutable), so the change doesn't affect the original value.

print()  # Spacing

# ------------------------------
# 2. Pass by Reference (Mutable Types)

def modify_list(lst):
    lst.append(4)
    print("Inside function:", lst)

numbers = [1, 2, 3]
modify_list(numbers)
print("Outside function:", numbers)

# Output:
# Inside function: [1, 2, 3, 4]
# Outside function: [1, 2, 3, 4]
# Explanation: 'numbers' is a list (mutable), so the original list is modified.