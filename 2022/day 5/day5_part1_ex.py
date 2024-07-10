import re


stacks = {
    1: ['Z', 'N'],
    2: ['M', 'C', 'D'],
    3: ['P']
}

with open('day5_ex.txt', 'r') as txt:
    lines = txt.readlines()

# move {amount} from {origin} to {destination}
for line in lines:
    numbers = re.search(r'move (\d+) from (\d+) to (\d+)', line)
    amount, origin, destination = numbers.groups()
    amount, origin, destination = int(amount), int(origin), int(destination)

    for i in range(amount):
        moving = stacks[origin].pop()
        stacks[destination].append(moving)
    
for stack in stacks.values():
    print(f'-- {stack[-1]} --')
    
