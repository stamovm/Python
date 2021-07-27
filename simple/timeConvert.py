#!/usr/bin/python3
def TimeConvert(num):
    hours = num // 60
    minutes = num % 60
    return str(hours) + ":" + str(minutes)
   
print(TimeConvert(45))

