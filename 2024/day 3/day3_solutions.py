import re

with open('day3_input.txt', 'r') as inp:
    txt = inp.readlines()
    inp.seek(0)
    txt_str = inp.read().strip()

def part_one(txt: list) -> int:
    result = 0
    for line in txt:
        matches = re.findall(r"mul\((\d+),(\d+)\)", line)

        for tpl in matches:
            result += int(tpl[0]) * int(tpl[1])
    
    return result

def part_two(txt_str: str) -> int:
    result = 0

    tokens = re.split(r"(do\(\)|don't\(\)|mul\(\d+,\d+\))", txt_str)
    multiplications = []
    after_do = True

    for token in tokens:
        if after_do and re.match(r"mul\((\d+),(\d+)\)", token):
            find = re.match(r"mul\((\d+),(\d+)\)", token)
            multiplications.append((int(find.group(1)), int(find.group(2))))
        elif re.match(r"do\(\)", token): after_do = True
        elif re.match(r"don't\(\)", token): after_do = False
        
    result = sum(x * y for x, y in multiplications)

    return result

print(f'The solution for part 1: {part_one(txt)}')
print(f'The solution for part 2: {part_two(txt_str)}')
