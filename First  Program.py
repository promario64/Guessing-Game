import random
from tracemalloc import stop


input("Are you ready to play? 'Y' or 'N' ")

if "Y" or "Yes":
    Value = int(random.randrange(1,100))
    Lives = int(5)
    print("you have 5 lives Good Luck :)")
    print("The numbers are between 1 and 100")

    print("")
    Guess = int(input("What is your guess? "))
   
    #loops untill lives are done
    while Lives >= int(1):
        if Guess == Value: 
            print("You Win :)")
            exit()
        if Guess < Value:
            print("Your Guess is higher then the number ")
            
            Lives -= 1
            print("You Now have " + str(Lives) + " Lives left" )
            print("")
            Guess = int(input("What is your guess? "))
        if Guess > Value:
            print("Your guess is lower then the Number")

            Lives -= 1
            print("You Now have " + str(Lives) + " Lives left" )
            print("")
            Guess = int(input("What is your guess? "))
        
    if Lives == int(0):
        print("Sorry you lose :(")

else:
    exit()

# Didn't Look online to figure it out 1.5 days it took

