input_file = "Day 1/input.txt"

# Store the total sum
total_sum = 0

# Conversion dataset
data_set = {
    'one': 'one1one',
    'two': 'two2two',
    'three': 'three3three',
    'four': 'four4four',
    'five': 'five5five',
    'six': 'six6six',
    'seven': 'seven7seven',
    'eight': 'eight8eight',
    'nine': 'nine9nine'
}

try:
    # Read the input file and apply the conversion dataset
    with open(input_file, 'r') as text_file:
        lines = text_file.readlines()

    # Update the lines using the conversion dataset
    updated_lines = []
    for line in lines:
        for key, value in data_set.items():
            line = line.replace(key, value)
        updated_lines.append(line)

    # Write the updated lines back to the input file
    with open(input_file, 'w') as text_file:
        text_file.writelines(updated_lines)

    # Iterate through each line in the updated file
    for line in updated_lines:
        # Store the first and last numbers for each row
        first_number = None
        last_number = None

        # Iterate through each character in the line
        for char in line:
            # Check if the character is a digit
            if char.isdigit():
                # If it's the first number, store it
                if first_number is None:
                    first_number = char
                # Always update the last number
                last_number = char

        # Concatenate the first and last numbers to make a 2-digit number for each row
        two_digit_number = int(str(first_number) + str(last_number)) if first_number is not None and last_number is not None else None

        # Sum the results for each row
        if two_digit_number is not None:
            total_sum += two_digit_number

            print(f"Row: {line.strip()}, Concatenated 2-Digit Number: {two_digit_number:02d}")

        else:
            print(f"Row: {line.strip()}, No numbers found in the row.")

    # Print the total sum
    print(f"\nTotal Sum of Concatenated 2-Digit Numbers: {total_sum:02d}")

except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
