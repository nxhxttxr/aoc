with open('day4.txt', 'r') as txt:
    lines = txt.readlines()


sum = 0
first = True
card = 1
for line in lines:
    points = 0

    parts = line.split('|')
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
                points += 1
    
    sum += int(2**(points-1))
    print(f'Points: {int(2**(points-1))}')
    print('-----------------\n')
    card += 1

    # 1 -> 1
    # 2 -> 2
    # 3 -> 4
    # 4 -> 8
    # 5 -> 16
    # 6 -> 32

print(f'Total sum: {sum}')