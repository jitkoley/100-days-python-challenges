import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp) 

name = input('Enter your name: ')
#recenttime = time.strftime('%H:%M:%S')
Recenttime = int(time.strftime('%H'))
c= name.capitalize()
print(Recenttime)
if(5<=Recenttime<12):
    print('GOOD MORNING!!',c,'it\'s',timestamp)
elif(12<=Recenttime<17):
    print('GOOD AFTER NOON!!',c,'it\'s',timestamp)
elif(17<=Recenttime<21):
    print("Good EVENING!!",c,'it\'s',timestamp)
else:
    print('GOOD NIGHT!!',c,'it\'s',timestamp)
 



# print('Hii',name,'its',recent time)
# Morning Time : 04:00:00 to 11:59:59
# Afternoon Time : 12:00:00 to 16:59:59
# Evening Time : 17:00:00 to 20:59:59
# Night Time : 21:00:00 to 03:59:59