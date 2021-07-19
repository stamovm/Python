
def readFlot(msg):
    while True:
        userImp = input (msg)
        try:
            flstr = float(userImp)
            return flstr
        except:
            print("This not a valid number!")

def calculatePay():
    hrs = readFlot("Enter Hours:")
    rate = readFlot("Enter Rate per hour:")
    overtime = 0.0
    if hrs > 40:
        overtime = h - 40
        h = 40.0
    pay = hrs * rate +  1.5 * rate * overtime
    print(pay)


#-----------------------------------------------------------

calculatePay()
