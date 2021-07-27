#!/usr/bin/python3
import random
counter = 0
number = random.randint(1,100)

def main():
  print ("Let's play a game. I am thinking of a number between 1 and 100 can you guess it?")
  while True:
    tmpNumber = int(input("Enter a number: "))
    global counter
    counter+=1
    if tmpNumber == number:
        print( "Great you guessed right. Number of tries: " + str(counter) )
        print ("Good job!")
        return
    elif tmpNumber > number:
        print ("Too big!")
    else:
        print ("Too small!")

main()
