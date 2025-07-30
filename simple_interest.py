# simple_interest.py

def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest.

    Parameters:
    principal (float): The principal amount
    rate (float): The annual interest rate (in percentage)
    time (float): The time in years

    Returns:
    float: Simple interest
    """
    return (principal * rate * time) / 100

if __name__ == "__main__":
    try:
        p = float(input("Enter principal amount: "))
        r = float(input("Enter rate of interest (%): "))
        t = float(input("Enter time (in years): "))

        si = calculate_simple_interest(p, r, t)
        print(f"Simple Interest = {si}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
