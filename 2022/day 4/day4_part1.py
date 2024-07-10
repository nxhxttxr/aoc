with open('day4.txt', 'r') as txt:
    lines = txt.readlines()

pairs = 0
for line in lines:
    ranges = line.split(',')
    left_range_start = int((ranges[0].split('-'))[0])
    left_range_end = int((ranges[0].split('-'))[1])
    right_range_start = int((ranges[1].split('-'))[0])
    right_range_end = int((ranges[1].split('-'))[1])

    if (left_range_start <= right_range_start and left_range_end >= right_range_end) or (right_range_start <= left_range_start and right_range_end >= left_range_end): pairs += 1

print(f'-- Number of redudant pairs: {pairs} --')
