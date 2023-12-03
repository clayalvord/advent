# Open the file in the same directory as the script
file_name = "input.txt"
file_path = "./" + file_name  # Assuming the file is in the same directory as the script

try:
    with open(file_path, 'r') as file:
        # Read and print the contents of the file
        file_contents = file.read()
        print("File contents:")
        print(file_contents)
except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
