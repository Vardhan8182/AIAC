def format_name(name):
    parts = name.strip().split()
    if len(parts) < 2:
        return name  # Return as is if not enough parts
    # Move the first part to the end
    return ' '.join(parts[1:] + [parts[0]])

# Example usage:
input_name = input("Enter a name: ")
print(format_name(input_name))