with open('day1.txt', 'r') as txt:
    lines = txt.readlines()

inventory = [[]]
j = 0
highest = []
for i, line in enumerate(lines):
    if line == "\n" or i+1 == len(lines): 
        highest.append(sum(inventory[j]))

        inventory.append([])
        j += 1
    else: inventory[j].append(int(line.strip()))
    

highest.sort(reverse=True)

print(f'-- Highest calories: {highest[0] + highest[1] + highest[2]} --')