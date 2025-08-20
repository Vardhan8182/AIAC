def collect_and_save_student_details():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    email = input("Enter student email: ")

    with open("student_details.txt", "a") as file:
        file.write(f"Name: {name}, Age: {age}, Email: {email}\n")

# Example usage
if __name__ == "__main__":
    collect_and_save_student_details()