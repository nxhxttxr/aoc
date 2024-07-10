import re

def find_adjacent_numbers(lines, index):
    previous = f'.{lines[index-1]}.' if index > 0 else None
    actual = f'.{lines[index]}.'
    next = f'.{lines[index+1]}.' if index < len(lines) - 1 else None

    matches_digits_actual = [(match.group(), match.start(), match.end()) for match in re.finditer(r'\d+', actual)]
    matches_digits_previous = [(match.group(), match.start(), match.end()) for match in re.finditer(r'\d+', previous)] if previous else []
    matches_digits_next = [(match.group(), match.start(), match.end()) for match in re.finditer(r'\d+', next)] if next else []

    matches_asterisks = [match.start() for match in re.finditer(r'\*', actual)]

    adjacent_pairs = []

    for asterisk_index in matches_asterisks:
        num_adj = []

        # Check digits in the same line
        for digit_sequence, start, end in matches_digits_actual:
            if actual[asterisk_index-1] == actual[end-1]:  # Left of *
                num_adj.append(digit_sequence)
            if actual[asterisk_index+1] == actual[start]:  # Right of *
                num_adj.append(digit_sequence)

        # Check digits in the previous line
        for digit_sequence, start, end in matches_digits_previous:
            if asterisk_index-1 in range(start, end):  # Below and left of *
                num_adj.append(digit_sequence)
            if asterisk_index in range(start, end):  # Below *
                num_adj.append(digit_sequence)
            if asterisk_index+1 in range(start, end):  # Below and right of *
                num_adj.append(digit_sequence)

        # Check digits in the next line
        for digit_sequence, start, end in matches_digits_next:
            if asterisk_index-1 in range(start, end):  # Above and left of *
                num_adj.append(digit_sequence)
            if asterisk_index in range(start, end):  # Above *
                num_adj.append(digit_sequence)
            if asterisk_index+1 in range(start, end):  # Above and right of *
                num_adj.append(digit_sequence)

        if len(num_adj) == 2:
            adjacent_pairs.append((int(num_adj[0]), int(num_adj[1])))

    return adjacent_pairs

with open('day3.txt', 'r') as txt:
    tlines = txt.readlines()

lines = [line.strip() for line in tlines]  # Read the first 10 lines and strip newlines

total_sum = 0

for i in range(len(lines)):
    adjacent_pairs = find_adjacent_numbers(lines, i)
    for pair in adjacent_pairs:
        total_sum += pair[0] * pair[1]

print(total_sum)