with open('day1.txt', 'r') as txt:
    lines = txt.readlines()

inventory = [[]]
j, highest = 0, 0
for i, line in enumerate(lines):
    if line == "\n" or i+1 == len(lines): 
        if sum(inventory[j]) > highest: highest = sum(inventory[j])

        inventory.append([])
        j += 1
    else: inventory[j].append(int(line.strip()))
    
    

print(f'-- Highest calories: {highest} --')