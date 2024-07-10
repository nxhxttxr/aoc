import re


with open('day3.txt', 'r') as txt:
    lines = txt.readlines()

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sum = 0
i, j = 0, 0

for i in range(len(lines)):
    print(i)
    if i == 0:
        actual = lines[0]
        next = lines[1]

        matches = re.finditer(r'\d+', actual)
        results = [(match.group(), match.start(), match.end()) for match in matches]
        
        for digit_sequence, start, end in results:
            print(f'Seq: {digit_sequence}')
            if actual[start-1] != '.' or actual[end+1] != '.': 
                sum += int(digit_sequence)
                print(f'Found: {digit_sequence}')
            else:
                next_scanable = lines[1][start-1:end+1]

                if bool(re.search(r"[^0-9.]", next_scanable)): 
                    sum += int(digit_sequence) #if it contains anything else rather than numbers and periods
                    print(f'Found: {digit_sequence}')
    elif i == len(lines)-1:
        previous = lines[-2]
        actual = lines[-1]

        matches = re.finditer(r'\d+', actual)
        results = [(match.group(), match.start(), match.end()) for match in matches]
    
        for digit_sequence, start, end in results:
            print(f'Seq: {digit_sequence}')
            if lines[-1][start-1] != '.' or lines[-1][end+1] != '.': 
                sum += int(digit_sequence)
                print(f'Found: {digit_sequence}')
            else:
                next_scanable = lines[-2][start-1:end+1]

                if bool(re.search(r"[^0-9.]", next_scanable)): 
                    sum += int(digit_sequence)
                    print(f'Found: {digit_sequence}')
    else:
        previous = lines[i-1]
        previous = f'.{previous}.'
        print(previous)

        actual = lines[i]
        actual = f'.{actual}.'
        print(actual)
        
        #print(lines[i])
        next = lines[i+1]
        next = f'.{next}.'
        print(next)

        matches = re.finditer(r'\d+', actual)
        results = [(match.group(), match.start(), match.end()) for match in matches]
    
        for digit_sequence, start, end in results:
            '''
            if digit_sequence == "627":
                print('Next chars:')
                print(actual[42:46])
                print(f'Char 42: {actual[42]}')
                print(f'Char 43: {actual[43]}')
                print(f'Char 44: {actual[44]}')
                print(f'Char 45: {actual[45]}')
                print(f'Char 46: {actual[46]}')
                print(f'Char 47: {actual[47]}')
                print(f'Start: {start} / End: {end}')
                print(actual[end])
                print(actual[start-1])
                print(actual[start])
                print(lines[i][start-1:end+1])
                print(actual[start-1:end+1])
                print(actual[end+1])
            print(f'Next char: {actual[end+1]}')
            '''
            if actual[start-1] != '.' or actual[end] != '.': 
                sum += int(digit_sequence)
                print(f'Found: {digit_sequence}')
            else:
                previous_scanable = previous[start-1:end+1]
                next_scanable = next[start-1:end+1]

                if bool(re.search(r"[^0-9.]", previous_scanable)): 
                    sum += int(digit_sequence)
                    print(f'Found: {digit_sequence}')
                if bool(re.search(r"[^0-9.]", next_scanable)): 
                    sum += int(digit_sequence)
                    print(f'Found: {digit_sequence}')
            
        #for char in actual:
            #print(f"Char: {char}")
        
        #break
    i += 1
print(sum)
    

