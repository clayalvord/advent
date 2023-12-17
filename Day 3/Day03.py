import os
import re

file_path = os.path.join("Day 3", "input.txt")

try:
    with open(file_path, 'r') as file:
        for line_number, row in enumerate(file, start=1):
            part_numbers = [match for group in re.findall(r'[*#+$](\d+)|(\d+)[*#+$]', row) for match in group if match]
            print(f"Row {line_number}: {', '.join(part_numbers)}")

except FileNotFoundError as e:
    print(f"Error: {e}")
except IOError as e:
    print(f"IOError: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
