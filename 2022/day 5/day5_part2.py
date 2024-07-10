import re


stacks = {
    1: ['N', 'R', 'G', 'P'],
    2: ['J', 'T', 'B', 'L', 'F', 'G', 'D', 'C'],
    3: ['M', 'S', 'V'],
    4: ['L', 'S', 'R', 'C', 'Z', 'P'],
    5: ['P', 'S', 'L', 'V', 'C', 'W', 'D', 'Q'],
    6: ['C', 'T', 'N', 'W', 'D', 'M', 'S'],
    7: ['H', 'D', 'G', 'W', 'P', ],
    8: ['Z', 'L', 'P', 'H', 'S', 'C', 'M', 'V'],
    9: ['R', 'P', 'F', 'L', 'W', 'G', 'Z']
}

with open('day5.txt', 'r') as txt:
    lines = txt.readlines()

# move {amount} from {origin} to {destination}
for line in lines:
    numbers = re.search(r'move (\d+) from (\d+) to (\d+)', line)
    amount, origin, destination = numbers.groups()
    amount, origin, destination = int(amount), int(origin), int(destination)

    moving = stacks[origin][-amount:]
    stacks[destination] += moving
    del stacks[origin][-amount:]
    
for stack in stacks.values():
    print(f'-- {stack[-1]} --')
    
