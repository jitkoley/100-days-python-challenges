x=int(input("enter the value :"))

match x:
    case 0:
        print("this is 0 Case")
    case 4:
        print("this is 4 case")
    case _:
        print("this is default case")
