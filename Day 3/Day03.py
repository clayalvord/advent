import re

# Assuming the input file is in the "Day 3" directory
file_path = "Day 3/input.txt"

try:
    with open(file_path, 'r') as file:
        # Read the content of the file
        file_content = file.readlines()

        # Define the regular expression pattern to identify part numbers
        part_number_pattern = r'\b\d+\b'

        # Process each row
        for line_number, row in enumerate(file_content, start=1):
            # Find all symbols in the row
            symbols = {'*': 0, '#': 0, '+': 0, '$': 0}
            for symbol in symbols:
                symbols[symbol] = row.count(symbol)

            # Find all part numbers in the row using the regular expression
            part_numbers = re.findall(part_number_pattern, row)

            # Display or process the symbols and part numbers found in the row
            print(f"Row {line_number}: Symbols: {symbols}, Part Numbers: {part_numbers}")

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
