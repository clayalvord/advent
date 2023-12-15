# Assuming the input file is in the "Day 3" directory
file_path = "Day 3/input.txt"

try:
    with open(file_path, 'r') as file:
        # Read the content of the file
        file_content = file.readlines()

        # Process each row
        for line_number, row in enumerate(file_content, start=1):
            symbols = {'*': 0, '#': 0, '+': 0, '$': 0}

            # Count the occurrences of each symbol in the row
            for symbol in symbols:
                symbols[symbol] = row.count(symbol)

            # Display or process the count of each symbol in the row
            print(f"Row {line_number}: {symbols}")

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
