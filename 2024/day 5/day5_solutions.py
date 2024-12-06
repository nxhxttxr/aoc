with open('day5_input.txt', 'r') as inp:
    txt = inp.readlines()

# Format data for processing
pre_rules = []
ordering = []
cur = pre_rules

for line in txt:
    line = line.strip()
    if not line:
        cur = ordering
        continue

    cur.append([int(num) for num in line.replace('|', ',').split(',')]) # replace | with , in the first part and also works for the second part

# Populate dict with better formatted rules
rules = {}
for rule in pre_rules:
    if rule[0] in rules.keys(): rules[rule[0]].append(rule[1])
    else: rules[rule[0]] = [rule[1]]

def part_one(rules: dict, ordering: list) -> int:
    result = 0
    valid_lists = []

    # Check validity
    for order in ordering:
        all_valid = True
        for i in range(len(order)):
            comp = order[i+1:]
            if comp == []: break # end of list

            if order[i] in rules.keys(): 
                bools = [num in rules[order[i]] for num in comp]
                if False in bools: all_valid = False
                #print(bools)
            else: 
                # So in case the number was not present in the rules given, 
                # we must check whenever it is present inside the rules for any of the numbers that came before
                afters = [key for key, values in rules.items() if order[i] in values]
                #print(afters)
                for after in afters:
                    if after in order and order.index(after) < i: all_valid = False

        if all_valid: valid_lists.append(order)

    # Calculate result
    for valid in valid_lists:
        result += valid[(len(valid)-1) // 2] # since all orders are even numbered, I used a formula I thought of in Minecraft (🤷) to find the middle point, adapted for 0-based indexing

    return result

def part_two(rules: dict, ordering: list) -> int:
    result = 0
    invalid_lists = []

    # Check validity
    for order in ordering:
        all_valid = True
        for i in range(len(order)):
            comp = order[i+1:]
            if comp == []: break # end of list

            if order[i] in rules.keys(): 
                bools = [num in rules[order[i]] for num in comp]
                if False in bools: all_valid = False
            else: 
                # So in case the number was not present in the rules given, 
                # we must check whenever it is present inside the rules for any of the numbers that came before
                afters = [key for key, values in rules.items() if order[i] in values]
                
                for after in afters:
                    if after in order and order.index(after) < i: all_valid = False

        if not all_valid: invalid_lists.append(order)

    # Some hours in, I found out that despite the example not following this rule, the actual data set
    # had a rule set for EVERY number - 24 per number to be exact (looping).
    # This means we don't have to actually sort anything, we can figure out the middle point by
    # simply checking which number in the order has exactly (len(order))-1 // 2 numbers of the list in its rule set.
    for order in invalid_lists:
        for num in order:
            match_count = sum(1 for other in order if other in rules[num]) # we find how many of the numbers in the order are included in the rules for <num>

            if match_count == (len(order)-1) // 2: result += num

    return result

print('Result for part 1: ', part_one(rules, ordering))
print('Result for part 2: ', part_two(rules, ordering))