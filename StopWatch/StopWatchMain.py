import time

ClockOn = ''
timeSpent = 0

ClockOn = input("Start StopWatch or Timer (w/t)")

while ClockOn :
    if ClockOn == "w":
        time.sleep(1)
        timeSpent += 1
        print(timeSpent)