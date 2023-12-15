def is_part_number(engine, row, col):
    # Check if the given position is a part number
    if 0 <= row < len(engine) and 0 <= col < len(engine[0]) and engine[row][col].isdigit():
        return True
    return False

def find_adjacent_numbers(engine, row, col):
    # Find all adjacent numbers to a symbol at the given position
    adjacent_numbers = []
    symbols = ['*', '#', '+', '$']

    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if 0 <= i < len(engine) and 0 <= j < len(engine[0]) and (i != row or j != col):
                if is_part_number(engine, i, j):
                    adjacent_numbers.append(int(engine[i][j]))
                elif engine[i][j] in symbols:
                    # Handle non-numeric characters differently (optional)
                    adjacent_numbers.append(engine[i][j])

    return adjacent_numbers

def find_missing_part(engine):
    # Find the sum of all part numbers adjacent to a symbol
    total_sum = 0

    for i in range(len(engine)):
        for j in range(len(engine[0])):
            if is_part_number(engine, i, j):
                adjacent_numbers = find_adjacent_numbers(engine, i, j)
                total_sum += sum(adjacent_numbers)

    return total_sum

# Specify the input file path
input_path = "Day 3/input.txt"

# Read the engine schematic from the file
with open(input_path, "r") as file:
    engine_schematic = [line.strip() for line in file]

result = find_missing_part(engine_schematic)
print("Sum of part numbers adjacent to a symbol:", result)
