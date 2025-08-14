full_name = input("Enter a name: ")
parts = full_name.strip().split()
if len(parts) >= 2:
    formatted_name = f"{parts[-1]} {' '.join(parts[:-1])}"
    print(formatted_name)
else:
    print(full_name)
