import re
def check_validity(start,num):
    if lines[line_index][start - 1] != '.' and not (lines[line_index][start - 1]).isdigit():
        return True
    if lines[line_index][start + len(num)] != '.' and not (lines[line_index][start + len(num)]).isdigit():
        return True
    for i in range((start - 1), (start + len(num) + 1)):
        if lines[line_index - 1][i] != '.' and not (lines[line_index - 1][i]).isdigit():
            return True
        if lines[line_index + 1][i] != '.' and not (lines[line_index + 1][i]).isdigit():
            return True
    
with open('03/input.txt', 'r') as f:
    lines = f.readlines()

    for i in range(0,len(lines)):
        lines[i] = '.' + lines[i].strip() + '.'
    lines.insert(0, '.'*len(lines[0]))
    lines.append('.'*len(lines[0]))
    line_index = 0
    sum = 0

    for line in lines:
        all_nums = re.findall(r'\d+', line)
        all_nums = list(set(all_nums))
        for num in all_nums:
            starts = []
            for i in range(len(line)):
                if line[i:i+len(num)] == num and not line[i + len(num)].isdigit() and not line[i - 1].isdigit():
                    starts.append(i)
            for start in starts:
                if check_validity(start,num):
                    sum += int(num)
        line_index += 1

    print(sum)
