# 1h Countdown Timer

import time


my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    if my_time > 3600 :
        print("Counter can only be up to 3600 seconds. Enter a valid amount.")
        my_time = int(input("Enter the time in seconds: "))
    else:
        seconds = x % 60
        minutes = int(x / 60) % 60
        hour = int(x / 3600)
        print(f'{hour:02}:{minutes:02}:{seconds:02}')
        time.sleep(1)
    

print("TIME'S UP")