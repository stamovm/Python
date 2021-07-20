
def readFlot(msg):
    while True:
        userImp = input (msg)
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
        overtime = hrs - 40
        hrs = 40.0
    pay = hrs * rate +  1.5 * rate * overtime
    print(pay)

#-----------------------------------------------------------

calculatePay()
