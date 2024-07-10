import string


priority_map = dict(zip(string.ascii_letters, range(1, 53)))

with open('day3.txt', 'r') as txt:
    lines = txt.readlines()

groups = []
sum = 0
group_split = 0
for line in lines:
    if len(groups) == 3:
        #badge = (set(groups[0]) & set(groups[1]) & set(groups[2])).pop()
        #print(badge)
        sum += priority_map[(set(groups[0]) & set(groups[1]) & set(groups[2])).pop()]
        groups = []
    groups.append(line.strip())

sum += priority_map[(set(groups[0]) & set(groups[1]) & set(groups[2])).pop()]


print(f'-- Sum: {sum} --')
