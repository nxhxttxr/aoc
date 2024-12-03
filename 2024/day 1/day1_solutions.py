# Read input
with open('day1_input.txt', 'r') as inp:
    txt = inp.readlines()

# Initialize lists
nums_left = []
nums_right = []

# Split numbers to the appropriate lists
for line in txt:
    left, right = line.strip().split('   ')[0], line.strip().split('   ')[1]
    
    nums_left.append(left)
    nums_right.append(right)

def part_one(nums_left: list, nums_right: list) -> int:
    # Sort lists (python go brrrr)
    nums_left.sort()
    nums_right.sort()

    # Compare lists and evaluate result
    result = 0

    for i in range(len(nums_left)):
        if int(nums_left[i]) > int(nums_right[i]): result += int(nums_left[i]) - int(nums_right[i])
        elif int(nums_left[i]) < int(nums_right[i]): result += int(nums_right[i]) - int(nums_left[i])

    return result # Is this the most efficient way to do this? No. Did I finish it in sub 10 mins? Yes.

def part_two(nums_left: list, nums_right: list) -> int:
    # Find occurrences of every number in the left list inside the right list
    occurrences = dict()
    result = 0

    #for num in nums_left:
    #    if num in occurrences: result += int(num) * int(occurrences[num])
    #    elif num in nums_right: occurrences[num] = nums_right.count(num)

    for num in nums_left:
        if num in nums_right: result += int(num) * nums_right.count(num)

    return result # Same thing as part_one's result

print(f'The result for part 1: {part_one(nums_left, nums_right)}')
print(f'The result for part 2: {part_two(nums_left, nums_right)}')
