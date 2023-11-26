import random

def random_action():
    # Generate a random number between 1 and 3
    random_number = random.randint(1, 3)

    # Perform a random action based on the generated number
    if random_number == 1:
        print("Action 1: Generate a random message.")
        print("Random Message:", ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10)))
    elif random_number == 2:
        print("Action 2: Print a random number.")
        print("Random Number:", random.uniform(1, 10))
    else:
        print("Action 3: Display a random quote.")
        quotes = [
            "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
            "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
            "The way to get started is to quit talking and begin doing. - Walt Disney"
        ]
        print("Random Quote:", random.choice(quotes))

if __name__ == "__main__":
    random_action()