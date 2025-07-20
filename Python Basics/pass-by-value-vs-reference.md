# Pass by Value vs Pass by Reference in Python

Examples: 

1. Pass by Value (Immutable)
def modify(x):
    x = x + 10
    print("Inside function:", x)

a = 5
modify(a)
print("Outside function:", a)

2. Pass by Reference (Mutable)
def modify_list(lst):
    lst.append(4)
    print("Inside function:", lst)

numbers = [1, 2, 3]
modify_list(numbers)
print("Outside function:", numbers)
