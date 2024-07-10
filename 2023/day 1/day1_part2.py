import re


spelled_out = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
substrings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sum = 0

with open('day1.txt', 'r') as txt:
    lines = txt.readlines()


for line in lines:
    line_finds = []
    
    for substring in substrings:
        finds = re.finditer(substring, line)

        for find in finds:
            start_index = find.start()
            line_finds.append((substring, start_index))

    sorted_finds = sorted(line_finds, key=lambda x: x[1])
    sorted_list = [item[0] for item in sorted_finds]
        
    if len(sorted_list[0]) > 1:
        for key, value in spelled_out.items():
            if sorted_list[0] == key:
                sum += int(value) * 10
                break
    else: sum += int(sorted_list[0]) * 10
    #print(f"Left: {sorted_list[0]}")

    if len(sorted_list[-1]) > 1:
        for key, value in spelled_out.items():
            if sorted_list[-1] == key:
                sum += int(value)
                break
    else: sum += int(sorted_list[-1])
    #print(f"Right: {sorted_list[-1]}")

    print(f'{line}\nLeft: {sorted_list[0]}\nRight: {sorted_list[-1]}')
    
print(sum)
