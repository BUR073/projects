import time

speed = int(input("Input Speed (Mph) : "))

miles_time = 1 / speed

time_seconds = miles_time * 3600

x = 1

miles = 0

while x == 1:
    
    time.sleep(time_seconds)

    miles = miles + 1

    print(miles)
    
