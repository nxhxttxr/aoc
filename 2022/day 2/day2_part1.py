def calc_outcome(enemy: str, player: str):
    guide = {
        'A': 'Y',
        'B': 'Z',
        'C': 'X'
    }

    points_map = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    if guide[enemy] == player: outcome = points_map[player] + 6
    elif (enemy == 'A' and player == 'X') or (enemy == 'B' and player == 'Y') or (enemy == 'C' and player == 'Z'): outcome = points_map[player] + 3
    else: outcome = points_map[player]

    return outcome


with open('day2.txt', 'r') as txt:
    lines = txt.readlines()

sum = 0
for line in lines:
    game = line.strip().split(' ')
    sum += calc_outcome(game[0], game[1])

print(f'-- Sum: {sum} --')




# A/X: Rock
# B/Y: Paper
# C/Z: Scissors
