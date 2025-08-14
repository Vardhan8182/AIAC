# Get the number of students
n = int(input("Enter number of students: "))

emails = []
for _ in range(n):
    name = input("Enter student name: ").strip()
    parts = name.split()
    if len(parts) < 2:
        print("Please enter both first and last name.")
        continue
    first, last = parts[0], parts[-1]
    email = f"{first[0].lower()}{last.lower()}@sru.edu.in"
    emails.append(email)

print("Generated Email IDs:")
for email in emails:
    print(email)