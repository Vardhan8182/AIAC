def register_user(users_db):
    """
    Registers a new user by taking username and password input from the console.
    Stores the user in the users_db dictionary.
    """
    print("=== User Registration ===")
    username = input("Enter a username: ").strip()
    if username in users_db:
        print("Username already exists. Please choose a different username.")
        return
    password = input("Enter a password: ").strip()
    users_db[username] = password
    print("Registration successful!")

def login_user(users_db):
    """
    Logs in a user by verifying username and password from the console input.
    """
    print("=== User Login ===")
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    if username in users_db and users_db[username] == password:
        print("Login successful! Welcome,", username)
    else:
        print("Invalid username or password.")

if __name__ == "__main__":
    users_db = {}
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Select an option (1-3): ").strip()
        if choice == '1':
            register_user(users_db)
        elif choice == '2':
            login_user(users_db)
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
