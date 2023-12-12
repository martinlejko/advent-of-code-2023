def cardWorth(line, index):
    cardsCount[str(index)] = cardsCount.get(str(index), 0) + 1
    multiplier = cardsCount.get(str(index))

    line = line.strip().split(' ')
    line = line[2:]
    line = ' '.join(line).strip()
    line = line.split('|')
    winNums = line[0].split(' ')
    ourNums = line[1].split(' ')

    numbersFound = 0
    for num in ourNums:
        if num.isnumeric():
            if num in winNums:
                numbersFound+=1
    for i in range(1, numbersFound+1):
        cardsCount[str(index+i)] = cardsCount.get(str(index+i), 0) + multiplier
    


with open('04/example2.txt', 'r') as f:
    table = f.readlines()
    sum = 0
    index = 1
    cardsCount = {}
    for line in table:
        cardWorth(line, index)
        index+=1

for key in cardsCount:
    sum+=cardsCount[key]

print(sum)
