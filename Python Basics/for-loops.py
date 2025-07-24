# ------------------------------
# For Loop in Python - Syntax & Examples
# ------------------------------

# General Syntax:
# for variable in iterable:
#     # Code block (indented)

# ------------------------------
# 1. Loop through a list
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

print()  # Spacing

# ------------------------------
# 2. Using range() from 0 to 4
for i in range(5):
    print(i)

print()

# ------------------------------
# 3. Using range() with start and stop: 1 to 5
for i in range(1, 6):
    print(i)

print()

# ------------------------------
# 4. Using range() with step: 0, 2, 4, 6, 8
for i in range(0, 10, 2):
    print(i)