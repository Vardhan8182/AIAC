import hashlib

def collect_and_store_student_details(filename="students.txt"):
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    email = input("Enter student email: ")

    # Anonymize name and email using SHA-256 hash
    name_hash = hashlib.sha256(name.encode()).hexdigest()
    email_hash = hashlib.sha256(email.encode()).hexdigest()

    # Store anonymized data
    with open(filename, "a") as f:
        f.write(f"NameHash: {name_hash}, Age: {age}, EmailHash: {email_hash}\n")

    print("Student details collected and anonymized.")

if __name__ == "__main__":
    collect_and_store_student_details()