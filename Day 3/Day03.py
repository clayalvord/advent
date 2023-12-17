import os
import re

file_path = os.path.join("Day 3", "input.txt")

try:
    with open(file_path, 'r') as file:
        file_content = file.readlines()
        part_number_pattern = re.compile(r'\b\d+\b')

        for line_number, row in enumerate(file_content, start=1):
            symbols = re.findall(r'[*#+$]', row)
            part_numbers = part_number_pattern.findall(row)

            print(f"Row {line_number}: Symbols: {symbols}, Part Numbers: {part_numbers}")

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except IOError as e:
    print(f"IOError: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
