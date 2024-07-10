from collections import Counter


with open('day6_ex.txt', 'r') as txt:
    lines = txt.readlines()

for line in lines:
    for i in range(len(line)):
        scan = line[i:i+4]
        
        if len(set(scan)) == len(scan):
            print(f'-- Character processed: {i+4} --')
            break
