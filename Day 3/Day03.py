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

def process_input_file(file_path):
    symbols_to_find = "*#+$"
    
    with open(file_path, 'r') as file:
        for row_num, line in enumerate(file, start=1):
            part_numbers = extract_numbers_from_line(line)
            symbol_positions = find_symbols_positions(line, symbols_to_find)
            
            print(f"Row {row_num}: {', '.join(map(str, part_numbers))}")
            if symbol_positions:
                print(f"   Symbol positions: {symbol_positions}")

if __name__ == "__main__":
    input_file_path = "Day 3/input.txt"
    process_input_file(input_file_path)