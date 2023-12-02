import pandas as pd

with open('/Users/martinlejko/Desktop/github/advent-of-code-2023/01/input2.txt', 'r') as f:
    lines = f.readlines()
    numbers = ['1','2','3','4','5','6','7','8','9','-x-','one','two','three','four','five','six','seven','eight','nine']
    sum = 0

    for line in lines:
        max_index = None
        max_index_num = None
        min_index = None
        min_index_num = None
        for num in numbers:
            try:
                temp_min = line.index(num)
                temp_max = line.rindex(num)
                if min_index == None or temp_min < min_index:
                    min_index = temp_min
                    min_index_num = numbers.index(num) % 10 + 1
                if max_index == None or temp_max > max_index:
                    max_index = temp_max
                    max_index_num = numbers.index(num) % 10 + 1

            except ValueError:
                pass
        if min_index_num != None:
            sum += (int(str(min_index_num) + str(max_index_num)))

print(sum)
