# create global word_to_digit mapping
WORD_TO_DIGIT = {
    "one": "1", "two": "2", "three": "3", "four": "4",
    "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
}

def extract_calibration_value(line, word_to_digit=False):

    # Track the positions of all digits in the line, along with digit value in a list of tuples
    found_digits = []

    # There is probably a better way of writing this, but it will do for now .. it works
    i = 0
    while i < len(line):
        # Check for numeric digit
        if line[i].isdigit():
            found_digits.append((i,line[i]))
            i += 1
            continue

        if not word_to_digit:
            i += 1
            continue

        # Check for spelled-out digits
        for word, digit in WORD_TO_DIGIT.items():
            if line[i:i+len(word)] == word:
                found_digits.append((i,digit))
                # don't increment by len(word) because we want to check for overlapping words
                # e.g., twone3four should find "two" and "one" separately
                i += 1
                break
        else:
            i += 1  # Move to the next character if no match

    if not found_digits:
        return 0

    # Sort the found digits by their position in the line
    found_digits.sort(key=lambda x: x[0])

    first_digit = found_digits[0][1]
    last_digit = found_digits[-1][1]
    return int(first_digit + last_digit)

def sum_calibration_values(lines, word_to_digit=False):
    total_sum = 0
    for line in lines:
        calibration_value = extract_calibration_value(line, word_to_digit=word_to_digit)
        total_sum += calibration_value
    return total_sum

# Example input
input_lines = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen"
]

# Get input from file
with open("Day1Input.txt", "r") as file:
    input_lines = file.readlines()

# Calculate the sum of calibration values - Part 1
result = sum_calibration_values(input_lines)
print(result)

# Calculate the sum of calibration values - Part 2
result = sum_calibration_values(input_lines, word_to_digit=True)
print(result)
