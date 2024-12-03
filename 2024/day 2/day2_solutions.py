# Read input
with open('day2_input.txt', 'r') as inp:
    txt = inp.readlines()

def part_one(txt: list) -> int:
    # First we check the first condition (all increasing or decreasing)
    result = 0
    for line in txt:
        nums_str = line.split(' ')
        nums_int = []

        for num in nums_str:
            nums_int.append(int(num))

        # Remove duplicates as they are neither an increase or a decrease, thus making it invalid in the next step
        sorted_nums = sorted(set(nums_int))
        sorted_nums_reverse = sorted_nums[::-1]

        if nums_int != sorted_nums and nums_int != sorted_nums_reverse: continue # Invalid report

        evals = 0
        for i in range(len(nums_int)-1):
            if nums_int == sorted_nums:
                if nums_int[i+1] - nums_int[i] <= 3: evals += 1
            elif nums_int == sorted_nums_reverse:
                if nums_int[i] - nums_int[i+1] <= 3: evals += 1
            
        if evals == len(nums_int)-1: result += 1

    return result

def part_two(txt: list) -> int:
    result = 0
    for line in txt:
        nums_str = line.split(' ')
        nums_int = []

        for num in nums_str:
            nums_int.append(int(num))

        j = 0
        while j <= len(nums_int):
            # We make a list by removing an element each time (brute-forcing) - it took me hours, I don't even care to find a more effecient solution. It ran in 21ms for 1000 lines.
            excluded_list = [nums_int[i] for i in range(len(nums_int)) if i != j] if j < len(nums_int) else nums_int
            
            is_ascending = all(1 <= excluded_list[i+1] - excluded_list[i] <= 3 for i in range(len(excluded_list)-1))
            is_descending = all(1 <= excluded_list[i] - excluded_list[i+1] <= 3 for i in range(len(excluded_list)-1))

            if is_ascending or is_descending:
                result += 1
                break
        
            j += 1

    return result

print(f'The result for part 1: {part_one(txt)}')
print(f'The result for part 2: {part_two(txt)}')