# Match Statement Synatax (Switch in other Languages)

match variable:
    case first-case: 
        statements
    case second-case:
        statements
    case _:
        default statements

As you noticed, it doesn't need break in each case. Only the selected case executes. 

Example:
day = input("Enter Mon/Tue/Wed/...:")

match day:
    case "Mon": 
        print("Monday")
    case "Tue":
        print("Tuesday")
    .
    .
    .
    case _:
        print("Invalid Input)
