import string


priority_map = dict(zip(string.ascii_letters, range(1, 53)))

with open('day3.txt', 'r') as txt:
    lines = txt.readlines()

sum = 0
for line in lines:
    left = set(line[:int(len(line)/2)])
    right = set(line[int(len(line)/2):])
    
    sum += priority_map[list(left.intersection(right))[0]]


print(f'-- Sum: {sum} --')
