input_file = "Day 2/input.txt"

try:
    with open(input_file, 'r') as text_file:
        # Iterate through each line in the file
        for line in text_file:
            # Process each line as needed
            print(line.strip())  # Example: print each line without leading/trailing whitespaces

except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
