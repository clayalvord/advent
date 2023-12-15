import re

def calculate_max_colors(line):
    # Initialize variables for the largest number and color
    max_red = 0
    max_green = 0
    max_blue = 0

    # Split the line into segments
    splits = line.split(';')

    # Process each segment
    for segment in splits:
        # Extract numbers and colors using regular expressions
        matches = re.findall(r'(\d+)\s*([a-zA-Z]+)', segment)

        # Update the largest color and number
        for number, color in matches:
            number = int(number)
            if color.lower() == 'red' and number > max_red:
                max_red = number
            elif color.lower() == 'green' and number > max_green:
                max_green = number
            elif color.lower() == 'blue' and number > max_blue:
                max_blue = number

    return max_red, max_green, max_blue

def print_max_colors(line_number, line, max_red, max_green, max_blue):
    # Calculate the product of the max numbers
    product = max_red * max_green * max_blue

    # Truncate the row name and display the largest number, color, and product for the line
    print(f"Line {line_number}: Max Red: {max_red}, Max Green: {max_green}, Max Blue: {max_blue}, Product: {product}, Original line: {line.strip()}")

def main():
    input_file = "Day 2/input.txt"

    try:
        with open(input_file, 'r') as text_file:
            # Enumerate over each line with its corresponding line number
            for line_number, line in enumerate(text_file, start=1):
                # Calculate the largest number and color and print results
                max_red, max_green, max_blue = calculate_max_colors(line)
                print_max_colors(line_number, line, max_red, max_green, max_blue)

                # Print the row separator between every row
                print("-" * 30)

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except StopIteration:
        print("File is empty.")
    except IOError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
