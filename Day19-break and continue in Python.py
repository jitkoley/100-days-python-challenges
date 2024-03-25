# i=int(input("Enter the vale : "))
# while True:
#     print(i)
#     i=i+1
#     if(i%50==0):
#         break
#     print("break the loop")


# 
count = int(input("enter the num between 1 to 5"))
while count <= 20:
    if count == 10:
        count += 1
        print("skip 3")
        continue
    print(count)
    count += 1


