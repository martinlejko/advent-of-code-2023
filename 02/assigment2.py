with open('/Users/martinlejko/Desktop/github/advent-of-code-2023/02/input2.txt', 'r') as f:
    max_red = 12
    max_green = 13
    max_blue = 14
    sum = 0

    lines = f.readlines()
    for line in lines:
        line = line.strip().split(':')[1]
        shows = line.strip().split(';')
        min_red = None
        min_green = None
        min_blue = None

        for show in shows:
            block = show.split(',')
            for color in block:
                color = color.strip().split(' ')
                if color[1] == 'red' and (min_red == None or int(color[0]) > min_red):
                    min_red = int(color[0])
                if color[1] == 'green' and (min_green == None or int(color[0]) > min_green):
                    min_green = int(color[0])
                if color[1] == 'blue' and (min_blue == None or int(color[0]) > min_blue):
                    min_blue = int(color[0])
        sum += (min_red * min_green * min_blue)
        
print(sum)


