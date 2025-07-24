# ------------------------------
# Input and Output Syntax in Python
# ------------------------------

# ------------------------------
# INPUT SYNTAX

# General form:
# input('prompt')

# Example: Get an integer as input from the user
num = int(input("Enter a number: "))  # Converts string input to integer
print("You entered:", num)

# Example: Take space-separated integers as list input
# Explanation:
# 1. input() takes input as a string
# 2. .split(" ") splits it into a list of strings by space
# 3. int(x) converts each string to an integer
# 4. list comprehension groups them into a list

a = [int(x) for x in input("Enter numbers (space separated): ").split()]
print("List of numbers entered:", a)

# ------------------------------
# OUTPUT SYNTAX

# General form:
# print(object(s), sep=' ', end='\n', file=file, flush=flush)

# object(s): Any objects to print (converted to strings)
# sep: String inserted between objects (default is space)
# end: String appended after the last value (default is newline)

# Examples:

print("Python", "is", "fun")                     # Default sep=' ', end='\n'
print("Python", "is", "fun", sep='-')            # Custom separator
print("Loading", end='...')                      # Custom end string
print("Done")

# Note: file and flush are used in advanced scenarios like writing to files or forcing immediate output.