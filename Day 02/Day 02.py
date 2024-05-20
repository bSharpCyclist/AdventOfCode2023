def parse_game_file(filename):
    color_indices = {"red": 0, "green": 1, "blue": 2}

    with open(filename, 'r') as file:
        games = []
        for line in file:
            game_number, sets_str = line.split(": ")
            game_number = int(game_number.split(" ")[1])
            sets = [
                # Create (R, G, B) tuple for each set in the game
                tuple(
                    int(number) if color_indices[color] == i else 0
                    for i in range(3)
                )
                for set_str in sets_str.split("; ")
                for color_str in set_str.split(", ")
                for number, color in [color_str.strip().split(" ")]
            ]
            games.append({"id": game_number, "sets": sets})
        return games

def find_valid_games_sum(games, required_colors):
    # Initialize the sum of valid game IDs
    total_valid_game_ids = 0

    # Iterate through each game in the games list
    for game in games:
        # Check if all sets in the game meet the required colors criteria
        if all(all(color <= req_color for color, req_color in zip(game_set, required_colors)) for game_set in game["sets"]):
            # If valid, add the game's ID to the total sum
            total_valid_game_ids += game["id"]

    # Return the total sum of valid game IDs
    return total_valid_game_ids

# Create function that finds the maximum number colors found in each game. Multiple those numbers together and then sum across all games
def find_max_colors_product_sum(games):
    total_sum = 0
    for game in games:
        max_colors = [max(set[i] for set in game["sets"]) for i in range(3)]
        product = max_colors[0] * max_colors[1] * max_colors[2]
        total_sum += product
    return total_sum
    
games = parse_game_file("Input.txt")
required_colors = (12, 13, 14)

# Part 1
print(find_valid_games_sum(games, required_colors))

# Part 2
print(find_max_colors_product_sum(games))