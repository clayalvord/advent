import re

input_file = "Day 2/input.txt"

try:
    with open(input_file, 'r') as text_file:
        # Iterate through each line in the file
        for line in text_file:
            # Extract all numbers from the line using regular expression
            numbers = [int(match) for match in re.findall(r'\d+', line)]
            
            # Calculate the sum of numbers on the current line
            line_sum = sum(numbers)
            
            # Print the result
            print(f"Line: {line.strip()}, Sum: {line_sum}")

except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
