import random
import csv
import os

# Define card abbreviations and colors
card_names = {
    9: 'Nine', 10: 'Ten', 11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'
}
colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Function to determine the poker hand
def poker_hand(hand):
    values = [card[0] for card in hand]
    suits = [card[1] for card in hand]

    # Check for pairs, three of a kind, and four of a kind
    value_counts = {value: values.count(value) for value in set(values)}
    num_pairs = sum(count == 2 for count in value_counts.values())
    num_three_of_a_kind = sum(count == 3 for count in value_counts.values())
    num_four_of_a_kind = sum(count == 4 for count in value_counts.values())

    # Check for straight and royal straight
    is_royal_straight = all(value in values for value in (10, 11, 12, 13, 14))
    is_normal_straight = all(value in values for value in (9, 10, 11, 12, 13))

    # Check for poker hand combinations
    if all(value == values[0] for value in values):
        return "Royal Flush"
    elif num_four_of_a_kind == 1:
        return "Four of a Kind"
    elif num_three_of_a_kind == 1 and num_pairs == 1:
        return "Full House"
    elif len(set(suits)) == 1:
        if is_royal_straight:
            return "Royal Straight Flush"
        elif is_normal_straight:
            return "Straight Flush"
        else:
            return "Flush"
    elif is_royal_straight:
        return "Royal Straight"
    elif is_normal_straight:
        return "Straight"
    elif num_three_of_a_kind == 1:
        return "Three of a Kind"
    elif num_pairs == 2:
        return "Two Pairs"
    elif num_pairs == 1:
        return "Pair"
    else:
        return "High Card"

# Function to write results to a CSV file in the same directory
def write_to_csv(results, filename='poker_results.csv'):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)

    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['Hand', 'Result']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header if the file is empty
        if csvfile.tell() == 0:
            writer.writeheader()

        # Write results
        for result in results:
            writer.writerow(result)

# Create a full deck of cards
deck = [(card_names[rank], color) for rank in card_names for color in colors]

# Function to draw 5 random cards
def draw_hand(deck, num_cards=5):
    return random.sample(deck, num_cards)

# Function to display and save results
def display_and_save_results(results):
    for result in results:
        print(f'Hand: {result["Hand"]}')
        print(f'Result: {result["Result"]}')
        print("------")

    # Write results to CSV in the same directory
    write_to_csv(results)

# Draw and display hands five times
results = []
for _ in range(5):
    hand = draw_hand(deck)
    hand_result = poker_hand(hand)
    results.append({'Hand': ', '.join([f'{card[0]} of {card[1]}' for card in hand]), 'Result': hand_result})

# Display and save results
display_and_save_results(results)
