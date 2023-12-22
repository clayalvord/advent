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

def scan(line, symbol_position):
    approved_numbers = []
    
    # Look 1 position to the right
    match_right = re.search(r'\d+', line[symbol_position:])
    if match_right:
        approved_numbers.append(int(match_right.group()))

    # Look 1 position to the left
    match_left = re.search(r'\d+', line[:symbol_position])
    if match_left:
        approved_numbers.append(int(match_left.group()))

    # Look at symbol_position on the preceding row
    match_current = re.search(r'\d+', line)
    if match_current:
        approved_numbers.append(int(match_current.group()))

    # Look at symbol_position on the following row
    if symbol_position < len(line):
        match_below = re.search(r'\d+', line)
        if match_below:
            approved_numbers.append(int(match_below.group()))

    # Look at symbol_position + 1 on the preceding row
    match_above_right = re.search(r'\d+', line)
    if match_above_right:
        approved_numbers.append(int(match_above_right.group()))

    # Look at symbol_position - 1 on the preceding row
    match_above_left = re.search(r'\d+', line)
    if match_above_left:
        approved_numbers.append(int(match_above_left.group()))

    # Look at symbol_position + 1 on the following row
    if symbol_position < len(line):
        match_below_right = re.search(r'\d+', line)
        if match_below_right:
            approved_numbers.append(int(match_below_right.group()))

    # Look at symbol_position - 1 on the following row
    if symbol_position < len(line):
        match_below_left = re.search(r'\d+', line)
        if match_below_left:
            approved_numbers.append(int(match_below_left.group()))

    return approved_numbers

def process_input_file(file_path):
    symbols_to_find = "*#+$"
    
    with open(file_path, 'r') as file:
        for row_num, line in enumerate(file, start=1):
            part_numbers = extract_numbers_from_line(line)
            symbol_positions = find_symbols_positions(line, symbols_to_find)
            
            if symbol_positions:
                for symbol, positions in symbol_positions.items():
                    for symbol_position in positions:
                        approved_numbers = scan(line, symbol_position)
                        print(f"Row {row_num}, Approved Numbers for {symbol} at position {symbol_position}: {approved_numbers}")

if __name__ == "__main__":
    input_file_path = "Day 3/input.txt"
    process_input_file(input_file_path)
