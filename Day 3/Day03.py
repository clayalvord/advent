import re

# Function to extract numbers from a given string using regular expression
def extract_numbers(input_string):
    return re.findall(r'\d+', input_string)

# Read input file and process each line
input_file_path = "Day 3/input.txt"

with open(input_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        # Extract numbers from the current line
        part_numbers = extract_numbers(line)
        
        # Print the result
        print(f"Row {line_number}: {', '.join(part_numbers)}")
