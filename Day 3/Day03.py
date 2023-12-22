import re

def extract_numbers_from_line(line):
    return [int(num) for num in re.findall(r'\d+', line)]

def find_symbols_positions(line, symbols):
    positions = {}
    for symbol in symbols:
        symbol_positions = [pos.start() + 1 for pos in re.finditer(re.escape(symbol), line)]
        if symbol_positions:
            positions[symbol] = symbol_positions
    return positions

def scan(lines, row_num, symbol_position):
    approved_numbers = []
    
    # Look 1 position to the right
    match_right = re.search(r'\d+', lines[row_num][symbol_position:])
    if match_right:
        approved_numbers.append(int(match_right.group()))

    # Look 1 position to the left
    match_left = re.search(r'\d+', lines[row_num][:symbol_position])
    if match_left:
        approved_numbers.append(int(match_left.group()))

    # Look at symbol_position on the preceding row
    match_current = re.search(r'\d+', lines[row_num])
    if match_current:
        approved_numbers.append(int(match_current.group()))

    # Look at symbol_position on the following row
    if row_num + 1 < len(lines):
        match_below = re.search(r'\d+', lines[row_num + 1])
        if match_below:
            approved_numbers.append(int(match_below.group()))

    # Look at symbol_position + 1 on the preceding row
    match_above_right = re.search(r'\d+', lines[row_num])
    if match_above_right:
        approved_numbers.append(int(match_above_right.group()))

    # Look at symbol_position - 1 on the preceding row
    match_above_left = re.search(r'\d+', lines[row_num])
    if match_above_left:
        approved_numbers.append(int(match_above_left.group()))

    # Look at symbol_position + 1 on the following row
    if row_num + 1 < len(lines):
        match_below_right = re.search(r'\d+', lines[row_num + 1])
        if match_below_right:
            approved_numbers.append(int(match_below_right.group()))

    # Look at symbol_position - 1 on the following row
    if row_num + 1 < len(lines):
        match_below_left = re.search(r'\d+', lines[row_num + 1])
        if match_below_left:
            approved_numbers.append(int(match_below_left.group()))

    return approved_numbers

def process_input_file(file_path):
    symbols_to_find = "*#+$"
    
    with open(file_path, 'r') as file:
        lines = file.readlines()

    row_num = 0
    for line in lines:
        line = line.strip()
        if line:
            row_num += 1
            part_numbers = extract_numbers_from_line(line)
            symbol_positions = find_symbols_positions(line, symbols_to_find)
            
            row_data = f"Row {row_num} [{', '.join(map(str, part_numbers))}]"
            
            if symbol_positions:
                for symbol, positions in symbol_positions.items():
                    for symbol_position in positions:
                        approved_numbers = scan(lines, row_num - 1, symbol_position - 1)
                        print(f"{row_data} for {symbol} at position {symbol_position} [{', '.join(map(str, approved_numbers))}]")
            else:
                print(row_data)

if __name__ == "__main__":
    input_file_path = "Day 3/input.txt"
    process_input_file(input_file_path)
