# ------------------------------
# Branching Statements in Python - Syntax & Example
# ------------------------------

# General Syntax:
# if condition1:
#     statements to execute
# elif condition2:
#     statements to execute
# else:
#     statements to execute

# ------------------------------
# Example: Find the biggest number among a, b, and c

a = 10
b = 25
c = 15

if a >= b and a >= c:
    print("The biggest number is:", a)
elif b >= a and b >= c:
    print("The biggest number is:", b)
else:
    print("The biggest number is:", c)