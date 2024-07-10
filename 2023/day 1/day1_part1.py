if __name__ == "__main__":
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    sum = 0

    with open('day1.txt', 'r') as txt:
        lines = txt.readlines()
        
    for line in lines:
        line_digits = []
        for char in line:
            if char in digits: line_digits.append(int(char))
        
        if len(line_digits) > 1:
            sum += line_digits[0] * 10
            sum += line_digits[-1]
        else: 
            sum += line_digits[0] * 10
            sum += line_digits[0]

    print(sum)
