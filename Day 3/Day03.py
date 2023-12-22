# Read input file and store each line in the schematic list
with open("Day 3/input.txt") as file:
    schematic = [line.rstrip("\n") for line in file]

# Initialize variables
used_positions = []
part_sum = 0
ratio_sum = 0

# Iterate through each position in the schematic
for y, line in enumerate(schematic):
    for x, char in enumerate(line):
        # Check if the character is not a dot or a number
        if char not in ".0123456789":
            adj_count = 0
            ratio = 1

            # Define relative positions of adjacent cells
            adjacent_positions = [
                (x + 1, y), (x + 1, y + 1), (x, y + 1), (x - 1, y + 1),
                (x - 1, y), (x - 1, y - 1), (x, y - 1), (x + 1, y - 1)
            ]

            # Check each adjacent position
            for pos in adjacent_positions:
                # Check if the position is within the bounds of the schematic
                if 0 <= pos[0] < len(line) and 0 <= pos[1] < len(schematic):
                    # Check if the character at the position is a number
                    if schematic[pos[1]][pos[0]] in "0123456789" and pos not in used_positions:
                        part = schematic[pos[1]][pos[0]]
                        used_positions.append(pos)

                        # Check positions to the left of the current position
                        for direction in [-1, 1]:
                            check_x = pos[0] + direction

                            while (
                                0 <= check_x < len(line)
                                and schematic[pos[1]][check_x] in "0123456789"
                                and (check_x, pos[1]) not in used_positions
                            ):
                                part = (
                                    schematic[pos[1]][check_x] + part
                                    if direction == -1
                                    else part + schematic[pos[1]][check_x]
                                )
                                used_positions.append((check_x, pos[1]))
                                check_x += direction

                        part_sum += int(part)

                        # Check if the current character is "*" and the adjacent count is less than 2
                        if char == "*" and adj_count < 2:
                            adj_count += 1
                            ratio *= int(part)

            # Check if the adjacent count is 2 and update the ratio sum
            if adj_count == 2:
                ratio_sum += ratio

# Print results
print(f"Part 1: {part_sum}")
print(f"Part 2: {ratio_sum}")
