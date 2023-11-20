import random
import csv
import os

# Define card abbreviations and colors
card_names = {
    2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'
}
colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Function to draw a specified number of random cards
def draw_hand(deck, num_cards=2):
    return random.sample(deck, num_cards)

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

    with open(file_path, 'a', newline='') as csvfile:
        fieldnames = ['Community Cards'] + [f'Player {i + 1}' for i in range(4)]  # Assuming 4 players
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_NONNUMERIC, escapechar=' ', delimiter=',')

        # Write header if the file is empty
        if os.stat(file_path).st_size == 0:
            writer.writeheader()

        # Write results
        writer.writerow(results)

# Function to simulate a round of Texas Hold'em
def simulate_texas_holdem_round(deck, round_number):
    community_cards = []

    # Draw 2 hole cards for each player
    players = {f'Player {i + 1}': draw_hand(deck, 2) for i in range(4)}

    # Save results with only hole cards
    results = {'Community Cards': ''}
    for player, hole_cards in players.items():
        results[player] = f'{", ".join(hole_cards)}'

    # Save results
    write_to_csv(results)

    # Draw the flop: three face-up community cards
    community_cards.extend(draw_hand(deck, 3))

    # Save results after the flop
    results = {'Community Cards': ', '.join(community_cards)}
    for player, hole_cards in players.items():
        total_hand = hole_cards + community_cards
        hand_result = poker_hand(total_hand)
        results[player] = f'{", ".join(total_hand)} ({hand_result})'

    # Save results
    write_to_csv(results)

    # Draw the turn: a single face-up community card
    community_cards.extend(draw_hand(deck, 1))

    # Save results after the turn
    results = {'Community Cards': ', '.join(community_cards)}
    for player, hole_cards in players.items():
        total_hand = hole_cards + community_cards
        hand_result = poker_hand(total_hand)
        results[player] = f'{", ".join(total_hand)} ({hand_result})'

    # Save results
    write_to_csv(results)

    # Draw the river: a single face-up community card
    community_cards.extend(draw_hand(deck, 1))

    # Save results after the river
    results = {'Community Cards': ', '.join(community_cards)}
    for player, hole_cards in players.items():
        total_hand = hole_cards + community_cards
        hand_result = poker_hand(total_hand)
        results[player] = f'{", ".join(total_hand)} ({hand_result})'

    # Save results
    write_to_csv(results)

    # Display round information
    print(f"\nRound {round_number} Results:")
    print(", ".join([f'{player}: {hand_result}' for player, hand_result in results.items()]))

# Main game loop
def main():
    # Create a full deck of cards
    deck = [(card_names[rank], color) for rank in card_names for color in colors]

    # Number of rounds
    num_rounds = 3

    # Play multiple rounds
    for round_num in range(1, num_rounds + 1):
        input(f"\nPress Enter to start Round {round_num}...")
        simulate_texas_holdem_round(deck, round_num)

    print("\nAll rounds completed. Results saved to 'poker_results.csv'.")

if __name__ == "__main__":
    main()
