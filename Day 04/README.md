# My Notes

## Part 1
* Split the card into card number and numbers - throw away the card number.
* Split the numbers into winning numbers and your numbers.
* Convert the numbers to sets of integers.
* Use Set Intersection to find the winning numbers in your numbers, and count them.
* Calculate the points for the card. Points = 2^(n-1) where n is the number of winning numbers

## Part 2
* Keep track of total cards per instructions.
* Initialize array to be [1, 1, 1, ..] up to the initial number of cards
* Increment the appropriate index in the array when copies of cards are earned

## Things Learned
* Replaced np.array([1] * len(cards)) with np.ones(len(cards), dtype=int) for better performance.
* Used total_cards.sum() instead of sum(total_cards) for summing the NumPy array for better performance.

# Original Exercise

![alt text](image.png)

![alt text](image-1.png)

![alt text](image-2.png)


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
            total_cards[index:index+winning_count] += total_cards[index-1]