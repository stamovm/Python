
def readInt():
    while True:
        userImp = input ("Enter a number:")
        try:
            istr = int(userImp)
            return istr
        except:
            print("This not a valid number!")

def calculatePay():
    hrs = input("Enter Hours:")
    h = float(hrs)
    rte = input("Enter Rate per hour:")
    r = float(rte)
    overtime = 0.0
    if h > 40:
        overtime = h - 40
        h = 40.0
    pay = h * r +  1.5 * r * overtime
    print(pay)


#-----------------------------------------------------------
#x = readInt()
#print("============> the number is:",x)
#calculatePay()
