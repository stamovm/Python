print ("Hello!")
score = input("Enter Score between 0 and 1: ")
try:
    flscore = float(score)
except:
    print("This not a valid number!")
    quit()

if flscore < 0 :
    print ("score can't be negative")
    quit()

if flscore > 1.0 :
    print ("score can't be bigger tnen 1")
    quit()

if flscore >= .9 :
    print ("Grade is: A")
elif flscore >= .8 :
    print ("Grade is: B")
elif flscore >= .7 :
    print ("Grade is: C")
elif flscore >= .6 :
    print ("Grade is: D")
else :
    print ("Grade is: F")
