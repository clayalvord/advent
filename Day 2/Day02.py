import re

def process_line(line):
    ignore_reason = None

    # Split the line into segments
    splits = line.split(';')

    # Process each segment
    for split in splits:
        # Extract numbers and colors using regular expressions
        matches = re.findall(r'(\d+)\s*([a-zA-Z]+)', split)

        # Check if red, green, or blue exceeds criteria
        for number, color in matches:
            if color.lower() == 'red' and int(number) > 12:
                ignore_reason = f'Red exceeds 12 ({number})'
            elif color.lower() == 'green' and int(number) > 13:
                ignore_reason = f'Green exceeds 13 ({number})'
            elif color.lower() == 'blue' and int(number) > 14:
                ignore_reason = f'Blue exceeds 14 ({number})'

    return ignore_reason

def print_results(line, ignore_reason):
    if ignore_reason is None:
        # Display results for the line
        print(f"Results for line: {line.strip()}")
        print("-" * 30)
    else:
        # Display the specific reason for ignoring the line
        print(f"Ignoring line due to: {ignore_reason}: {line.strip()}")

def main():
    input_file = "Day 2/input.txt"

    try:
        with open(input_file, 'r') as text_file:
            for line in text_file:
                # Process each line and print results
                ignore_reason = process_line(line)
                print_results(line, ignore_reason)

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except StopIteration:
        print("File is empty.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
