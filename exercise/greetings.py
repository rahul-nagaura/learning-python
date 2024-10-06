import time

current_time = time.strftime("%H:%M:%S", time.localtime())
print("Current Time:", current_time)

current_hour = int(time.strftime("%H", time.localtime()))

if 5 < current_hour < 12:
    print('Good Morning')
elif 12 <= current_hour < 18:
    print('Good Afternoon')
else:
    print('Good Night')
