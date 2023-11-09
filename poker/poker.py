import random

# Define card abbreviations and colors
card_names = {
    2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six',
    7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
    11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'
}
colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Create a full deck of cards
deck = [(card_names[rank], color) for rank in card_names for color in colors]

# Function to draw 5 random cards
def draw_hand(deck, num_cards=5):
    if num_cards > len(deck):
        return None
    hand = random.sample(deck, num_cards)
    for card in hand:
        print(f'{card[0]} of {card[1]}')

# Generate and print a random hand
draw_hand(deck)