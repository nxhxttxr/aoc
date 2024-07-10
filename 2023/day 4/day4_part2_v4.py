def unpack_find(finds:dict, find: int):


    return []



with open('day4_ex.txt', 'r') as txt:
    lines = txt.readlines()


finds = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
for i, line in enumerate(lines):
    parts = line.split('|')
    winning_part = parts[0].split(':')[1].strip()
    numbers_part = parts[1].strip()
    winning = set(map(int, winning_part.split()))
    numbers = set(map(int, numbers_part.split()))

    winning_numbers = winning.intersection(numbers)
    
    if len(winning_numbers) > 0:
        print(f"({i + 1}) Winning Numbers: {winning_numbers}")

        #for win_num in winning_numbers:
            #print(win_num)
            
        finds[i+1] = list(range(i+2, i+len(winning_numbers)+2))
        print(finds)


instances = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}
for key, value in finds.items():
    # key = 1
    for find in value:
        instances[find] = instances[find] + 1


print(instances)


# 1:    2, 3, 4, 5
# 2:    3, 4
# 3:    4, 5
# 4:    5
# 5:    0
# 6:    0

# 1: x1
# 2: x2
# 3: x4
# 4: x7
# 5: x6
# 6: x1




# 1: 1
# 2: 1 + 1
# 3: 1 + 3
# 4: 1 + 7
# 5: 1 + 13
# 6: 1
