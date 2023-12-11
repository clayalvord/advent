import re
from collections import defaultdict

def process_line(line):
    color_sums = defaultdict(int)
    ignore_reason = None

    splits = line.split(';')

    for split in splits:
        matches = re.findall(r'(\d+)\s*([a-zA-Z]+)', split)
        for number, color in matches:
            color_sums[color.lower()] += int(number)

        # Check if the split exceeds the criteria for blue or green
        if color_sums['blue'] > 14 or color_sums['green'] > 13:
            ignore_reason = 'Blue exceeds 14' if color_sums['blue'] > 14 else 'Green exceeds 13'
            break

    return ignore_reason, color_sums

def print_results(line, ignore_reason, color_sums):
    if ignore_reason is None:
        print(f"Results for line: {line.strip()}")
        for color, total_sum in color_sums.items():
            print(f"Total sum for {color.capitalize()}: {total_sum}")
        print("-" * 30)
    else:
        print(f"Ignoring line due to: {ignore_reason}: {line.strip()}")

    print("=" * 30)

def main():
    input_file = "Day 2/input.txt"

    try:
        with open(input_file, 'r') as text_file:
            for line in text_file:
                ignore_reason, color_sums = process_line(line)
                print_results(line, ignore_reason, color_sums)

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except StopIteration:
        print("File is empty.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
