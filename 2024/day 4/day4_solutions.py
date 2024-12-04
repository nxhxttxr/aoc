with open('day4_input.txt', 'r') as inp:
    txt = inp.readlines()
    txt = [line.rstrip('\n') for line in txt]

    # To avoid going out of bounds (IndexError), I'll add some dots in front of and in the back of
    # every line, plus two lines at the top and bottom consisting of only dots. Probably not the best way to do it,
    # but I think it's the most straight-forward.
    txt = [f"....{string}...." for string in txt]
    txt.insert(0, "."*len(txt[0]))
    txt.insert(0, "."*len(txt[0]))
    txt.append("."*len(txt[0]))
    txt.append("."*len(txt[0]))

def part_one(txt: list) -> int:
    result = 0

    # My thought here is to get one of the middle letters of 'XMAS' like 'M' and try to find
    # every 'M' and check around it if there is an 'X' and 'A' and then an 'S' in the appropriate place
    for line_index, line in enumerate(txt):
        if line_index in [0, 1]: continue # speed-up

        for char_index, char in enumerate(line):
            if char != 'M': continue # just to avoid checking every sub-if
            
            if char == 'M' and (line_index == 2 or line_index == len(txt)-3):
                if (line[char_index-1] == 'X' \
                and line[char_index+1] == 'A' \
                and line[char_index+2] == 'S') \
                or (line[char_index-1] == 'A' \
                and line[char_index-2] == 'S' \
                and line[char_index+1] == 'X'): result += 1
            else:
                if (line[char_index-1] == 'X' \
                    and line[char_index+1] == 'A' \
                    and line[char_index+2] == 'S') \
                    or (line[char_index-1] == 'A' \
                    and line[char_index-2] == 'S' \
                    and line[char_index+1] == 'X'): result += 1
                if (txt[line_index-1][char_index] == 'X' \
                    and txt[line_index+1][char_index] == 'A' \
                    and txt[line_index+2][char_index] == 'S') \
                    or (txt[line_index-1][char_index] == 'A' \
                    and txt[line_index-2][char_index] == 'S' \
                    and txt[line_index+1][char_index] == 'X'): result += 1
                if txt[line_index-1][char_index-1] == 'X' \
                    and txt[line_index+1][char_index+1] == 'A' \
                    and txt[line_index+2][char_index+2] == 'S': result += 1
                if txt[line_index-1][char_index+1] == 'X' \
                    and txt[line_index+1][char_index-1] == 'A' \
                    and txt[line_index+2][char_index-2] == 'S': result += 1
                if txt[line_index-1][char_index-1] == 'A' \
                    and txt[line_index-2][char_index-2] == 'S' \
                    and txt[line_index+1][char_index+1] == 'X': result += 1
                if txt[line_index-1][char_index+1] == 'A' \
                    and txt[line_index-2][char_index+2] == 'S' \
                    and txt[line_index+1][char_index-1] == 'X': result += 1
    
    return result

def part_two(txt: list) -> int:
    result = 0
    targets = ['M', 'S']

    # For part two, pretty much nothing changed considering my approach. We'll look for 'A's which are exactly in the middle
    for line_index, line in enumerate(txt):
        if line_index in [0, 1]: continue # speed-up

        for char_index, char in enumerate(line):
            if char != 'A': continue
            
            if txt[line_index-1][char_index-1] in targets and \
                txt[line_index+1][char_index+1] in targets and \
                txt[line_index-1][char_index-1] != txt[line_index+1][char_index+1] and \
                txt[line_index-1][char_index+1] in targets and \
                txt[line_index+1][char_index-1] in targets and \
                txt[line_index-1][char_index+1] != txt[line_index+1][char_index-1]: result += 1
    
    return result

print(f'The result for part 1: {part_one(txt)}')
print(f'The result for part 2: {part_two(txt)}')