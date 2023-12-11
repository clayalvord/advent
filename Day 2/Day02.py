import re

input_file = "Day 2/input.txt"

try:
    with open(input_file, 'r') as text_file:
        # Dictionary to store sums per color
        color_sums = {'red': 0, 'green': 0, 'blue': 0}

        # Process only the first line in the file
        line = next(text_file)

        # Split the line at the colon (:) and take the right part
        line_data = line.split(':', 1)[-1]

        # Extract all numbers and colors from the right part using regular expressions
        matches = re.findall(r'(\d+)\s*([a-zA-Z]+)', line_data)

        # Process each match
        for number, color in matches:
            # Sum the numbers per color
            color_sums[color.lower()] += int(number)

        # Print the results for the first row
        for color, total_sum in color_sums.items():
            print(f"Total sum for {color.capitalize()} in the first row: {total_sum}")

except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
except StopIteration:
    print("File is empty.")
except Exception as e:
    print(f"An error occurred: {e}")
