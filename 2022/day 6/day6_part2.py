from collections import Counter


with open('day6.txt', 'r') as txt:
    line = txt.read()


for i in range(len(line)):
    scan = line[i:i+14]
    
    if len(set(scan)) == len(scan):
        print(f'-- Character processed: {i+14} --')
        break
