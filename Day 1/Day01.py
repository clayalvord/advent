input = "Day 1/input.txt"

# Initialize variables to store the first and last numbers
first_number = None
last_number = None

try:
    with open(input, 'r') as text_file:
        # Read the entire content of the file
        content = text_file.read()

        # Iterate through each character in the content
        for char in content:
            # Check if the character is a digit
            if char.isdigit():
                # If it's the first number, store it
                if first_number is None:
                    first_number = char
                # Always update the last number
                last_number = char

    # Print the results
    if first_number is not None:
        print(f"First Number: {first_number}")
    else:
        print("No numbers found in the file.")

    if last_number is not None:
        print(f"Last Number: {last_number}")
    else:
        print("No numbers found in the file.")

except FileNotFoundError:
    print(f"Error: File '{input}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
