with open('/Users/martinlejko/Desktop/github/advent-of-code-2023/02/input.txt', 'r') as f:
    max_red = 12
    max_green = 13
    max_blue = 14
    sum = 0

    lines = f.readlines()
    for line in lines:
        line = line.strip().split(':')
        game_num = int(line[0][5:])
        line = line[1]
        shows = line.strip().split(';')
        possible = True

        for show in shows:
            block = show.split(',')
            for color in block:
                color = color.strip().split(' ')
                if color[1] == 'red' and int(color[0]) > max_red:
                    possible = False
                if color[1] == 'green' and int(color[0]) > max_green:
                    possible = False
                if color[1] == 'blue' and int(color[0]) > max_blue:
                    possible = False
        if possible:
            sum += game_num
        

print(sum)


