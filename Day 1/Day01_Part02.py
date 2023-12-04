input_file = "Day 1/input.txt"

# variable to store the total sum
total_sum = 0

try:
    with open(input_file, 'r') as text_file:
        
        # Iterate through each line in the file
        for line in text_file:
            
            # variables to store the first and last numbers for each row
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

    # Print the total sum
    print(f"Total Sum of Concatenated 2-Digit Numbers: {total_sum:02d}")

except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
