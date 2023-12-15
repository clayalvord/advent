# Assuming the input file is in the "Day 3" directory
file_path = "Day 3/input.txt"

try:
    with open(file_path, 'r') as file:
        # Read the content of the file
        file_content = file.read()

        # Display or process the content as needed
        print("File Content:")
        print(file_content)

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
