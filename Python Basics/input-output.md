# Input Syntax
input('prompt')
Consider an example to get an integer as input from the user:
int(input("Enter a number:"))
(Here, by default input is treated as a string. Hence, int() converts the input to integer.)

**List elements as input (space seperated)**
First, split the input by ' ', apply int function and group all these inputs in a list. 
Example:
a = [int(x) for x in str(input()).split(" ")]

# Output Syntax
print(object(s), sep=’ ‘ ,end = ‘\n’, file = file, flush = flush)
object(s) - any object as many as you like (will be converted to a string before printing). 
All other parameters are optional. 
sep specifies how to separate objects (by default space). 
end specifies what to print at the end (by default new line). 