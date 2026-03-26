# This program simulates drawing 5 cards from a shuffled deck and checks for pairs, triples, flushes, and straights.
# Author: Marcin Kaminski

import requests
from collections import Counter # For counting card values and suits

# Shuffle a new deck
shuffle = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1").json()
deck_id = shuffle["deck_id"]

# Draw 5 cards
draw = requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5").json()
cards = draw["cards"]

print("Your cards:\n")

values = []
suits = []

for card in cards:
    value = card["value"]
    suit = card["suit"]
    print(value, "of", suit)
    values.append(value)
    suits.append(suit)

print("\nChecking your hand...\n")

# Count card values and suits
value_count = Counter(values)
suit_count = Counter(suits)

# Pair
if 2 in value_count.values():
    print("Congratulations! You got a Pair!")

# Triple
if 3 in value_count.values():
    print("Congratulations! You got a Triple!")

# Flush (all same suit)
if len(suit_count) == 1:
    print("Congratulations! All cards are the same suit (Flush)!")

# Check Straight
value_order = {
    "ACE":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,
    "8":8,"9":9,"10":10,"JACK":11,"QUEEN":12,"KING":13
}

numbers = sorted([value_order[v] for v in values])

straight = True
for i in range(4):
    if numbers[i+1] != numbers[i] + 1:
        straight = False

if straight:
    print("Congratulations! You got a Straight!")

# End of program

