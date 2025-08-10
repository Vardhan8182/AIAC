def temperature_conversion():
    """
    Prompts the user to enter a temperature and convert between Celsius and Fahrenheit.
    """
    print("=== Temperature Conversion ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Select conversion type (1/2): ").strip()
    if choice == '1':
        try:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C = {fahrenheit:.2f}°F")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    elif choice == '2':
        try:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit}°F = {celsius:.2f}°C")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print("Invalid choice. Please select 1 or 2.")

def temperature_menu():
    """
    Displays the temperature conversion menu and continues until the user chooses to exit.
    """
    while True:
        print("\n--- Temperature Conversion Menu ---")
        print("1. Convert Temperature")
        print("2. Exit")
        menu_choice = input("Enter your choice (1/2): ").strip()
        if menu_choice == '1':
            temperature_conversion()
        elif menu_choice == '2':
            print("Exiting Temperature Conversion Menu.")
            break
        else:
            print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    temperature_menu()
