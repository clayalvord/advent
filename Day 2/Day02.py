import re

input_file = "Day 2/input.txt"

try:
    with open(input_file, 'r') as text_file:
        # Iterate through each line in the file
        for line in text_file:
            # Dictionary to store sums per color for each split in the line
            color_sums = {'red': 0, 'green': 0, 'blue': 0}

            # Split the line at semicolons (;)
            splits = line.split(';')

            # Flag to indicate whether the row should be considered
            consider_row = True

            # Iterate through each split in the line
            for split in splits:
                # Extract all numbers and colors from the split using regular expressions
                matches = re.findall(r'(\d+)\s*([a-zA-Z]+)', split)

                # Process each match
                for number, color in matches:
                    # Sum the numbers per color
                    color_sums[color.lower()] += int(number)

                # Check if the split exceeds the criteria for blue
                if color_sums['blue'] > 14:
                    consider_row = False
                    break  # No need to continue checking if one split exceeds the criteria

            # Check if the row should be considered based on the splits
            if consider_row:
                # Print the results for each split
                print(f"Results for line: {line.strip()}")
                for color, total_sum in color_sums.items():
                    print(f"Total sum for {color.capitalize()}: {total_sum}")
                print("-" * 30)  # Separate results for each split
            else:
                print(f"Ignoring line due to exceeding criteria: {line.strip()}")

            print("=" * 30)  # Separate results for each line

except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
except StopIteration:
    print("File is empty.")
except Exception as e:
    print(f"An error occurred: {e}")
