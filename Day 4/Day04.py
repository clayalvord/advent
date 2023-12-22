def calculate_points(card):
    # Split the card into winning numbers and numbers you have
    winning_numbers, your_numbers = map(str.split, card.split('|'))

    # Convert the lists to sets for easy comparison
    winning_numbers = set(map(int, winning_numbers))
    your_numbers = set(map(int, your_numbers))

    # Find the common numbers and calculate points
    common_numbers = your_numbers.intersection(winning_numbers)
    points = sum([2 ** i for i in range(len(common_numbers))])

    return points

def main():
    # Read input from file
    file_path = "Day 4/input.txt"
    with open(file_path, "r") as file:
        puzzle_input = file.read().splitlines()

    total_points = 0
    for card in puzzle_input:
        points = calculate_points(card)
        total_points += points

    print("Total points:", total_points)

if __name__ == "__main__":
    main()
