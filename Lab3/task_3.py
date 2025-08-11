def calculate_power_bill(units):
    """
    Calculates the power bill based on the number of units consumed.
    Example slab:
        - First 100 units: Rs. 5/unit
        - Next 100 units (101-200): Rs. 7/unit
        - Above 200 units: Rs. 10/unit
    """
    if units < 0:
        raise ValueError("Units consumed cannot be negative.")
    bill = 0
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    else:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10
    return bill

def get_customer_details():
    """
    Prompts the user to enter customer details and returns them as a dictionary.
    """
    print("Enter Customer Details:")
    name = input("Name: ").strip()
    customer_id = input("Customer ID: ").strip()
    address = input("Address: ").strip()
    return {
        "name": name,
        "customer_id": customer_id,
        "address": address
    }

def show_previous_bill_details(previous_bills):
    """
    Displays previous bill details for the customer.
    previous_bills: list of dicts with keys 'month', 'units', 'amount'
    """
    if not previous_bills:
        print("No previous bill details available.")
        return
    print("\nPrevious Bill Details:")
    for bill in previous_bills:
        print(f"Month: {bill['month']}, Units: {bill['units']}, Amount: Rs. {bill['amount']}")

if __name__ == "__main__":
    customer = get_customer_details()
    try:
        units = int(input("Enter number of units consumed this month: "))
        amount = calculate_power_bill(units)
        print(f"\nCustomer: {customer['name']} (ID: {customer['customer_id']})")
        print(f"Address: {customer['address']}")
        print(f"Units Consumed: {units}")
        print(f"Total Bill Amount: Rs. {amount}")
    except ValueError as e:
        print(f"Invalid input: {e}")

    # Example previous bills (in a real application, this would come from a database)
    previous_bills = [
        {"month": "April", "units": 120, "amount": calculate_power_bill(120)},
        {"month": "March", "units": 95, "amount": calculate_power_bill(95)},
        {"month": "February", "units": 210, "amount": calculate_power_bill(210)},
    ]
    show_previous_bill_details(previous_bills)

