import re


with open('day3.txt', 'r') as txt:
    tlines = txt.readlines()

j = 0
lines = []
for line in tlines:
    if j == 10: break
    lines.append(line)
    j += 1

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sum = 0
i = 0

for i in range(len(lines)):
    print(f'We are at line: {i}')
    if i == 0:
        actual = lines[i]
        actual = f'.{actual}.'

        next = lines[i+1]
        next = f'.{next}.'


        matches_digits_actual = re.finditer(r'\d+', actual)
        results_digits_actual = [(match.group(), match.start(), match.end()) for match in matches_digits_actual]
        matches_digits_next = re.finditer(r'\d+', next)
        results_digits_next = [(match.group(), match.start(), match.end()) for match in matches_digits_next]
        
        matches_asterisks = re.finditer(r'\*', actual)
        results_asterisks = [match.start() for match in matches_asterisks]

        num_adj = []
        for asterisk_index in results_asterisks:
            #scanning same line, can only be left or right of the asterisk
            for digit_sequence, start, end in results_digits_actual:
                if actual[asterisk_index-1] == actual[end-1]: 
                    num_adj.append(digit_sequence) #left num*
                    print(f'(actual) Appended: {digit_sequence}')
                if actual[asterisk_index+1] == actual[start]: 
                    num_adj.append(digit_sequence) #right *num
                    print(f'(actual) Appended: {digit_sequence}')


            for digit_sequence, start, end in results_digits_next:
                if asterisk_index-1 in list(range(start, end)):
                    num_adj.append(digit_sequence)
                    print(f'(next-1) Appended: {digit_sequence}')
                    continue

                if asterisk_index in list(range(start, end)):
                    num_adj.append(digit_sequence)
                    print(f'(next) Appended: {digit_sequence}')
                    continue

                if asterisk_index+1 in list(range(start, end)):
                    num_adj.append(digit_sequence)
                    print(f'(next+1) Appended: {digit_sequence}')
                    continue

            if len(num_adj) == 2: sum += int(num_adj[0]) * int(num_adj[1])
    elif i == len(lines)-1:
        previous = lines[i-1]
        previous = f'.{previous}.'
        #print(previous)

        actual = lines[i]
        actual = f'.{actual}.'

        matches_digits_actual = re.finditer(r'\d+', actual)
        results_digits_actual = [(match.group(), match.start(), match.end()) for match in matches_digits_actual]
        matches_digits_previous = re.finditer(r'\d+', previous)
        results_digits_previous = [(match.group(), match.start(), match.end()) for match in matches_digits_previous]
    
        matches_asterisks = re.finditer(r'\*', actual)
        results_asterisks = [match.start() for match in matches_asterisks]
    
        num_adj = []
        for asterisk_index in results_asterisks:
            #scanning same line, can only be left or right of the asterisk
            for digit_sequence, start, end in results_digits_actual:
                #print(f'Cords: {actual[start:end]}')
                if actual[asterisk_index-1] == actual[end-1]: num_adj.append(digit_sequence) #left num*
                if actual[asterisk_index+1] == actual[start]: num_adj.append(digit_sequence) #right *num

            for digit_sequence, start, end in results_digits_previous:
                if asterisk_index-1 in list(range(start, end)):
                    num_adj.append(digit_sequence)
                    print(f'(previous-1) Appended: {digit_sequence}')
                    print(f'Len: {len(num_adj)}')
                    continue

                if asterisk_index in list(range(start, end)):
                    num_adj.append(digit_sequence)
                    print(f'(previous) Appended: {digit_sequence}')
                    continue

                if asterisk_index+1 in list(range(start, end)):
                    num_adj.append(digit_sequence)
                    print(f'(previous+1) Appended: {digit_sequence}')
                    continue

        if len(num_adj) == 2: sum += int(num_adj[0]) * int(num_adj[1])
    else:
        previous = lines[i-1]
        previous = f'.{previous}.'

        actual = lines[i]
        actual = f'.{actual}.' 
        
        next = lines[i+1]
        next = f'.{next}.'

        matches_digits_actual = re.finditer(r'\d+', actual)
        results_digits_actual = [(match.group(), match.start(), match.end()) for match in matches_digits_actual]
        matches_digits_previous = re.finditer(r'\d+', previous)
        results_digits_previous = [(match.group(), match.start(), match.end()) for match in matches_digits_previous]
        matches_digits_next = re.finditer(r'\d+', next)
        results_digits_next = [(match.group(), match.start(), match.end()) for match in matches_digits_next]
        print(f'>>>>>>>>>>>>>>> {results_asterisks}')  
        matches_asterisks = re.finditer(r'\*', actual)
        results_asterisks = [match.start() for match in matches_asterisks]

        num_adj = []
        for asterisk_index in results_asterisks:
            #print(f'Len: {len(num_adj)}')
            #num_adj = []

            #scanning same line, can only be left or right of the asterisk
            for digit_sequence, start, end in results_digits_actual:
                if actual[asterisk_index-1] == actual[end-1]: 
                    num_adj.append(digit_sequence) #left num*
                    print(f'(actual) Appended: {digit_sequence}')
                if actual[asterisk_index+1] == actual[start]: 
                    num_adj.append(digit_sequence) #right *num
                    print(f'(actual) Appended: {digit_sequence}')


            for digit_sequence, start, end in results_digits_previous:
                if asterisk_index-1 in list(range(start, end)):
                    num_adj.append(digit_sequence)
                    print(f'(previous-1) Appended: {digit_sequence}')
                    print(f'Len: {len(num_adj)}')
                    continue

                if asterisk_index in list(range(start, end)):
                    num_adj.append(digit_sequence)
                    print(f'(previous) Appended: {digit_sequence}')
                    continue

                if asterisk_index+1 in list(range(start, end)):
                    num_adj.append(digit_sequence)
                    print(f'(previous+1) Appended: {digit_sequence}')
                    continue
            
            for digit_sequence, start, end in results_digits_next:
                if asterisk_index-1 in list(range(start, end)):
                    num_adj.append(digit_sequence)
                    print(f'(next-1) Appended: {digit_sequence}')
                    continue

                if asterisk_index in list(range(start, end)):
                    num_adj.append(digit_sequence)
                    print(f'(next) Appended: {digit_sequence}')
                    continue

                if asterisk_index+1 in list(range(start, end)):
                    num_adj.append(digit_sequence)
                    print(f'(next+1) Appended: {digit_sequence}')
                    continue
            
            #print(f'-- Len: {len(num_adj)}')
            if len(num_adj) == 2: 
                sum += int(num_adj[0]) * int(num_adj[1])
                print(f'{int(num_adj[0]) * int(num_adj[1])} added to sum')
                num_adj = []
            
    i += 1
print(sum)
    