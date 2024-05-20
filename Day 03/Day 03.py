import numpy as np
from collections import defaultdict

def get_part_numbers(engine_schematic):
    rows = len(engine_schematic)
    cols = len(engine_schematic[0])

    # Convert to numpy array
    engine_schematic = np.array([list(row) for row in engine_schematic])

    # Define directions, possible directions to move from a point in matrix
    directions = [(-1, -1), (-1, 0), (-1, 1),
                   (0, -1),          (0, 1),
                   (1, -1), (1, 0),  (1, 1)]
    
    part_numbers = []
    symbols_positions = defaultdict(list)

    # If the character is not a digit and not a dot, it is a symbol
    def is_symbol(char):
        return not char.isdigit() and char != '.'

    # Check if the cell is adjacent to a symbol
    def is_adjacent_to_symbol(r, c):
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and is_symbol(engine_schematic[nr, nc]):
                return (nr, nc)
        return None

    # Extract numbers from a row
    def extract_numbers_from_row(row):
        numbers = []
        c = 0
        while c < cols:
            if engine_schematic[row, c].isdigit():
                num_str = ''
                start_c = c
                while c < cols and engine_schematic[row, c].isdigit():
                    num_str += engine_schematic[row, c]
                    c += 1
                numbers.append((int(num_str), row, start_c, c - 1))
            else:
                c += 1
        return numbers

    # Extract numbers from each row and check if they are adjacent to a symbol
    # Add symbol to the dictionary with the connected part numbers
    for r in range(rows):
        numbers = extract_numbers_from_row(r)
        for number, row, start_c, end_c in numbers:
            for c in range(start_c, end_c + 1):
                symbol_position = is_adjacent_to_symbol(row, c)
                if symbol_position:
                    part_numbers.append(number)
                    symbols_positions[symbol_position].append(number)
                    break

    return part_numbers, symbols_positions

# Example input
engine_schematic = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598.."
]

part_numbers, symbols_positions = get_part_numbers(engine_schematic)

# Part 1
print(part_numbers)  # Output should be [467, 35, 633, 617, 592, 755, 664, 598]
print(sum(part_numbers))

# Part 2
print("Symbols and their connected part numbers:", dict(symbols_positions))
gears = {symbol: part_numbers for symbol, part_numbers in symbols_positions.items() if len(part_numbers) == 2}
print(gears)

gear_ratios = [x * y for x, y in gears.values()]
print(sum(gear_ratios))

# Load from input file
with open('Input.txt') as file:
    engine_schematic = [line.strip() for line in file]

# Part 1
part_numbers, symbols_positions = get_part_numbers(engine_schematic)
print(sum(part_numbers))

# Part 2
gears = {symbol: part_numbers for symbol, part_numbers in symbols_positions.items() if len(part_numbers) == 2}
gear_ratios = [x * y for x, y in gears.values()]
print(sum(gear_ratios))