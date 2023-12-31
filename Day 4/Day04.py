def read_input_file(file_path):
    CARD_PREFIX = "Card"
    DELIMITER = ":"
    total_points = 0  # Variable to keep track of the total points

    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()

                if line.startswith(CARD_PREFIX):
                    parts = line.split(DELIMITER)
                    if len(parts) == 2:
                        card_number = parts[0].strip().split()[1]
                        winning_numbers, player_numbers = map(str.split, parts[1].strip().split("|"))

                        winning_numbers_set = set(map(int, winning_numbers))
                        player_numbers_set = set(map(int, player_numbers))

                        matching_numbers = winning_numbers_set.intersection(player_numbers_set)
                        matched_quantity = len(matching_numbers)

                        card_score = 1 if matched_quantity > 0 else 0

                        if card_score == 1:
                            matched_quantity -= 1
                            for _ in range(matched_quantity):
                                card_score *= 2

                        total_points += card_score

                        print(f"Card {card_number} - Matching Numbers: {matching_numbers}, Points: {card_score}, Matched Quantity: {matched_quantity}")

            # Print the total points after processing all cards
            print(f"\nTotal Points: {total_points}")

    except FileNotFoundError:
        print(f"Error: Input file not found at {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file_path = "Day 4/input.txt"  # Replace with the correct path to your input file
    read_input_file(input_file_path)
