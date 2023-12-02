sum = 0

with open('/Users/martinlejko/Desktop/github/advent-of-code-2023/01/input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        list_of_digits = []
        for char in line:
            if char.isdigit():
                list_of_digits.append(char)
        if len(list_of_digits) > 0:
            if len(list_of_digits) == 1:
                sum += int(list_of_digits[0]+list_of_digits[0])
            else:
                sum += (int(list_of_digits[0] + list_of_digits[-1]))

print(sum)
