# ------------------------------
# Match Statement Syntax (Similar to Switch in Other Languages)
# ------------------------------

# General Syntax:
# match variable:
#     case first_case:
#         statements
#     case second_case:
#         statements
#     case _:
#         default statements

# Notes:
# - No need for 'break' between cases.
# - Only the matching case is executed.
# - The case '_' works as the default fallback.

# ------------------------------
# Example: Day Matching

day = input("Enter Mon/Tue/Wed/...: ")

match day:
    case "Mon":
        print("Monday")
    case "Tue":
        print("Tuesday")
    case "Wed":
        print("Wednesday")
    case "Thu":
        print("Thursday")
    case "Fri":
        print("Friday")
    case "Sat":
        print("Saturday")
    case "Sun":
        print("Sunday")
    case _:
        print("Invalid Input")
