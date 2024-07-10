def calc_outcome(enemy: str, out: str):
    guide = {
        'XA': 3,
        'XB': 1,
        'XC': 2,
        'YA': 4,
        'YB': 5,
        'YC': 6,
        'ZA': 8,
        'ZB': 9,
        'ZC': 7
    }

    outcome = guide[f'{out}{enemy}']
    return outcome


with open('day2.txt', 'r') as txt:
    lines = txt.readlines()

sum = 0
for line in lines:
    game = line.strip().split(' ')
    print(calc_outcome(game[0], game[1]))
    sum += calc_outcome(game[0], game[1])

print(f'-- Sum: {sum} --')




# A: Rock       (1)
# B: Paper      (2)
# C: Scissors   (3)

# X: Lose   (0)
# Y: Draw   (3)
# Z: Win    (6)
