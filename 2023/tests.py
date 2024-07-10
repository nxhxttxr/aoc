import re
from collections import defaultdict

# Input string
input_string = "Game 1: 2 blue, 4 green; 7 blue, 1 red, 14 green; 5 blue, 13 green, 1 red; 1 red, 7 blue, 11 green"

# Remove the "Game X:" part (where X is any number)
clean_string = re.sub(r'Game \d+: ', '', input_string)

# Split the string by ';' to get individual game results
game_results = clean_string.split(';')

# Dictionary to hold the highest count of each color
highest_color_counts = defaultdict(int)

# Process each game result
for result in game_results:
    # Dictionary to hold the count of each color for the current game
    game_color_counts = defaultdict(int)
    
    # Split the result by ',' to get individual color entries
    entries = result.split(',')
    for entry in entries:
        # Extract the number and color
        match = re.search(r'(\d+)\s+(\w+)', entry.strip())
        if match:
            number = int(match.group(1))
            color = match.group(2)
            # Update the count for the current game
            game_color_counts[color] = max(game_color_counts[color], number)
    
    # Update the highest counts for each color
    for color, count in game_color_counts.items():
        highest_color_counts[color] = max(highest_color_counts[color], count)

# Output the highest counts for each color
print("Highest count of blue:", highest_color_counts['blue'])
print("Highest count of red:", highest_color_counts['red'])
print("Highest count of green:", highest_color_counts['green'])
