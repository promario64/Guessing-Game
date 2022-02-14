import random


input("Are you ready to play? 'Y' or 'N' ")

if "Y" or "Yes":
    Value = int(random.randrange(1,11))
    Lives = int(5)
    Hidden = 1
    print("you have 5 lives Good Luck :)")

    print(Value)

    print("")
    Guess = int(input("What is your guess? "))
   

    if Guess == Value: 
        print("You Win :)")
        exit()





else:
    exit()
