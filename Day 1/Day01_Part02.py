input_file = "Day 1/input.txt"

# Store the total sum
total_sum = 0

# Value names to actual values
translation = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

try:
    with open(input_file, 'r') as text_file:
        # Iterate through each line in the file
        for line in text_file:
            # Translate the contents of each row based on the provided translation
            for word, value in translation.items():
                line = line.replace(word, value)

            # Store the first and last numbers for each row
            first_number = None
            last_number = None

            # Iterate through each character in the translated line
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

    # Print the total sum
    print(f"\nTotal Sum of Concatenated 2-Digit Numbers: {total_sum:02d}")

except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
