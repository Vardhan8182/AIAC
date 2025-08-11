def sort_numbers_menu():
    """
    Prompts the user to enter a list of numbers and select a sorting/filtering option.
    Displays the result based on the user's choice.
    """
    try:
        numbers_input = input("Enter numbers separated by spaces: ")
        numbers = [int(num) for num in numbers_input.strip().split()]
        if not numbers:
            print("No numbers entered.")
            return

        print("Select an option:")
        print("1. Sort in ascending order")
        print("2. Sort in descending order")
        print("3. Show only odd numbers")
        print("4. Show only even numbers")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            result = sorted(numbers)
            print("Numbers in ascending order:", result)
        elif choice == '2':
            result = sorted(numbers, reverse=True)
            print("Numbers in descending order:", result)
        elif choice == '3':
            result = [num for num in numbers if num % 2 != 0]
            print("Odd numbers:", result)
        elif choice == '4':
            result = [num for num in numbers if num % 2 == 0]
            print("Even numbers:", result)
        else:
            print("Invalid choice. Please select a valid option.")
    except ValueError:
        print("Invalid input. Please enter integers only.")

if __name__ == "__main__":
    sort_numbers_menu()
