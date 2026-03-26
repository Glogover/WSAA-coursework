# This program simulates drawing 5 cards from a shuffled deck and checks for pairs, triples, flushes, and straights.
# Author: Marcin Kaminski

import requests # for making API calls
from collections import Counter # for counting occurrences of card values and suits

# Shuffle a new deck
shuffle = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1").json() # API call to shuffle a new deck
deck_id = shuffle["deck_id"] # Store the deck ID for future API calls

# Draw 5 cards
draw = requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5").json() # API call to draw 5 cards from the shuffled deck
cards = draw["cards"] # Store the drawn cards for processing

print("Your cards:\n") # Print the drawn cards

values = [] # List to store card values for counting pairs, triples, and straights
suits = [] # List to store card suits for counting flushes

for card in cards: # Loop through each drawn card and print its value and suit, while also storing them for later analysis
    value = card["value"] # Get the card value
    suit = card["suit"] # Get the card suit
    print(value, "of", suit) # Print the card's value and suit
    values.append(value) # Add the card value to the list for counting pairs, triples and straights
    suits.append(suit) # Add the card suit to the list for counting flushes


# Count card values and suits
value_count = Counter(values) # Count the occurrences of each card value to check for pairs and triples
suit_count = Counter(suits) # Count the occurrences of each card suit to check for flushes

# Pair
if 2 in value_count.values(): # Check if any card value appears exactly twice, indicating a pair
    print("Congratulations! You got a Pair!")

# Triple
if 3 in value_count.values(): # Check if any card value appears exactly three times, indicating a triple
    print("Congratulations! You got a Triple!")

# Flush (all same suit)
if len(suit_count) == 1: # Check if all cards are of the same suit by verifying that there is only one unique suit in the count
    print("Congratulations! All cards are the same suit (Flush)!")

# Check Straight
value_order = { # Define the order of card values for checking straights
    "ACE":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,
    "8":8,"9":9,"10":10,"JACK":11,"QUEEN":12,"KING":13
}

numbers = sorted([value_order[v] for v in values]) # Convert card values to their corresponding numbers and sort them to check for a straight

straight = True
for i in range(4): # Loop through the sorted card values and check if each card is exactly one value higher than the previous card, which is necessary for a straight
    if numbers[i+1] != numbers[i] + 1: # If any card is not one value higher than the previous card, then it's not a straight
        straight = False

if straight:
    print("Congratulations! You got a Straight!")

# End of program

