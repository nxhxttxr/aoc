import re


with open('day3_ex.txt', 'r') as txt:
    lines = txt.readlines()

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sum = 0
i, j = 0, 0

for i in range(len(lines)):
    #print(i)
    if i == 0:
        actual = lines[i]
        actual = f'.{actual}.'
        #print(actual)

        next = lines[i+1]
        next = f'.{next}.'
        #print(next)


        matches_digits_actual = re.finditer(r'\d+', actual)
        results_digits_actual = [(match.group(), match.start(), match.end()) for match in matches_digits_actual]
        matches_digits_next = re.finditer(r'\d+', next)
        results_digits_next = [(match.group(), match.start(), match.end()) for match in matches_digits_next]
        
        matches_asterisks = re.finditer(r'\*', actual)
        results_asterisks = [match.start() for match in matches_asterisks]

        print(f'First line asterisks: {results_asterisks}')

        num_adj = []
        for asterisk_index in results_asterisks:
            if len(num_adj) == 2: sum += int(num_adj[0]) * int(num_adj[1])
            num_adj = []

            #scanning same line, can only be left or right of the asterisk
            for digit_sequence, start, end in results_digits_actual:
                #print(f'Cords: {actual[start:end]}')
                if actual[asterisk_index-1] == actual[end]: 
                    num_adj.append(digit_sequence) #left num*
                    print(f'Found adj: {digit_sequence}')
                if actual[asterisk_index+1] == actual[start]: 
                    num_adj.append(digit_sequence) #right *num
                    print(f'Found adj: {digit_sequence}')


            for digit_sequence, start, end in results_digits_next:
                #print(f'Cords: {next[start:end]}')

                if next[asterisk_index-1] == next[start-1] or\
                next[asterisk_index-1] == next[start] or\
                next[asterisk_index-1] == next[start+1] or\
                next[asterisk_index-1] == next[end]:
                    print(f'Found adj: {digit_sequence}')
                    num_adj.append(digit_sequence)
                    continue

                if next[asterisk_index] == next[start-1] or\
                next[asterisk_index] == next[start] or\
                next[asterisk_index] == next[start+1] or\
                next[asterisk_index] == next[end]:
                    print(f'Found adj: {digit_sequence}')
                    num_adj.append(digit_sequence)
                    continue

                if next[asterisk_index+1] == next[start-1] or\
                next[asterisk_index+1] == next[start] or\
                next[asterisk_index+1] == next[start+1] or\
                next[asterisk_index+1] == next[end]:
                    print(f'Found adj: {digit_sequence}')
                    num_adj.append(digit_sequence)
                    continue
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

        print(f'Last line asterisks: {results_asterisks}')
    
        num_adj = []
        for asterisk_index in results_asterisks:
            if len(num_adj) == 2: sum += int(num_adj[0]) * int(num_adj[1])
            num_adj = []

            #scanning same line, can only be left or right of the asterisk
            for digit_sequence, start, end in results_digits_actual:
                #print(f'Cords: {actual[start:end]}')
                if actual[asterisk_index-1] == actual[end]: num_adj.append(digit_sequence) #left num*
                if actual[asterisk_index+1] == actual[start]: num_adj.append(digit_sequence) #right *num

            for digit_sequence, start, end in results_digits_previous:
                #print(f'Cords: {previous[start:end]}')

                if previous[asterisk_index-1] == previous[start-1] or\
                previous[asterisk_index-1] == previous[start] or\
                previous[asterisk_index-1] == previous[start+1] or\
                previous[asterisk_index-1] == previous[end]:
                    num_adj.append(digit_sequence)
                    continue

                if previous[asterisk_index] == previous[start-1] or\
                previous[asterisk_index] == previous[start] or\
                previous[asterisk_index] == previous[start+1] or\
                previous[asterisk_index] == previous[end]:
                    num_adj.append(digit_sequence)
                    continue

                if previous[asterisk_index+1] == previous[start-1] or\
                previous[asterisk_index+1] == previous[start] or\
                previous[asterisk_index+1] == previous[start+1] or\
                previous[asterisk_index+1] == previous[end]:
                    num_adj.append(digit_sequence)
                    continue
    else:
        previous = lines[i-1]
        previous = f'.{previous}.'
        #print(previous)

        actual = lines[i]
        actual = f'.{actual}.'
        #print(actual)
        
        next = lines[i+1]
        next = f'.{next}.'
        #print(next)

        matches_digits_actual = re.finditer(r'\d+', actual)
        results_digits_actual = [(match.group(), match.start(), match.end()) for match in matches_digits_actual]
        matches_digits_previous = re.finditer(r'\d+', previous)
        results_digits_previous = [(match.group(), match.start(), match.end()) for match in matches_digits_previous]
        matches_digits_next = re.finditer(r'\d+', next)
        results_digits_next = [(match.group(), match.start(), match.end()) for match in matches_digits_next]
        
        matches_asterisks = re.finditer(r'\*', actual)
        results_asterisks = [match.start() for match in matches_asterisks]

        print(f'{i} line asterisks: {results_asterisks}')
        if i == 1:
            print('Wokhtgiojiphrtyjiphjiptyhriitp')
            print(results_digits_previous)
            print(results_digits_actual)
            print(results_digits_next)
            for digit_sequence, start, end in results_digits_actual:
                print(f'IF I 1: {digit_sequence}')

        num_adj = []
        for asterisk_index in results_asterisks:
            if i == 1: 
                print(f'i == 1 {previous[asterisk_index-1]}')
                print(f'i == 1 {next[asterisk_index]}')
                for digit_sequence, start, end in results_digits_previous:
                    if previous[asterisk_index-1] == previous[end-1]: print(f'DGT SEQ: {digit_sequence}')
                for digit_sequence, start, end, in results_digits_next:
                    if next[asterisk_index] == next[start+1]: 
                        print(f'DGT SEQ: {digit_sequence}')
                        print(next[start])
                        print(next[start+1])
            elif i == 8:
                print(f'i == 8 {previous[asterisk_index+1]}')
                print(f'i == 8 {next[asterisk_index]}')

            print(f'--Len: {len(num_adj)}--')
            if len(num_adj) == 2: sum += int(num_adj[0]) * int(num_adj[1])
            num_adj = []

            #scanning same line, can only be left or right of the asterisk
            for digit_sequence, start, end in results_digits_actual:
                #print(f'Cords: {actual[start:end]}')
                if actual[asterisk_index-1] == actual[end]: 
                    num_adj.append(digit_sequence) #left num*
                    print(f'Line ({i}): Appended: {digit_sequence}')
                if actual[asterisk_index+1] == actual[start]: 
                    num_adj.append(digit_sequence) #right *num
                    print(f'Line ({i}): Appended: {digit_sequence}')

            print(f'--Len: {len(num_adj)}--')

            for digit_sequence, start, end in results_digits_previous:
                #print(f'Cords: {previous[start:end]}')
                #if digit_sequence == '114':
                    #print(f'>>>>>>>>>>>> {previous[asterisk_index-1]}{previous[asterisk_index]}{previous[asterisk_index+1]}')
                    #print(f'>>>>>>>>>>>> {actual[asterisk_index-1]}{actual[asterisk_index]}{actual[asterisk_index+1]}')
                    #print(f'>>>>>>>>>>>> {next[asterisk_index-1]}{next[asterisk_index]}{next[asterisk_index+1]}')


                if previous[asterisk_index-1] == previous[start] or\
                previous[asterisk_index-1] == previous[start+1] or\
                previous[asterisk_index-1] == previous[end-1]:
                    num_adj.append(digit_sequence)
                    print(f'(previous-1) Line ({i}): Appended: {digit_sequence}')
                    continue

                if previous[asterisk_index] == previous[start] or\
                previous[asterisk_index] == previous[start+1] or\
                previous[asterisk_index] == previous[end-1]:
                    num_adj.append(digit_sequence)
                    print(f'>>>>>>>>>>>>> {previous[start]} >>> {start} >>> {asterisk_index} >>> {end-1} >>> {end}')
                    print(f'>>>>>>>>>>>>> {previous[start+1]}')
                    print(f'>>>>>>>>>>>>> {previous[end-1]}')
                    print(f'(previous) Line ({i}): Appended: {digit_sequence}')
                    continue

                if previous[asterisk_index+1] == previous[start] or\
                previous[asterisk_index+1] == previous[start+1] or\
                previous[asterisk_index+1] == previous[end-1]:
                    num_adj.append(digit_sequence)
                    print(f'(previous+1) Line ({i}): Appended: {digit_sequence}')
                    continue
            print(f'--Len: {len(num_adj)}--')
            for digit_sequence, start, end in results_digits_next:
                #print(f'Cords: {next[start:end]}')

                if digit_sequence == "633":
                    if next[asterisk_index-1] == next[start]: print('next[start]')
                    if next[asterisk_index-1] == next[start+1]: print('next[start+1]')
                    if next[asterisk_index-1] == next[end-1]:
                        print('next[end-1]')
                        num_adj.append(digit_sequence)
                        print(f'>>>>>>>>>>>>> {next[start]} >>> {start} >>> {asterisk_index} >>> {end-1} >>> {end}')
                        print(f'>>>>>>>>>>>>> {next[start+1]}')
                        print(f'>>>>>>>>>>>>> {next[end-1]}')
                        print(f'(next-1) Line ({i}): Appended: {digit_sequence}')
                        print(f'Line ({i}): Appended: {digit_sequence}')
                        continue

                if next[asterisk_index] == next[start] or\
                next[asterisk_index] == next[start+1] or\
                next[asterisk_index] == next[end-1]:
                    num_adj.append(digit_sequence)
                    print(f'>>>>>>>>>>>>> {next[start]} >>> {start} >>> {asterisk_index} >>> {end-1} >>> {end}')
                    print(f'>>>>>>>>>>>>> {next[start+1]}')
                    print(f'>>>>>>>>>>>>> {next[end-1]}')
                    print(f'(next) Line ({i}): Appended: {digit_sequence}')
                    print(f'Line ({i}): Appended: {digit_sequence}')
                    continue

                if next[asterisk_index+1] == next[start] or\
                next[asterisk_index+1] == next[start+1] or\
                next[asterisk_index+1] == next[end-1]:
                    num_adj.append(digit_sequence)
                    print(f'>>>>>>>>>>>>> {next[start]} >>> {start} >>> {asterisk_index} >>> {end-1} >>> {end}')
                    print(f'>>>>>>>>>>>>> {next[start+1]}')
                    print(f'>>>>>>>>>>>>> {next[end-1]}')
                    print(f'(next+1) Line ({i}): Appended: {digit_sequence}')
                    print(f'Line ({i}): Appended: {digit_sequence}')
                    continue
            print(f'--Len: {len(num_adj)}--')
    i += 1
print(sum)
    