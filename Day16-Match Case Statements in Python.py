# x=int(input("enter the value :"))

# match x:
#     case 0:
#         print("this is 0 Case")
#     case 4:
#         print("this is 4 case")
#     case _ if x==90:
#         print("this is equal to 90")
#     case _ if x<=90:
#         print("this is not Equal to 90")
#     case _:
#         print("this is default case")



day = input("Enter the Day: ")

match day:
    case "Monday":
        print("Start of the week")
    case "Tuesday":
        print("Middle of the week (almost)")
    case "Wednesday" | "Thursday" | "Friday":  # Matching multiple cases
        print("Workday")
    case "Saturday" | "Sunday":
        print("Weekend!")
    case _:  # Wildcard case for anything not matched above
        print("Invalid day")


