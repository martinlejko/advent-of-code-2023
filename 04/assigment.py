def cardWorth(line):
    worth = 0
    line = line.strip().split(' ')
    line = line[2:]
    line = ' '.join(line).strip()
    line = line.split('|')
    winNums = line[0].split(' ')
    ourNums = line[1].split(' ')
    for num in ourNums:
        if num.isnumeric():
            if num in winNums:
                if worth == 0:
                    worth += 1
                else:
                    worth = worth + worth
    return int(worth)


with open('04/input.txt', 'r') as f:
    table = f.readlines()
    sum = 0
    for line in table:
        sum+=cardWorth(line)

print(sum)


