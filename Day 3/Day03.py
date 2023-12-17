import re

def extract_numbers_and_chars_from_line(line):
    # Adjust the regular expression to include the characters you want to identify
    matches = re.finditer(r'([+*#&]+)|(\d+)', line)
    result = [(match.group(), match.start()) for match in matches]
    return result

def process_input_file(file_path):
    with open(file_path, 'r') as file:
        for row_num, line in enumerate(file, start=1):
            symbols_and_positions = extract_numbers_and_chars_from_line(line)
            if symbols_and_positions:
                print(f"Row {row_num}:")
                for symbol, position in symbols_and_positions:
                    print(f"    Symbol: {symbol}, Position: {position}")

if __name__ == "__main__":
    input_file_path = "Day 3/input.txt"
    process_input_file(input_file_path)
