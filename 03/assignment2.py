def is_valid_position(row, col, max_row, max_col):
    return 0 <= row < max_row and 0 <= col < max_col

def calculate_gear_ratios(engine_map):
    rows = len(engine_map)
    cols = len(engine_map[0])

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    gear_ratios = []

    for i in range(rows):
        for j in range(cols):
            if engine_map[i][j] == '*':
                adjacent_numbers = []
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    number = ""
                    while is_valid_position(x, y, rows, cols) and engine_map[x][y].isdigit():
                        number += engine_map[x][y]
                        x, y = x + dx, y + dy
                    if number and len(adjacent_numbers) < 2:
                        adjacent_numbers.append(int(number))

                if len(adjacent_numbers) == 2:
                    gear_ratio = adjacent_numbers[0] * adjacent_numbers[1]
                    gear_ratios.append(gear_ratio)

    return sum(gear_ratios)

def read_engine_schematic(file_path):
    with open(file_path, 'r') as file:
        engine_map = [line.strip() for line in file]
    return engine_map

def main():
    file_path = 'example2.txt'  # Change this to the path of your engine schematic file
    engine_map = read_engine_schematic(file_path)
    total_gear_ratios = calculate_gear_ratios(engine_map)
    print(f"The sum of all gear ratios in the engine schematic is: {total_gear_ratios}")

if __name__ == "__main__":
    main()
