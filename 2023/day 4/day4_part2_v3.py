with open('day4_ex.txt', 'r') as txt:
    lines = txt.readlines()


card_sum = len(lines)
sum = {key: [1, []] for key in range(1, len(lines)+1)}

for i in range(len(lines)):
    tmp_found = []
    #print(i)
    parts = lines[i].split('|')
    winning_part = parts[0].split(':')[1].strip()
    numbers_part = parts[1].strip()
    winning = list(map(int, winning_part.split()))
    numbers = list(map(int, numbers_part.split()))

    #print('-----------------')
    #print(f'[Card #{i+1}]')
    #print("Winning:", winning)
    print("Numbers:", numbers)

    for win_num in winning:
        for num in numbers:
            if win_num == num:
                print(f'{i+1} Found: {win_num}')
                sum[i+1][1].append(win_num)

for key, value in sum.items():
    x = len(value)
    for i in range(len(value[1])):
        j = i+2

        sum[j][0] += 1

    #for j in range(len(tmp_found)):
        #print(f'>>> {j+2}')
        #sum[j+2] += 1
                

print(sum)
#print(f'Total sum: {card_sum}')

# 1: 1
# 2: 1 + 1
# 3: 1 + 3
# 4: 1 + 7
# 5: 1 + 13
# 6: 1
