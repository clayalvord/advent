import re

def check_color_criteria(color, number):
    if color.lower() == 'red' and int(number) > 12:
        return f'Red exceeds 12 ({number})'
    elif color.lower() == 'green' and int(number) > 13:
        return f'Green exceeds 13 ({number})'
    elif color.lower() == 'blue' and int(number) > 14:
        return f'Blue exceeds 14 ({number})'
    return None

def process_line(line_number, line):
    ignore_reason = None

    # Split the line into segments
    splits = line.split(';')

    # Process each segment
    for segment in splits:
        # Extract numbers and colors using regular expressions
        matches = re.findall(r'(\d+)\s*([a-zA-Z]+)', segment)

        # Check if red, green, or blue exceeds criteria
        for number, color in matches:
            ignore_reason = check_color_criteria(color, number)
            if ignore_reason:
                return ignore_reason, line_number

    return ignore_reason, line_number

def print_results(line_number, line, ignore_reason):
    if ignore_reason is None:
        # Display results for the line
        print(f"Results for line {line_number}: {line.strip()}")
        print("-" * 30)
        return line_number
    else:
        # Display the specific reason for ignoring the line
        print(f"Ignoring line {line_number} due to: {ignore_reason}: {line.strip()}")
        return 0  # Return 0 for ignored lines

def main():
    input_file = "Day 2/input.txt"
    total_line_numbers = 0  # Accumulate line numbers for lines that were not ignored

    try:
        with open(input_file, 'r') as text_file:
            for line_number, line in enumerate(text_file, start=1):
                # Process each line and print results
                ignore_reason, line_number = process_line(line_number, line)
                total_line_numbers += print_results(line_number, line, ignore_reason)

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except StopIteration:
        print("File is empty.")
    except Exception as e:
        print(f"An error occurred: {e}")

    print(f"Sum of line numbers for non-ignored lines: {total_line_numbers}")

if __name__ == "__main__":
    main()
