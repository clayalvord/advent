import os
import re

file_path = os.path.join("Day 3", "input.txt")

try:
    with open(file_path, 'r') as file:
        file_content = file.readlines()

        # Updated part_number_pattern to capture numbers immediately following a symbol
        part_number_pattern = re.compile(r'[*#+$](\d+)|(\d+)[*#+$]')

        for line_number, row in enumerate(file_content, start=1):
            symbols = re.findall(r'[*#+$]', row)
            part_numbers = [match.group(1) or match.group(2) for match in part_number_pattern.finditer(row)]

            print(f"Row {line_number}: Symbols: {symbols}, Part Numbers: {part_numbers}")

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except IOError as e:
    print(f"IOError: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
