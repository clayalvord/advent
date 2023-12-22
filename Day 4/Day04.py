# Filename: read_input.py

def read_input_file(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read each line (card) sequentially
            for line in file:
                line = line.strip()

                # Skip lines that start with "Card"
                if line.startswith("Card"):
                    parts = line.split(":")
                    if len(parts) == 2:
                        card_number = parts[0].strip().split()[1]
                        numbers = parts[1].strip().split("|")

                        # Convert the numbers to sets for easy comparison
                        winning_numbers_set = set(map(int, numbers[0].split()))
                        player_numbers_set = set(map(int, numbers[1].split()))

                        # Find the matching numbers
                        matching_numbers = winning_numbers_set.intersection(player_numbers_set)

                        # Print the desired output format
                        print(f"Card {card_number} - Matching Numbers: {matching_numbers}")

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file_path = "Day 4/input.txt"  # Replace with the correct path to your input file
    read_input_file(input_file_path)
