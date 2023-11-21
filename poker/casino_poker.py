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
        fieldnames = ['Community Cards'] + [f'Player {i + 1}' for i in range(4)]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_NONNUMERIC, escapechar=' ', delimiter=',')

        # Write header if the file is empty
        if os.stat(file_path).st_size == 0:
            writer.writeheader()

        # Write results
        writer.writerow(results)

# Function to simulate a round of Texas Hold'em
def simulate_texas_holdem_round(deck, round_num, players_hands=None, community_cards=None):
    if not players_hands:
        # Draw hole cards for each player only if not provided
        players_hands = {f'Player {i + 1}': draw_hand(deck, 2) for i in range(4)}

    # Draw community cards only if not provided or if it's the first round
    if not community_cards or round_num == 1:
        community_cards = draw_hand(deck, 3)
    elif round_num == 2:
        # Draw one additional community card for the second round
        community_cards.append(deck.pop())
    elif round_num == 3:
        # Draw the final additional community card for the third round
        community_cards.append(deck.pop())

    # Results dictionary
    results = {'Community Cards': ', '.join([f"{card[0]} of {card[1]}" for card in community_cards])}

    # Evaluate player hands
    for player, hole_cards in players_hands.items():
        results[player] = ', '.join([f"{card[0]} of {card[1]}" for card in hole_cards])

    # Write results to CSV
    write_to_csv(results, f'round_{round_num}_results.csv')

    # Display results
    print(f'Round {round_num} Results:')
    print(f'Community Cards: {results["Community Cards"]}')
    for player, hole_cards_str in results.items():
        if player != 'Community Cards':
            print(f'{player}: {hole_cards_str}')

    return players_hands, community_cards

# Function to run the Texas Hold'em simulation
def main():
    deck = [(card_names[rank], color) for rank in card_names for color in colors]

    # Initialize players' hands and community cards
    players_hands, community_cards = None, None

    for round_num in range(1, 4):
        players_hands, community_cards = simulate_texas_holdem_round(deck, round_num, players_hands, community_cards)
        input('Press Enter to continue...')

if __name__ == "__main__":
    main()