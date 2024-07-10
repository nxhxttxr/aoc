with open('day4_ex.txt', 'r') as txt:
    lines = txt.readlines()

i = 0
card, card_tree = 1, 1
card_sum = len(lines)
for i in range(len(lines)):
    j = 0
    winning_numbers = 0

    parts = lines[i].split('|')
    winning_part = parts[0].split(':')[1].strip()
    numbers_part = parts[1].strip()
    winning = list(map(int, winning_part.split()))
    numbers = list(map(int, numbers_part.split()))

    print('-----------------')
    print(f'[Card #{card}]')
    print("Winning:", winning)
    print("Numbers:", numbers)

    for win_num in winning:
        for num in numbers:
            if win_num == num:
                print(f'Found winning number: {num}')
                winning_numbers += 1

    print(f'END OF ORIGINAL CARD #{card}')
    print('-----------------\n')

    card_sum += winning_numbers

    print(f'{i+1}, {i+winning_numbers}\n\n')
    for j in range(i+1, i+winning_numbers+1):
        print(f'>>> J: {j}')
        parts_tree = lines[j].split('|')
        winning_part_tree = parts_tree[0].split(':')[1].strip()
        numbers_part_tree = parts_tree[1].strip()
        winning_tree = list(map(int, winning_part_tree.split()))
        numbers_tree = list(map(int, numbers_part_tree.split()))

        print(f'Scanning card #{j+1} => {winning_tree}\n')
        
        for win_num_tree in winning_tree:
            for num_tree in numbers_tree:
                if win_num_tree == num_tree:
                    print(f'Found winning number: {num_tree}')
                    card_sum += 1

        j += 1
        card_tree += 1


    card += 1

    # 1 -> 1
    # 2 -> 2
    # 3 -> 4
    # 4 -> 8
    # 5 -> 16
    # 6 -> 32

    i += 1

print(f'Total sum: {card_sum}')