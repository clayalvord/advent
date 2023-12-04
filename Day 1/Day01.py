input_file = "Day 1/input.txt"

# Initialize variables to store the first and last numbers
first_number = None
last_number = None

try:
    with open(input_file, 'r') as text_file:
        # Read only the first line of the file
        first_line = text_file.readline()

        # Iterate through each character in the first line
        for char in first_line:
            # Check if the character is a digit
            if char.isdigit():
                # If it's the first number, store it
                if first_number is None:
                    first_number = char
                # Always update the last number
                last_number = char

    # Concatenate the first and last numbers to make a 2-digit number
    two_digit_number = int(str(first_number) + str(last_number)) if first_number is not None and last_number is not None else None

    # Print the results
    if two_digit_number is not None:
        print(f"Concatenated 2-Digit Number: {two_digit_number:02d}")
    else:
        print("No numbers found in the file.")

except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
