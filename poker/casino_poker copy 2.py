import random
import csv
import os
import itertools

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
        fieldnames = ['Round', 'Community Cards'] + [f'Player {i + 1}' for i in range(4)] + ['Win Percentages']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_NONNUMERIC, escapechar=' ', delimiter=',')

        # Write header if the file is empty
        if os.stat(file_path).st_size == 0:
            writer.writeheader()

        # Write results
        writer.writerow(results)

# Function to calculate the percentage chance of winning for each player
def calculate_win_percentages(players_hands, community_cards):
    all_possible_hands = list(itertools.product(*players_hands.values()))
    remaining_community_cards = 5 - len(community_cards)

    win_percentages = {}
    for player, hole_cards in players_hands.items():
        player_hand = hole_cards + community_cards
        remaining_cards = set(itertools.product(card_names.keys(), colors)) - set(player_hand)

        possible_winning_hands = list(itertools.product(*[remaining_cards] * remaining_community_cards))

        player_wins = 0
        total_combinations = len(possible_winning_hands)
        for possible_community_cards in possible_winning_hands:
            combined_hand = player_hand + list(possible_community_cards)
            player_rank = poker_hand(combined_hand)

            # Check if there are other players in the game
            other_players_hands = [hand + list(possible_community_cards) for p, hand in players_hands.items() if p != player]
            if other_players_hands:
                other_players_ranks = [poker_hand(hand) for hand in other_players_hands]
                if player_rank == max(other_players_ranks):
                    player_wins += 1
            else:
                # No other players, player always wins
                player_wins += 1

        win_percentages[player] = (player_wins / total_combinations) * 100 if total_combinations > 0 else 0

    return win_percentages

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
    results = {'Round': round_num, 'Community Cards': ', '.join([f"{card[0]} of {card[1]}" for card in community_cards])}

    # Evaluate player hands
    for player, hole_cards in players_hands.items():
        results[player] = ', '.join([f"{card[0]} of {card[1]}" for card in hole_cards])

# Calculate win percentages
    win_percentages = calculate_win_percentages(players_hands, community_cards)

    # Add win percentages to results dictionary
    results['Win Percentages'] = win_percentages

    # Write results to CSV
    write_to_csv(results, 'poker_results.csv')

    # Display results
    print(f'Round {round_num} Results:')
    print(f'Community Cards: {results["Community Cards"]}')
    for player, hole_cards_str in results.items():
        if player != 'Community Cards' and player != 'Win Percentages':
            print(f'{player}: {hole_cards_str}')
    print(f'Win Percentages: {win_percentages}')

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