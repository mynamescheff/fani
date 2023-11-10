import random

# Define card abbreviations and colors
card_names = {
    9: 'Nine', 10: 'Ten', 11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'
}
colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Function to determine the poker hand
def poker_hand(hand):
    values = [card[0] for card in hand]
    suits = [card[1] for card in hand]

    # Check for poker hand combinations
    if all(value == values[0] for value in values):
        return "Royal Flush"
    elif len(set(values)) == 2:
        if values.count(values[0]) in (1, 4):
            return "Four of a Kind"
        else:
            return "Full House"
    elif len(set(suits)) == 1:
        return "Flush"
    elif all(value in values for value in (9, 10, 11, 12, 13)) and len(set(suits)) == 1:
        return "Straight Flush"
    elif all(value in values for value in (9, 10, 11, 12, 13)):
        return "Straight"
    else:
        return "High Card"

# Create a full deck of cards
deck = [(card_names[rank], color) for rank in card_names for color in colors]

# Function to draw 5 random cards
def draw_hand(deck, num_cards=5):
    return random.sample(deck, num_cards)

# Generate and print a random hand
hand = draw_hand(deck)
for card in hand:
    print(f'{card[0]} of {card[1]}')
print(f"Poker Hand: {poker_hand(hand)}")