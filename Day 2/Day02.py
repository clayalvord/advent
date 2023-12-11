import re

input_file = "Day 2/input.txt"

try:
    with open(input_file, 'r') as text_file:
        # Process only the first line in the file
        line = next(text_file)

        # Split the line at semicolons (;)
        splits = line.split(';')

        # Iterate through each split in the first row
        for split in splits:
            # Dictionary to store sums per color for each split
            color_sums = {'red': 0, 'green': 0, 'blue': 0}

            # Extract all numbers and colors from the split using regular expressions
            matches = re.findall(r'(\d+)\s*([a-zA-Z]+)', split)

            # Process each match
            for number, color in matches:
                # Sum the numbers per color
                color_sums[color.lower()] += int(number)

            # Print the results for each split
            print(f"Results for split: {split.strip()}")
            for color, total_sum in color_sums.items():
                print(f"Total sum for {color.capitalize()}: {total_sum}")
            print("-" * 30)  # Separate results for each split

except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
except StopIteration:
    print("File is empty.")
except Exception as e:
    print(f"An error occurred: {e}")
