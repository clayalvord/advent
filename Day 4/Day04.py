# Filename: read_input.py

def read_input_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    input_file_path = "Day 4/input.txt"  # Replace with the correct path to your input file
    file_content = read_input_file(input_file_path)

    if file_content is not None:
        print(f"Contents of the file:\n{file_content}")
