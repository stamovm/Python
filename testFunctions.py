#!/usr/bin/python3
import sys
import random


def reverseStr(str):
    revStr = ""
    for i in range(1, len(str) + 1):
        revStr += str[-i]
    return revStr


def abcFunction():
    abc = 123
    print("abc = " + str(abc))


def mathf():
    print(random.random())
    print(random.choice([1, 2, 3, 4, 5, 6]))


def listTest():
    mylist = [1, 2, 3, 4, 5, 6]
    names = ["Jack", "John", "Jim", "Jill", "Alex"]
    print(str(sum(mylist)))


def readFlot(msg):
    while True:
        userImp = input(msg)
        if userImp == 'q':
            quit()
        try:
            flstr = float(userImp)
            return flstr
        except:
            print("This not a valid number! Enter new number or 'q' to quit.")


def calculatePay():
    hrs = readFlot("Enter Hours:")
    rate = readFlot("Enter Rate per hour:")
    overtime = 0.0
    if hrs > 40:
        overtime = h - 40
        h = 40.0
    pay = hrs * rate + 1.5 * rate * overtime
    print(pay)

def TimeConvert(num):
    hours = num // 60
    minutes = num % 60
    return str(hours) + ":" + str(minutes)


print(TimeConvert(145))
#everseStr("1bravo123"))
#abcFunction()
#print((sys.platform + "  ") * 10)
#mathf()
#listTest()
