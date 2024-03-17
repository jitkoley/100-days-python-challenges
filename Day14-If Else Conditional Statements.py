# a= int(input("enter your Age: "))
# print("your Age is: ",a)

# Conditional operators 
# >, <, >=, <=, ==, !=
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)

# if(a>18):
#     print("you are eligible for voter id card")
# else:
#     print("you are not eligible for voter id card")


num=int(input("enter the number: "))
print(f"the number is {num}")
if(num<0):
    print(f"number {num} is negative")
elif(num==0):
    print(f"the number {num} is equal")
else:
    print(f"the number {num} is positive ")

num1=int(input("Enter the number: "))
if (num1>0):
    print(f"the Number {num1} is Positive")
    if(num1>18):
        print(f"the number greater-than 18")
    elif(num1==18):
        print("the number is equal to 18")
    else:
        print(f"the number is less than 18")
elif(num1==0):
    print("this number is equal to 0")
else:
    print("this number is negative number")

# while True:
#     num1 = int(input("Enter the number (or 'q' to quit): "))

#     # Check if user wants to quit
#     if num1 == 'q':
#         break

#     if num1 > 0:
#         print(f"The number {num1} is Positive")
#         if num1 > 18:
#             print(f"The number is greater than 18")
#         elif num1 == 18:
#             print("The number is equal to 18")
#         else:
#             print(f"The number is less than 18")
#     elif num1 == 0:
#         print("This number is equal to 0")
#     else:
#         print("This number is negative")

# print("Program terminated.")
