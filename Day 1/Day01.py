input = "Day 1/input.txt"

try:
    with open(input, 'r') as file:
        # Read and print the contents of the file
        file_contents = file.read()
        print("File contents:")
        print(file_contents)
except FileNotFoundError:
    print(f"Error: File '{input}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")