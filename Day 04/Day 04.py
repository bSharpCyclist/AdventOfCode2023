import numpy as np

def calculate_points(cards):
    total_points = 0

    # Part 2
    # Initialize an array with number of cards we have
    total_cards = np.ones(len(cards), dtype=int)
    index = 1

    for card in cards:
        # Split the card into card number and numbers - throw away the card number
        _, numbers = card.split(': ')
        
        # Split the numbers into winning numbers and your numbers
        winning_numbers_str, your_numbers_str = numbers.split('|')

        # Convert the numbers to sets of integers
        winning_numbers = set(map(int, winning_numbers_str.split()))
        your_numbers = set(map(int, your_numbers_str.split()))
        
        # Use Set Intersection to find the winning numbers in your numbers, and count them
        winning_count = len(winning_numbers & your_numbers)

        # Calculate the points for the card
        # The points is 2^(n-1) where n is the number of winning numbers
        if winning_count > 0:
            total_points += 2 ** (winning_count - 1)
            # Part 2
            # Important from instructions --> Cards will never make you copy a card past the end of the table!
            # Otherwise, we could be out of array bounds
            total_cards[index:index + winning_count] += total_cards[index - 1]

        index += 1
    
    return total_points, sum(total_cards)

# Example usage
cards = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
]

total_points, total_cards = calculate_points(cards)
print("Total Points:", total_points)
print("Total Cards:", total_cards)

# Load from input file
with open('Input.txt') as file:
    cards = [line.strip() for line in file]

total_points, total_cards = calculate_points(cards)
print("Total Points:", total_points)
print("Total Cards:", total_cards)