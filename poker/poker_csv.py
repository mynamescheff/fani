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

def write_to_csv(results, filename='poker_results.csv'):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)

    with open(file_path, 'a', newline='') as csvfile:
        fieldnames = ['First Card', 'Second Card', 'Third Card', 'Fourth Card', 'Fifth Card', 'Result']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_NONNUMERIC, escapechar=' ', delimiter=',')

        # Write header if the file is empty
        if os.stat(file_path).st_size == 0:
            writer.writeheader()

        # Write results
        for result in results:
            writer.writerow(result)

# Function to draw 5 random cards as strings
def draw_hand(deck, num_cards=5):
    return [f'{card[0]} {card[1]}' for card in random.sample(deck, num_cards)]

# Function to display and save results
def display_and_save_results(results):
    for result in results:
        print(', '.join(result.values()))
        print("------")

    # Write results to CSV in the same directory
    write_to_csv(results)

# Create a full deck of cards
deck = [(card_names[rank], color) for rank in card_names for color in colors]

# Draw and display hands five times
results = []
for _ in range(5):
    hand = draw_hand(deck)
    hand_result = poker_hand(hand)
    results.append({'First Card': hand[0], 'Second Card': hand[1], 'Third Card': hand[2], 'Fourth Card': hand[3], 'Fifth Card': hand[4], 'Result': hand_result})

# Display and save results
display_and_save_results(results)
