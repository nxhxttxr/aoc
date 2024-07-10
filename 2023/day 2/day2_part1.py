import re
from collections import defaultdict
from colorama import Fore, Style

TOTAL_RED = 12
TOTAL_GREEN = 13
TOTAL_BLUE = 14

with open('day2.txt', 'r') as txt:
    lines = txt.readlines()

i = 1
sum = 0

for line in lines:
    # Remove the "Game 1:" part
    clean_string = re.sub(r'^Game \d: ', '', line)

    # Split the string by ';' to get individual game results
    game_results = clean_string.split(';')

    # Dictionary to hold the count of each color
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

    # Output the counts for each color

    if highest_color_counts['blue'] <= TOTAL_BLUE and highest_color_counts['red'] <= TOTAL_RED and highest_color_counts['green'] <= TOTAL_GREEN: 
        sum += i
        print(Fore.GREEN + f'--- GAME #{i} POSSIBLE ---' + Style.RESET_ALL)

    i += 1
    print('\n')
print(sum)
