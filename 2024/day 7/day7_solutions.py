from itertools import product

with open('day7_input.txt', 'r') as inp:
    txt = inp.readlines()

# Prepare data
targets, nums = [], []
for line in txt:
    targets.append(int(line.split(':')[0]))
    nums.append([int(x) for x in line.split(':')[1].split()])

def part_one(targets: list, nums: list) -> int:
    result = 0

    for i, target in enumerate(targets):
        line_nums = nums[i]

        if len(line_nums) == 2: # easy enough to write by hand
            if line_nums[0] + line_nums[1] == target: result += target
            elif line_nums[0] * line_nums[1] == target: result += target
        else: # thank God we're only going from left -> right
            computations = []
            for operations in product(['+', '*'], repeat=len(line_nums)-1): # addressing 0-based indexing
                tmp = line_nums[0]

                for num, operation in zip(line_nums[1:], operations):
                    if operation == '+': tmp += num
                    else: tmp *= num

                computations.append(tmp)
            
            result += target if target in computations else 0 # fancy pythonic one-liner to avoid one extra line (I'm a clown)
    
    return result

def concat(nums: list) -> list:
    if len(nums) == 1:
        return [nums]

    res = []
    for other in concat(nums[1:]):
        res.append([nums[0]] + other)

        if len(other) > 0: # we only concat adjacent numbers
            combined = [int(str(nums[0]) + str(other[0]))] + other[1:]
            res.append(combined)

    return res # I hate recursion


def part_two(targets: list, nums: list) -> int:
    result = 0

    for i, target in enumerate(targets):
        line_nums = nums[i]

        if len(line_nums) == 2: # easy enough to write by hand
            if line_nums[0] + line_nums[1] == target: 
                result += target
                print(f'+1 for {target}')
            elif line_nums[0] * line_nums[1] == target: 
                result += target
                print(f'+1 for {target}')
            elif str(line_nums[0]) + str(line_nums[1]) == str(target): 
                result += target
                print(f'+1 for {target}')
        else:
            possible_combinations = concat(line_nums)

            for comb in possible_combinations:
                computations = []

                for operations in product(['+', '*'], repeat=len(comb)-1):
                    tmp = comb[0]

                    for num, operation in zip(comb[1:], operations):
                        if operation == '+': tmp += num
                        else: tmp *= num
                    
                    computations.append(tmp)

                if target in computations:
                    result += target
                    print(f'+1 for {target}')
                    break # we only care about 1 way for this to work

    return result

print('The result for part 1: ', part_one(targets, nums)) # computed in 208ms, which is a "lot", but it's python, give it a break
print('The result for part 2: ', part_two(targets, nums))