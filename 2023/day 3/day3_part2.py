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

        matches_digits_actual = re.finditer(r'\d+', actual)
        results_digits_actual = [(match.group(), match.start(), match.end()) for match in matches_digits_actual]
        matches_digits_previous = re.finditer(r'\d+', previous)
        results_digits_previous = [(match.group(), match.start(), match.end()) for match in matches_digits_actual]
        
        matches_asterisks = re.finditer(r'\*', actual)
        results_asterisks = [match.start() for match in matches_asterisks]

        for index in results_asterisks:
            print(actual[index])

            num_adj = 0
            for digit_sequence, start, end in results_digits:
                print(f'Cords: {actual[start:end]}')
                if actual[index-1] == actual[end-1]: num_adj += 1
                if actual[index+1] == actual[start]: num_adj += 1
                if previous[index-1] == previous[]
                '''
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
                '''
    i += 1
print(sum)
    

