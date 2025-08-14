file_path = r"C:\Users\Vardhan\Documents\Custom Office Templates\OneDrive\Desktop\ai.txt"

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        print(f"Number of lines in the file: {len(lines)}")
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred: {e}")